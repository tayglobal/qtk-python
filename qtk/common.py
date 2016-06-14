

class TemplateBase(object):
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
        self._instance_id = data[fl.TEMPLATE.id],
        self._conventions = {} if conventions is None else conventions
        self._data = data
        # self._global_conventions =

    def get(self, field, default_value=None):
        return self._data.get(field.id, self._conventions.get(field.id, default_value))


class AssetName(Name):
    _id_map = {}

    def __init__(self, asset_name):
        asset_id = self.toid(asset_name)
        super(AssetName, self).__init__(asset_name, asset_id)


class SecurityType(Name):
    _id_map = {}

    def __init__(self, security_type):
        type_id = self.toid(security_type)
        super(SecurityType, self).__init__(security_type, type_id)


class SecuritySubType(Name):
    _id_map = {}

    def __init__(self, security_subtype):
        type_id = self.toid(security_subtype)
        super(SecuritySubType, self).__init__(security_subtype, type_id)


class Instrument(Name, TemplateBase):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" %(security_type.id, security_subtype.id, self.toid(instrument_name))
        super(Instrument, self).__init__(instrument_name, inst_id, True)
        TemplateBase.__init__(self)

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def security_type(self):
        return self._security_type

    @property
    def security_subtype(self):
        return self._security_subtype


class Asset(object):
    FIXED_INCOME = AssetName("Fixed Income")
    EQUITY = AssetName("Equity")


class SecurityTypeList(object):
    GOVERNMENT = SecurityType("Government")
    CORPORATE = SecurityType("Corporate")


class SecuritySubTypeList(object):
    BOND = SecuritySubType("Bond")
    ZCB = SecuritySubType("ZCB")  # Zero coupon bond


class Collection(Name, TemplateBase):
    _id_map = {}

    def __init__(self, name):
        collection_id = self.toid(name)
        super(Collection, self).__init__(name, collection_id, True)
        TemplateBase.__init__(self)


class DataType(object):
    TEMPLATE = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    BOOL = 4
    LIST = 5
    DICT = 6
    DATE = 11
    FREQUENCY = 12
    DAYCOUNT = 13
    DAY_CONVENTION = 14
    CALENDAR = 15


class Field(Name):
    _id_map = {}

    def __init__(self, name, desc, data_type):
        field_id = self.toid(name)
        super(Field, self).__init__(name, field_id)
        self._desc = desc
        self._data_type = data_type

    @property
    def description(self):
        return self._desc

    def data_type(self):
        return self._data_type