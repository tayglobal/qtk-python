from qtk.common import TemplateBase, NameBase, Category
from qtk.fields import Field as F


class GenericTemplate(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, name,  prefix, category=None, convention_keys=(F.CURRENCY,)):
        name_id = "%s.%s" % (category.id, self.toid(name)) if category else self.toid(name)
        super(GenericTemplate, self).__init__(name, name_id=name_id, prefix=prefix)
        TemplateBase.__init__(self, prefix, convention_keys)


class Instrument(NameBase, TemplateBase):
    _id_map = {}

    def __init__(self, instrument_name, asset_type, security_type, security_subtype,
                 convention_keys=(F.CURRENCY,)):
        self._asset_type = asset_type
        self._security_type = security_type
        self._security_subtype = security_subtype
        inst_id = "%s.%s.%s" % (security_type.id, security_subtype.id, self.toid(instrument_name))
        prefix = self.__class__.__name__
        super(Instrument, self).__init__(instrument_name, name_id=inst_id, prefix=prefix)
        TemplateBase.__init__(self, prefix, convention_keys)

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def security_type(self):
        return self._security_type

    @property
    def security_subtype(self):
        return self._security_subtype


class Template(object):
    INST_GOVT_ZCB = Instrument("", Category.FIXED_INCOME, Category.GOVERNMENT, Category.ZCB)
    INST_GOVT_BOND = Instrument("", Category.FIXED_INCOME, Category.GOVERNMENT, Category.BOND)

    CRV_INST_GOVT_ZCB = Instrument("Curve Member", Category.FIXED_INCOME, Category.GOVERNMENT, Category.ZCB)
    CRV_INST_GOVT_BOND = Instrument("Curve Member",Category.FIXED_INCOME, Category.GOVERNMENT, Category.BOND)

    TS_YIELD_BOND = GenericTemplate("Bond Curve", prefix=Category.TERM_STRUCTURE.id,
                                    category=Category.YIELD)
    SCHEDULE = GenericTemplate("Schedule", prefix=Category.TIME.id, category=None)

