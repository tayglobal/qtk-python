from fields import Field as F
from converters import QuantLibConverter as qlf
import QuantLib as ql
import uuid
import networkx as nx



class Controller(object):

    def __init__(self, data):
        self._data = data if isinstance(data, list) else [data]

        self._templates = [qlf.to_template(d[F.TEMPLATE.id]) for d in self._data]  # get class
        self._creators = [t.get_creator()(self._data[i]) for i, t in enumerate(self._templates)]
        self._check_assign_object_id()

    def parse(self):
        for c in self._creators:
            c.check()

    def process(self, asof_date, check=True, parse=True):
        asof_date = qlf.to_date(asof_date)
        ql.Settings.instance().evaluationDate = asof_date

        if parse:
            self.parse()

        for c in self._creators:
            c.create(asof_date)

        return self._data

    def _check_assign_object_id(self):
        for d in self._data:
            d.setdefault(F.OBJECT_ID.id, uuid.uuid4())

    def _identify_dependency(self):
        pass