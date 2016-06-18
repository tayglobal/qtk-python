from qtk.common import Instrument, SecurityTypeList, SecuritySubTypeList, Collection, Asset, TermStructure, Category


class Template(object):
    INST_GOVT_ZCB = Instrument("", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                               SecuritySubTypeList.ZCB)
    INST_GOVT_BOND = Instrument("", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                                SecuritySubTypeList.BOND)

    CRV_INST_GOVT_ZCB = Instrument("Curve Instrument", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                               SecuritySubTypeList.ZCB)
    CRV_INST_GOVT_BOND = Instrument("Curve Instrument", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                                SecuritySubTypeList.BOND)

    COLN_INSTRUMENTS = Collection("Instrument Collection")

    TS_YIELD_BOND = TermStructure("Bond Curve", Category.YIELD)
