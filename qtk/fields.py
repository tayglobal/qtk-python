from qtk.common import Name


class DataType(object):
    INSTANCE = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    DATE = 4
    FREQUENCY = 5
    DAYCOUNT = 6
    DAY_CONVENTION = 7
    LIST = 20
    DICT = 21


class FieldName(Name):
    _id_map = {}

    def __init__(self, name, desc, data_type):
        field_id = self.toid(name)
        super(FieldName, self).__init__(name, field_id)
        self._desc = desc
        self._data_type = data_type

    @property
    def description(self):
        return self._desc

    def data_type(self):
        return self._data_type


class Field(object):
    # In alphabetical order
    ASOF_DATE = FieldName("As Of Date", "Reference date or as of date", DataType.DATE)
    ASSET_CLASS = FieldName("Asset Class", "Asset class of a security", DataType.STRING)
    DAY_CONVENTION = FieldName("Day Convention", "Bussiness day convention", DataType.DAY_CONVENTION)
    COUPON = FieldName("Coupon", "Coupon of a bond in % units", DataType.FLOAT)
    COUPON_FREQ = FieldName("Coupon Frequency", "Coupon frequency of a bond", DataType.FREQUENCY)
    CURRENCY = FieldName("Currency", "Currency", DataType.STRING)
    CURVE_MEMBERS = FieldName("Curve Members","Members constituting and index or curve", DataType.LIST)
    DATA_SOURCE = FieldName("Data Source", "Data vendor source", DataType.STRING)
    DAYCOUNT = FieldName("Day Count", "Day count of a security", DataType.DAYCOUNT)
    FIXING_DAYS = FieldName("Fixing Days", "Fixing days", DataType.INT)
    ISSUE_DATE = FieldName("Issue Date", "Date of issuance of a security", DataType.DATE)
    INSTANCE = FieldName("Instance", "Dictionary instance", DataType.INSTANCE)
    MATURITY_DATE = FieldName("Maturity Date", "Maturity date of a security", DataType.DATE)
    PRICE_LAST = FieldName("Price Last", "Last price of a security", DataType.FLOAT)
    SECURITY_DATA = FieldName("Security Data", "Security refernce data", DataType.DICT)
    SECURITY_ID = FieldName("Security Id", "Security identifier", DataType.STRING)
    SECURITY_TYPE = FieldName("Security Type", "Security Type", DataType.STRING)
    SECURITY_SUBTYPE = FieldName("Security Subtype", "Security Subtype", DataType.STRING)
    TICKER = FieldName("Ticker", "Ticker identifier for a security", DataType.STRING)
