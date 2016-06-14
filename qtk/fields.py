from qtk.common import Name


class DataType(object):
    INSTANCE = 0
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


class FieldList(object):
    # In alphabetical order
    ASOF_DATE = Field("As Of Date", "Reference date or as of date", DataType.DATE)
    ASSET_CLASS = Field("Asset Class", "Asset class of a security", DataType.STRING)
    CALENDAR = Field("Calendar", "Calendar", DataType.CALENDAR)
    CONVENTIONS = Field("Conventions", "Conventions for instruments, models or indices", DataType.DICT)
    COUPON = Field("Coupon", "Coupon of a bond in % units", DataType.FLOAT)
    COUPON_FREQ = Field("Coupon Frequency", "Coupon frequency of a bond", DataType.FREQUENCY)
    CURRENCY = Field("Currency", "Currency", DataType.STRING)
    CURVE_MEMBERS = Field("Curve Members","Members constituting and index or curve", DataType.LIST)
    DATA_SOURCE = Field("Data Source", "Data vendor source", DataType.STRING)
    DAY_CONVENTION = Field("Day Convention", "Bussiness day convention", DataType.DAY_CONVENTION)
    DAY_CONVENTION_TERMINATION = Field("Day Convention Termination",
                                           "Termination day convention", DataType.DAY_CONVENTION)
    DAYCOUNT = Field("Day Count", "Day count of a security", DataType.DAYCOUNT)
    END_OF_MONTH = Field("End Of Month", "End of month rule", DataType.BOOL)
    FACE_AMOUNT = Field("Face Amount", "Face amount", DataType.FLOAT)
    ISSUE_DATE = Field("Issue Date", "Date of issuance of a security", DataType.DATE)
    INSTANCE = Field("Instance", "Dictionary instance", DataType.INSTANCE)
    MATURITY_DATE = Field("Maturity Date", "Maturity date of a security", DataType.DATE)
    PRICE_LAST = Field("Price Last", "Last price of a security", DataType.FLOAT)
    SECURITY_DATA = Field("Security Data", "Security refernce data", DataType.DICT)
    SECURITY_ID = Field("Security Id", "Security identifier", DataType.STRING)
    SECURITY_TYPE = Field("Security Type", "Security Type", DataType.STRING)
    SECURITY_SUBTYPE = Field("Security Subtype", "Security Subtype", DataType.STRING)
    SETTLEMENT_DAYS = Field("Settlement Days", "Settlement days", DataType.INT)
    TICKER = Field("Ticker", "Ticker identifier for a security", DataType.STRING)
