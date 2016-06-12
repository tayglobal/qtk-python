

INT_TYPE = 1
FLOAT_TYPE = 2
STR_TYPE = 3
DATE_TYPE = 4
FREQ_TYPE = 5
DAY_COUNT_TYPE = 6
LIST_TYPE = 20
DICT_TYPE = 21


class FieldName(object):
    __field_map = {}

    def __init__(self, name, desc, data_type):
        self._name = name
        self._desc = desc
        self._id = self.toid(name)
        self.__class__.__field_map[self._id] = self
        self._data_type = data_type

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._desc

    def data_type(self):
        return self._data_type

    @staticmethod
    def toid(name):
        return ''.join(x for x in name.title() if not x.isspace())

    @classmethod
    def lookup(cls, id):
        return cls.__field_map[id]


# In alphabetical order
ASSET_CLASS = FieldName("Asset Class", "Asset class of a security", STR_TYPE)

COUPON = FieldName("Coupon", "Coupon of a bond in % units", FLOAT_TYPE)
COUPON_FREQ = FieldName("Coupon Frequency", "Coupon frequency of a bond", FREQ_TYPE)
CURVE_MEMBERS = FieldName("Curve Members","Members constituting and index or curve", LIST_TYPE)

DATA_SOURCE = FieldName("Data Source", "Data vendor source", STR_TYPE)
DAY_COUNT = FieldName("Day Count", "Day count of a security", DAY_COUNT_TYPE)

ISSUE_DATE = FieldName("Issue Date", "Date of issuance of a security", DATE_TYPE)

MATURITY_DATE = FieldName("Maturity Date", "Maturity date of a security", DATE_TYPE)

PRICE_LAST = FieldName("Price Last", "Last price of a security", FLOAT_TYPE)

SECURITY_DATA = FieldName("Security Data", "Security refernce data", DICT_TYPE)
SECURITY_ID = FieldName("Security Id", "Security identifier", STR_TYPE)
SECURITY_TYPE = FieldName("Security Type", "Security Type", STR_TYPE)
SECURITY_SUBTYPE = FieldName("Security Subtype", "Security Subtype", STR_TYPE)

TICKER = FieldName("Ticker", "Ticker identifier for a security", STR_TYPE)
