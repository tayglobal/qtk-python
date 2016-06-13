

class Name(object):

    def __init__(self, name, name_id):
        self._id = name_id
        self._name = name
        self._id_map[self._id] = self

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self.__class__)+"."+self._id

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