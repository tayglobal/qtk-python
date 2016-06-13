from .common import Name, Instance


class AssetName(Name):
    _id_map = {}

    def __init__(self, asset_name):
        asset_id = self.toid(asset_name)
        super(AssetName, self).__init__(asset_name, asset_id)


class SecurityTypeName(Name):
    _id_map = {}

    def __init__(self, security_type):
        type_id = self.toid(security_type)
        super(SecurityTypeName, self).__init__(security_type, type_id)


class SecuritySubTypeName(Name):
    _id_map = {}

    def __init__(self, security_subtype):
        type_id = self.toid(security_subtype)
        super(SecuritySubTypeName, self).__init__(security_subtype, type_id)


class InstrumentName(Name, Instance):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" %(security_type.id, security_subtype.id, self.toid(instrument_name))
        super(InstrumentName, self).__init__(instrument_name, inst_id, True)
        Instance.__init__(self, "Instrument")

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


class SecurityType(object):
    GOVERNMENT = SecurityTypeName("Government")
    CORPORATE = SecurityTypeName("Corporate")


class SecuritySubType(object):
    BOND = SecuritySubTypeName("Bond")
    ZCB = SecuritySubTypeName("ZCB")  # Zero coupon bond


class Instrument(object):
    US_TBILL = InstrumentName("US Treasury Bill", Asset.FIXED_INCOME, SecurityType.GOVERNMENT, SecuritySubType.ZCB)
    US_TNOTE = InstrumentName("US Treasury Note", Asset.FIXED_INCOME, SecurityType.GOVERNMENT, SecuritySubType.BOND)
    US_TBOND = InstrumentName("US Treasury Bond", Asset.FIXED_INCOME, SecurityType.GOVERNMENT, SecuritySubType.BOND)


