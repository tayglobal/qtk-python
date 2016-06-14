from .common import Name, Instance


class AssetName(Name):
    _id_map = {}

    def __init__(self, asset_name):
        asset_id = self.toid(asset_name)
        super(AssetName, self).__init__(asset_name, asset_id)


class SecurityType(Name):
    _id_map = {}

    def __init__(self, security_type):
        type_id = self.toid(security_type)
        super(SecurityType, self).__init__(security_type, type_id)


class SecuritySubType(Name):
    _id_map = {}

    def __init__(self, security_subtype):
        type_id = self.toid(security_subtype)
        super(SecuritySubType, self).__init__(security_subtype, type_id)


class Instrument(Name, Instance):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" %(security_type.id, security_subtype.id, self.toid(instrument_name))
        super(Instrument, self).__init__(instrument_name, inst_id, True)
        Instance.__init__(self)

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def security_type(self):
        return self._security_type

    @property
    def security_subtype(self):
        return self._security_subtype


class Asset(object):
    FIXED_INCOME = AssetName("Fixed Income")
    EQUITY = AssetName("Equity")


class SecurityTypeList(object):
    GOVERNMENT = SecurityType("Government")
    CORPORATE = SecurityType("Corporate")


class SecuritySubTypeList(object):
    BOND = SecuritySubType("Bond")
    ZCB = SecuritySubType("ZCB")  # Zero coupon bond


class InstrumentList(object):
    US_TBILL = Instrument("US Treasury Bill", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.ZCB)
    US_TNOTE = Instrument("US Treasury Note", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)
    US_TBOND = Instrument("US Treasury Bond", Asset.FIXED_INCOME, SecurityTypeList.GOVERNMENT, SecuritySubTypeList.BOND)


