from qtk.common import Instrument,GenericTemplate, Category


class Template(object):
    INST_GOVT_ZCB = Instrument("", Category.FIXED_INCOME, Category.GOVERNMENT, Category.ZCB)
    INST_GOVT_BOND = Instrument("", Category.FIXED_INCOME, Category.GOVERNMENT, Category.BOND)

    CRV_INST_GOVT_ZCB = Instrument("Curve Member", Category.FIXED_INCOME, Category.GOVERNMENT, Category.ZCB)
    CRV_INST_GOVT_BOND = Instrument("Curve Member",Category.FIXED_INCOME, Category.GOVERNMENT, Category.BOND)

    TS_YIELD_BOND = GenericTemplate("Bond Curve", prefix=Category.TERM_STRUCTURE.id, category=Category.YIELD)
    SCHEDULE = GenericTemplate("Schedule", prefix=Category.TIME.id, category=None)

