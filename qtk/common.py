import QuantLib as ql
from .converters import QuantLibConverter as qlf


class TemplateBase(object):
    _inst_map = {}
    _creator = None

    def __init__(self, prefix):
        self._instance_name = prefix
        self._iid = NameBase.toid(prefix)
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
    def lookup_template(cls, field_id):
        c_name = field_id.split(".")[0]
        c = cls._inst_map[c_name]
        return getattr(c, "lookup")(field_id)

    @classmethod
    def get_creator(cls):
        return cls._creator

    @classmethod
    def _set_creator(cls, creator):
        cls._creator = creator



class NameBase(object):
    """
    All named entities should inherit this class. Every class that inherits this
    class must have a class variable "_id_map = {}" defined. This helps to give
    each class a reverse lookup of name to class mapping.
    """

    def __init__(self, name, name_id=None, prefix="", desc=None):
        prefix += "." if len(prefix) else ""
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
        from .fields import Field as fl
        self._instance_id = data[fl.TEMPLATE.id],
        self._conventions = {} if conventions is None else conventions
        self._data = data
        # self._global_conventions =

    def get(self, field, default_value=None):
        return self._data.get(field.id, self._conventions.get(field.id, default_value))


class Instrument(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" % (security_type.id, security_subtype.id, self.toid(instrument_name))
        prefix = self.__class__.__name__
        super(Instrument, self).__init__(instrument_name, name_id=inst_id, prefix=prefix)
        TemplateBase.__init__(self, prefix)

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def security_type(self):
        return self._security_type

    @property
    def security_subtype(self):
        return self._security_subtype


class TypeName(NameBase):
    _id_map = {}

    def __init__(self, name, type, converter):
        super(TypeName, self).__init__(name)
        self._type = type
        self._converter = converter

    @property
    def type(self):
        return self._type

    def convert(self, value):
        return self._converter(value)


class DataType(object):
    TEMPLATE = TypeName("Template", TemplateBase, qlf.to_template)
    INT = TypeName("Integer", int, int)
    FLOAT = TypeName("Float", float, float)
    STRING = TypeName("String", str, str)
    BOOL = TypeName("Boolean", bool, bool)
    LIST = TypeName("List", list, list)
    DICT = TypeName("Dictionary", dict, dict)
    OBJECT = TypeName("Object", object, lambda x: x)

    DATE = TypeName("Date", ql.Date, qlf.to_date)
    FREQUENCY = TypeName("Frequency", int, qlf.to_frequency)  # this is enum for frequency
    DAYCOUNT = TypeName("Day Count", ql.DayCounter, qlf.to_daycount)
    DAY_CONVENTION = TypeName("Day Convention", int, qlf.to_day_convention)  # this is enum for day convention
    CALENDAR = TypeName("Calendar", ql.Calendar, qlf.to_calendar)


class FieldName(NameBase):
    _id_map = {}

    def __init__(self, name, desc, data_type):
        super(FieldName, self).__init__(name, desc=desc)
        self._data_type = data_type

    @property
    def data_type(self):
        return self._data_type

    def check_type(self, value):
        return isinstance(value, self._data_type.type)


class CategoryName(NameBase):
    _id_map = {}

    def __init__(self, name, desc=None):
        super(CategoryName, self).__init__(name, desc=desc)


class Category(object):

    # termstructure categorization
    TERM_STRUCTURE = CategoryName("Term Structure")  # Term structure categorization
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

    # Other category headings
    TIME = CategoryName("Time", "Time module")


class GenericTemplate(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, name,  prefix, category=None):
        name_id = "%s.%s" % (category.id, self.toid(name)) if category else self.toid(name)
        super(GenericTemplate, self).__init__(name, name_id=name_id, prefix=prefix)
        TemplateBase.__init__(self, prefix)
