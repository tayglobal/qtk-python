from qtk import Controller, Field as F, Template as T
import pprint

data = {
    F.LIST_OF_DATES.id: ["7/5/2016", "8/1/2016", "9/1/2016", "10/1/2016"],
    F.LIST_OF_ZERO_RATES.id: [1.0, 0.99, 0.98, 0.97],
    F.DISCOUNT_BASIS.id: "30/360",
    F.TEMPLATE.id: T.TS_YIELD_ZERO,
    F.CURRENCY.id: "USD",
    F.DISCOUNT_CALENDAR.id: "UnitedStates.GovernmentBond"
}

res = Controller([data])
asof_date = "7/5/2016"

ret = res.process(asof_date)
zcurve = data[F.OBJECT.id]

pprint.pprint(data)