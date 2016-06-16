from qtk.common import Instrument, SecurityTypeList, SecuritySubTypeList, Collection, Asset, TermStructure, Category


class Template(object):
    INST_US_TBILL = Instrument("US Treasury Bill", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.ZCB)
    INST_US_TNOTE = Instrument("US Treasury Note", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)
    INST_US_TBOND = Instrument("US Treasury Bond", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)

    COLN_INSTRUMENTS = Collection("Instrument Collection")

    TS_YIELD_BOND = TermStructure("Bond Curve", Category.YIELD)
