from qtk.common import Instrument, Asset, SecurityTypeList, SecuritySubTypeList, Collection


class Template(object):
    US_TBILL = Instrument("US Treasury Bill", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.ZCB)
    US_TNOTE = Instrument("US Treasury Note", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)
    US_TBOND = Instrument("US Treasury Bond", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)

    BOOTSTRAP_INSTRUMENTS = Collection("Bootstrap Instruments")
