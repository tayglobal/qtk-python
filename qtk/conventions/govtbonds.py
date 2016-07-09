from qtk.templates import Template as T
from qtk.fields import Field as F
import QuantLib as ql

# http://help.derivativepricing.com/1571.htm
# USD
_govt_bonds = dict.fromkeys([
    "USD."+T.INST_GOVT_BOND.id,
    "USD."+T.CRV_INST_GOVT_BOND.id
], {
    F.COUPON_FREQ.id: ql.Period(6, ql.Months),
    F.ACCRUAL_BASIS.id: ql.ActualActual(ql.ActualActual.Bond),
    F.END_OF_MONTH.id: True,
    F.COMPOUNDING.id: ql.Compounded,
    F.SETTLEMENT_DAYS.id: 1,
    F.PAYMENT_CALENDAR.id: ql.UnitedStates(),
    F.PAYMENT_DAY_CONVENTION.id: ql.Following,
    F.SETTLEMENT_CALENDAR.id: ql.UnitedStates(),
    F.ROUNDING.id: ql.ClosestRounding(12)
})


