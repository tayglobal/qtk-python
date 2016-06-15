from qtk.common import DataType, Field


class FieldList(object):
    # In alphabetical order
    ASOF_DATE = Field("As Of Date", "Reference date or as of date", DataType.DATE)
    ASSET_CLASS = Field("Asset Class", "Asset class of a security", DataType.STRING)
    CALENDAR = Field("Calendar", "Calendar", DataType.CALENDAR)
    CONVENTIONS = Field("Conventions", "Conventions for instruments, models or indices", DataType.DICT)
    COUPON = Field("Coupon", "Coupon of a bond in % units", DataType.FLOAT)
    COUPON_FREQ = Field("Coupon Frequency", "Coupon frequency of a bond", DataType.FREQUENCY)
    CURRENCY = Field("Currency", "Currency", DataType.STRING)
    INSTRUMENT_COLLECTION = Field("Instrument Collection","Instruments constituting in curve construction", DataType.LIST)
    DATA_SOURCE = Field("Data Source", "Data vendor source", DataType.STRING)
    DAY_CONVENTION = Field("Day Convention", "Bussiness day convention", DataType.DAY_CONVENTION)
    DAY_CONVENTION_TERMINATION = Field("Day Convention Termination",
                                           "Termination day convention", DataType.DAY_CONVENTION)
    DAYCOUNT = Field("Day Count", "Day count of a security", DataType.DAYCOUNT)
    END_OF_MONTH = Field("End Of Month", "End of month rule", DataType.BOOL)
    FACE_AMOUNT = Field("Face Amount", "Face amount", DataType.FLOAT)
    ISSUE_DATE = Field("Issue Date", "Date of issuance of a security", DataType.DATE)

    MATURITY_DATE = Field("Maturity Date", "Maturity date of a security", DataType.DATE)
    PRICE_LAST = Field("Price Last", "Last price of a security", DataType.FLOAT)
    PRICE_MID = Field("Price Mid", "Mid price of a security", DataType.FLOAT)
    SECURITY_DATA = Field("Security Data", "Security refernce data", DataType.DICT)
    SECURITY_ID = Field("Security Id", "Security identifier", DataType.STRING)
    SECURITY_TYPE = Field("Security Type", "Security Type", DataType.STRING)
    SECURITY_SUBTYPE = Field("Security Subtype", "Security Subtype", DataType.STRING)
    SETTLEMENT_DAYS = Field("Settlement Days", "Settlement days", DataType.INT)
    TEMPLATE = Field("Template", "Instantiation template", DataType.TEMPLATE)
    TICKER = Field("Ticker", "Ticker identifier for a security", DataType.STRING)
