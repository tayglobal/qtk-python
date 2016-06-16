

class TemplateBase(object):
    _inst_map = {}
    _creator = None
    _req_fields = None
    _opt_fields = None

    def __init__(self):
        self._instance_name = self.__class__.__name__
        self._iid = NameBase.toid(self._instance_name)
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

    @classmethod
    def get_creator(cls):
        return cls._creator

    @classmethod
    def get_req_fields(cls):
        return cls._req_fields

    @classmethod
    def get_opt_fields(cls):
        return cls._opt_fields

    @classmethod
    def _set_creator(cls, creator):
        cls._creator = creator

    @classmethod
    def _set_req_fields(cls, req_fields):
        cls._req_fields = req_fields

    @classmethod
    def _set_opt_fields(cls, opt_fields):
        cls._opt_fields = opt_fields



class NameBase(object):
    """
    All named entities should inherit this class. Every class that inherits this
    class must have a class variable "_id_map = {}" defined. This helps to give
    each class a reverse lookup of name to class mapping.
    """

    def __init__(self, name, name_id=None, is_template=False, desc=None):
        prefix = self.__class__.__name__+"." if is_template else ""
        name_id = name_id or self.toid(name)
        self._id = prefix+name_id
        self._name = name
        if self._id_map.has_key(self._id):
            raise ValueError("Duplicate id "+self._id)
        else:
            self._id_map[self._id] = self
        self._desc = desc or name

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

    @property
    def description(self):
        return self._desc


class CheckedDataFieldGetter(object):

    def __init__(self, data, conventions=None):
        from .fields import FieldList as fl
        self._instance_id = data[fl.TEMPLATE.id],
        self._conventions = {} if conventions is None else conventions
        self._data = data
        # self._global_conventions =

    def get(self, field, default_value=None):
        return self._data.get(field.id, self._conventions.get(field.id, default_value))


class AssetName(NameBase):
    _id_map = {}

    def __init__(self, asset_name, desc=None):
        super(AssetName, self).__init__(asset_name, desc=desc)


class SecurityType(NameBase):
    _id_map = {}

    def __init__(self, security_type, desc=None):
        super(SecurityType, self).__init__(security_type, desc=desc)


class SecuritySubType(NameBase):
    _id_map = {}

    def __init__(self, security_subtype, desc=None):
        super(SecuritySubType, self).__init__(security_subtype, desc=desc)


class Instrument(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" % (security_type.id, security_subtype.id, self.toid(instrument_name))
        super(Instrument, self).__init__(instrument_name, name_id=inst_id, is_template=True)
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


class Collection(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, name):
        super(Collection, self).__init__(name, is_template=True)
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


class Field(NameBase):
    _id_map = {}

    def __init__(self, name, desc, data_type):
        super(Field, self).__init__(name, desc=desc)
        self._data_type = data_type

    def data_type(self):
        return self._data_type


class Asset(object):
    FIXED_INCOME = AssetName("FI", "Fixed Income")
    EQUITY = AssetName("EQ", "Equity")


class SecurityTypeList(object):
    GOVERNMENT = SecurityType("Govt", "Government")
    CORPORATE = SecurityType("Corp", "Corporate")


class SecuritySubTypeList(object):
    BOND = SecuritySubType("Bond")
    ZCB = SecuritySubType("ZCB")  # Zero coupon bond


class CategoryName(NameBase):
    _id_map = {}

    def __init__(self, name, desc=None):
        super(CategoryName, self).__init__(name, desc=desc)


class TermStructure(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, name, category):
        name_id = "%s.%s" % (category.id, self.toid(name))
        super(TermStructure, self).__init__(name, name_id=name_id, is_template=True)
        TemplateBase.__init__(self)


class Category(object):

    # termstructure categorization
    CREDIT = CategoryName("Credit")
    INFLATION = CategoryName("Inflation")
    VOLATILITY = CategoryName("Volatility")
    YIELD = CategoryName("Yield")

    # Asset names
    FIXED_INCOME = CategoryName("FI", "Fixed Income")
    EQUITY = CategoryName("EQ", "Equity")

    # Security types
    GOVERNMENT = CategoryName("Govt", "Government")
    CORPORATE = CategoryName("Corp", "Corporate")

    # Security subtype
    BOND = CategoryName("Bond")
    ZCB = CategoryName("ZCB", "Zero Coupon Bond")

