from blpapi.exception import NotFoundException

from qtk.fields import Field as fl
from qtk.fields import DataType as dt
from qtk.instruments import Instrument as inst

__field_list_pair = [
    ("BPIPE_REFERENCE_SECURITY_CLASS", fl.ASSET_CLASS),
    ("CPN", fl.COUPON),
    ("CPN_FREQ", fl.COUPON_FREQ),
    ("DAY_CNT_DES", fl.DAYCOUNT),
    ("ISSUE_DT", fl.ISSUE_DATE),
    ("MATURITY", fl.MATURITY_DATE),
    ("PX_LAST", fl.PRICE_LAST),
    ("SECURITY_TYP", fl.SECURITY_TYPE),
    ("SECURITY_TYP2", fl.SECURITY_SUBTYPE)
]

__bbg_to_std = {}
__std_to_bbg = {}

for bbg, std in __field_list_pair:
    __bbg_to_std[bbg] = std
    __std_to_bbg[std] = bbg


def bbg_to_std(key):
    return __bbg_to_std[key]


def std_to_bbg(key):
    return __std_to_bbg[key]


def fmt(e, f):
    key = bbg_to_std(f)

    def _to_int(ele, field):
        return ele.getElementAsInteger(field)

    def _to_str(ele, field):

        return ele.getElementAsString(field)

    def _to_float(ele, field):
        return ele.getElementAsFloat(field)

    def _to_day_count(ele, field):
        return ele.getElementAsString(field)

    def _to_date(ele, field):
        return ele.getElementAsString(field)

    def _to_freq(ele, field):
        return ele.getElementAsInteger(field)

    _format_map = {
        dt.STRING: _to_str,
        dt.INT: _to_int,
        dt.FLOAT: _to_float,
        dt.DATE: _to_date,
        dt.DAYCOUNT: _to_day_count,
        dt.FREQUENCY: _to_freq,
    }

    converter = _format_map[key.data_type()]
    try:
        val = converter(e, f)
    except NotFoundException as e:
        val = None

    return key, val


def instrument_mapper(asset_type, security_type, security_subtype):
    pass