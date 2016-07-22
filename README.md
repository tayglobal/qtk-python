# Quant Python ToolKit

This package is intended to be a layer above QuantLib Python and a few other quantitative libraries 
to be more accessible for quantitative finance calculations.

## Minimal Example
Here is a minimal example for valuing a bond using a provided zero rates.

    from qtk import Controller, Field as F, Template as T

    data = [{
              'Compounding': 'Compounded',
              'CompoundingFrequency': 'Annual',
              'Currency': 'USD',
              'DiscountBasis': '30/360',
              'DiscountCalendar': 'UnitedStates',
              'ListOfDate': ['1/15/2015', '7/15/2015', '1/15/2016'],
              'ListOfZeroRate': [0.0, 0.005, 0.007],
              'ObjectId': 'USD.Zero.Curve',
              'Template': 'TermStructure.Yield.ZeroCurve'},
             {
              'DiscountCurve': '->USD.Zero.Curve',
              'ObjectId': 'BondEngine',
              'Template': 'Engine.Bond.Discounting'},
             {
              'AccrualCalendar': 'UnitedStates',
              'AccrualDayConvention': 'Unadjusted',
              'AsOfDate': '2016-01-15',
              'Coupon': 0.06,
              'CouponFrequency': 'Semiannual',
              'Currency': 'USD',
              'DateGeneration': 'Backward',
              'EndOfMonth': False,
              'IssueDate': '2015-01-15',
              'MaturityDate': '2016-01-15',
              'ObjectId': 'USD.TBond',
              'PaymentBasis': '30/360',
              'PricingEngine': '->BondEngine',
              'Template': 'Instrument.Bond.TreasuryBond'}]

    res = Controller(data)
    asof_date = "1/15/2015"

    ret = res.process(asof_date)
    tbond = res.object("USD.TBond")
    print tbond.NPV()


The basic idea here is that once you have the data prepared, the `Controller` can be invoked to do the calculations. 
A few points that are worth noting here. 

- All the data is textual and rather intuitive. For instance, the coupon
  frequency is just stated as `Annual` or `Semiannual`. The same is true for a lot of other fields. For dates,
  the `dateutil` package is used to parse and covers a wide variety of formats. 

- The `data` is essentially a `list` of `dict` with each `dict` corresponding to a specific `object` as determined
  by the value to the key `Template` in each `dict`. Each `object` here has a name as specified by the value of the 
  key `ObjectId`
  
- One of the values can refer to another object described by a `dict` by using the `reference` syntax. For instance,
  the first `dict` in the `data` list (with `ObjectId` given as *USD.Zero.Curve* ) variable refers to an interest 
  rate term structure of zero rates. The next object is a discounting bond engine, and require an yield curve as 
  input for the discount curve. Here the yield curve is refered by using the prefix `->` along with the name of the
  object we are referring to.
  
- Here, the `Controller` parses the data, and figures out the dependency and processes the object in the correct order
  and fulfills the dependencies behind the scenes. 
  
  
## Installation

You can install qtk using `pip` or `easy_install`

    pip install qtk
    
or

    easy_install qtk
    
`qtk` has a dependency on `QuantLib-Python` which needs to be installed as well.


  