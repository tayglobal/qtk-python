from fields import Field as fl
from converters import QuantLibConverter as qlf


class Controller(object):

    def __init__(self, data, in_place=False):
        self._data = data if isinstance(data, list) else [data]

        self._templates = [qlf.to_template(d[fl.TEMPLATE.id]) for d in self._data]  # get class
        self._creators = [t.get_creator(self._data) for t in self._template]

    def parse(self):
        for c in self._creators:
            c.check()
