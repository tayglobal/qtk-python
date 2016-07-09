from qtk.templates import Template as T
from qtk.fields import Field as F
import QuantLib as ql

# http://help.derivativepricing.com/1571.htm
# USD
_govt_bonds = dict.fromkeys([
    "USD."+T.INST_GOVT_BOND.id,
    "USD."+T.CRV_INST_GOVT_BOND.id
], {
    F.COUPON_FREQ: ql.Period(6, ql.Months),
    F.ACCRUAL_BASIS: ql.ActualActual(ql.ActualActual.Bond),
    F.END_OF_MONTH: True,
    F.COMPOUNDING: ql.Compounded,
    F.SETTLEMENT_DAYS: 1,
    F.PAYMENT_CALENDAR: ql.UnitedStates(),
    F.PAYMENT_DAY_CONVENTION: ql.Following,
    F.SETTLEMENT_CALENDAR: ql.UnitedStates(),
    F.ROUNDING: ql.ClosestRounding(12)
})


