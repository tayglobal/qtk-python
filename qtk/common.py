

class Instance(object):
    _inst_map = {}

    def __init__(self):
        self._instance_name = self.__class__.__name__
        self._iid = Name.toid(self._instance_name)
        self._inst_map[self._instance_name] = self.__class__

    @property
    def instance_name(self):
        return self._instance_name

    @property
    def iid(self):
        """
        Get instance id
        :return: Instance id
        """
        return self._iid

    @classmethod
    def lookup_instance(cls, field_id):
        c_name = field_id.split(".")[0]
        c = cls._inst_map[c_name]
        return getattr(c, "lookup")(field_id)


class Name(object):

    def __init__(self, name, name_id, is_instance=False):
        prefix = self.__class__.__name__+"." if is_instance else ""
        self._id = prefix+name_id
        self._name = name
        self._id_map[self._id] = self

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @staticmethod
    def toid(name):
        return ''.join(x for x in name.title() if not x.isspace())

    @classmethod
    def lookup(cls, field_id):
        return cls._id_map[field_id]


class CheckedDataFieldGetter(object):

    def __init__(self, data, conventions=None):
        from .fields import FieldList as fl
        self._instance_id = data[fl.INSTANCE.id],
        self._conventions = {} if conventions is None else conventions
        self._data = data
        # self._global_conventions =

    def get(self, field, default_value=None):
        return self._data.get(field.id, self._conventions.get(field.id, default_value))
