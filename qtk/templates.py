from qtk.common import Instrument, SecurityTypeList, SecuritySubTypeList, Collection, Asset, TermStructure, Category


class Template(object):
    INST_GOVT_ZCB = Instrument("Government ZCB", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                               SecuritySubTypeList.ZCB)
    INST_GOVT_BOND = Instrument("Government Bond", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                                SecuritySubTypeList.BOND)

    CRV_INST_GOVT_ZCB = Instrument("Curve Instrument Government ZCB", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                               SecuritySubTypeList.ZCB)
    CRV_INST_GOVT_BOND = Instrument("Curve Instrument Government Bond", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT,
                                SecuritySubTypeList.BOND)

    COLN_INSTRUMENTS = Collection("Instrument Collection")

    TS_YIELD_BOND = TermStructure("Bond Curve", Category.YIELD)
