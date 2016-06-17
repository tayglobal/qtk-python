from qtk.common import DataType, FieldName


class Field(object):
    # In alphabetical order
    ASOF_DATE = FieldName("As Of Date", "Reference date or as of date", DataType.DATE)
    ASSET_CLASS = FieldName("Asset Class", "Asset class of a security", DataType.STRING)
    CALENDAR = FieldName("Calendar", "Calendar", DataType.CALENDAR)
    CONVENTIONS = FieldName("Conventions", "Conventions for instruments, models or indices", DataType.DICT)
    COUPON = FieldName("Coupon", "Coupon of a bond in % units", DataType.FLOAT)
    COUPON_FREQ = FieldName("Coupon Frequency", "Coupon frequency of a bond", DataType.FREQUENCY)
    CURRENCY = FieldName("Currency", "Currency", DataType.STRING)
    INSTRUMENT_COLLECTION = FieldName("Instrument Collection", "Collection of instruments", DataType.LIST)
    DATA_SOURCE = FieldName("Data Source", "Data vendor source", DataType.STRING)
    DAY_CONVENTION = FieldName("Day Convention", "Bussiness day convention", DataType.DAY_CONVENTION)
    DAY_CONVENTION_TERMINATION = FieldName("Day Convention Termination",
                                           "Termination day convention", DataType.DAY_CONVENTION)
    DAYCOUNT = FieldName("Day Count", "Day count of a security", DataType.DAYCOUNT)
    END_OF_MONTH = FieldName("End Of Month", "End of month rule", DataType.BOOL)
    FACE_AMOUNT = FieldName("Face Amount", "Face amount", DataType.FLOAT)
    ISSUE_DATE = FieldName("Issue Date", "Date of issuance of a security", DataType.DATE)

    MATURITY_DATE = FieldName("Maturity Date", "Maturity date of a security", DataType.DATE)
    OBJECT = FieldName("Object", "Instantiation of a QuantLib class", DataType.OBJECT)
    OBJECT_ID = FieldName("Object Id", "ID of a QuantLib object", DataType.STRING)
    PRICE_LAST = FieldName("Price Last", "Last price of a security", DataType.FLOAT)
    PRICE = FieldName("Price", "Price of a security", DataType.FLOAT)
    SECURITY_DATA = FieldName("Security Data", "Security refernce data", DataType.DICT)
    SECURITY_ID = FieldName("Security Id", "Security identifier", DataType.STRING)
    SECURITY_TYPE = FieldName("Security Type", "Security Type", DataType.STRING)
    SECURITY_SUBTYPE = FieldName("Security Subtype", "Security Subtype", DataType.STRING)
    SETTLEMENT_DAYS = FieldName("Settlement Days", "Settlement days", DataType.INT)
    TEMPLATE = FieldName("Template", "Instantiation template", DataType.TEMPLATE)
    TICKER = FieldName("Ticker", "Ticker identifier for a security", DataType.STRING)
