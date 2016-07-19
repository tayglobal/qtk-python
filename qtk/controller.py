from .fields import Field as F, FieldName
from .common import DataType as D
from converters import QuantLibConverter as qlf
import QuantLib as ql
import networkx as nx
import uuid


class Controller(object):
    _ROOT = "~ROOT~"

    def __init__(self, data):
        self._data = data if isinstance(data, list) else [data]
        self._graph = nx.DiGraph()
        self._parse_dependency(self._data, self._graph)
        self._node_creators = self._compile_node_creator_list()

    def parse(self):
        for n,c in self._node_creators:
            c.check()

    def process(self, asof_date, check=True, parse=True, context=None):
        asof_date = qlf.to_date(asof_date)
        ql.Settings.instance().evaluationDate = asof_date

        if parse:
            self.parse()

        for n, c in self._node_creators:
            obj = c.create(asof_date)
            for p in self._graph.predecessors(n):
                field_id = self._graph.edge[p][n].get("field_id")
                if field_id:
                    data = self._graph.node[p]["data"]
                    data[field_id] = obj

        return self._data

    @classmethod
    def _parse_dependency(cls, data_list, graph, parent_id=_ROOT):

        for data in data_list:
            data.setdefault(F.OBJECT_ID.id, str(uuid.uuid4()))
            object_id = data[F.OBJECT_ID.id]
            template = qlf.to_template(data[F.TEMPLATE.id])
            creator = template.get_creator()(data)
            graph.add_node(object_id, template=template, creator=creator, data=data)
            graph.add_edge(parent_id, object_id)  # dependency that doesn't need injection

            for field_id, value in data.iteritems():
                field = FieldName.lookup(field_id)
                if isinstance(value, str) and value[:2] == '->':
                    dependency = value[2:].strip()
                    graph.add_edge(object_id, dependency, field_id=field_id)  # dependency needs injection

                if (field.data_type == D.LIST) and isinstance(value, list):
                    cls._parse_dependency(value, graph, object_id)
        return

    def _compile_node_creator_list(self):
        graph = self._graph
        cycles = list(nx.simple_cycles(graph))
        if len(cycles):
            raise ValueError("Found cycles in dependencies "+str(cycles))
        else:
            nodes = list(nx.dfs_postorder_nodes(graph))
            creators = [(n, graph.node[n]['creator']) for n in nodes if n != self._ROOT]
            return creators
