from qtk import Controller, Field as F, Template as T
import pprint

# replicates http://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html
data = [
    {
        F.LIST_OF_DATES.id: ["1/15/2015", "7/15/2015", "1/15/2016"],
        F.LIST_OF_ZERO_RATES.id: [0.0, 0.005, 0.007],
        F.DISCOUNT_BASIS.id: "30/360",
        F.DISCOUNT_CALENDAR.id: "UnitedStates",
        F.COMPOUNDING.id: "Compounded",
        F.COMPOUNDING_FREQ.id: "Annual",
        F.CURRENCY.id: "USD",
        F.TEMPLATE.id: T.TS_YIELD_ZERO,
        F.OBJECT_ID.id: "USD.Zero.Curve"},
    {
        F.OBJECT_ID.id: "BondEngine",
        F.DISCOUNT_CURVE.id: "->USD.Zero.Curve",
        F.TEMPLATE.id: T.ENG_BOND_DISCOUNTING.id},
    {
        F.ASOF_DATE.id: '2016-01-15',
        F.COUPON.id: 0.06,
        F.COUPON_FREQ.id: "Semiannual",
        F.CURRENCY.id: 'USD',
        F.PAYMENT_BASIS.id: '30/360',
        F.ISSUE_DATE.id: '2015-01-15',
        F.MATURITY_DATE.id: '2016-01-15',
        F.ACCRUAL_CALENDAR.id: "UnitedStates",
        F.ACCRUAL_DAY_CONVENTION.id: "Unadjusted",
        F.DATE_GENERATION.id: "Backward",
        F.END_OF_MONTH.id: False,
        F.OBJECT_ID.id: "USD.TBond",
        F.PRICING_ENGINE.id: "->BondEngine",
        F.TEMPLATE.id: T.INST_BOND_TBOND.id}
]

res = Controller(data)
asof_date = "1/15/2015"

ret = res.process(asof_date)
tbond = res.object("USD.TBond")
print tbond.NPV()
