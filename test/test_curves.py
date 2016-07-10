import QuantLib as ql
from unittest import TestCase
from qtk import Controller, Field, QuantLibConverter as qlc
import copy

_bond_sample_data = {
    'AsOfDate': '2016-06-14',
    'Country': 'US',
    'Currency': 'USD',
    'DataSource': 'TEST',
    'InstrumentCollection': [{'AsOfDate': '2016-06-14',
                              'Coupon': '0.000000',
                              'CouponFrequency': None,
                              'Currency': 'USD',
                              'AccrualBasis': 'ACT/360',
                              'IssueDate': '2016-01-07',
                              'MaturityDate': '2016-07-07',
                              'Yield': '0.212500',
                              'SecurityId': '912796HZ Govt',
                              'Template': 'Instrument.Govt.Zcb.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '0.000000',
                              'CouponFrequency': None,
                              'Currency': 'USD',
                              'AccrualBasis': 'ACT/360',
                              'IssueDate': '2015-09-17',
                              'MaturityDate': '2016-09-15',
                              'Yield': '0.262500',
                              'SecurityId': '912796HE Govt',
                              'Template': 'Instrument.Govt.Zcb.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '0.000000',
                              'CouponFrequency': None,
                              'Currency': 'USD',
                              'AccrualBasis': 'ACT/360',
                              'IssueDate': '2016-06-16',
                              'MaturityDate': '2016-12-15',
                              'Yield': '0.392500',
                              'SecurityId': '912796JY Govt',
                              'Template': 'Instrument.Govt.Zcb.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '0.000000',
                              'CouponFrequency': None,
                              'Currency': 'USD',
                              'AccrualBasis': 'ACT/360',
                              'IssueDate': '2016-05-26',
                              'MaturityDate': '2017-05-25',
                              'Yield': '0.530000',
                              'SecurityId': '912796JT Govt',
                              'Template': 'Instrument.Govt.Zcb.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '0.875000',
                              'Currency': 'USD',
                              'IssueDate': '2016-05-31',
                              'MaturityDate': '2018-05-31',
                              'Price': '100.292969',
                              'SecurityId': '912828R5 Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '0.875000',
                              'Currency': 'USD',
                              'IssueDate': '2016-06-15',
                              'MaturityDate': '2019-06-15',
                              'Price': '100.066406',
                              'SecurityId': '912828R8 Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '1.375000',
                              'Currency': 'USD',
                              'IssueDate': '2016-05-31',
                              'MaturityDate': '2021-05-31',
                              'Price': '101.136719',
                              'SecurityId': '912828R7 Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '1.625000',
                              'Currency': 'USD',
                              'IssueDate': '2016-05-31',
                              'MaturityDate': '2023-05-31',
                              'Price': '101.382813',
                              'SecurityId': '912828R6 Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '1.625000',
                              'Currency': 'USD',
                              'IssueDate': '2016-05-16',
                              'MaturityDate': '2026-05-15',
                              'Price': '100.101563',
                              'SecurityId': '912828R3 Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'},
                             {'AsOfDate': '2016-06-14',
                              'Coupon': '2.500000',
                              'Currency': 'USD',
                              'IssueDate': '2016-05-16',
                              'MaturityDate': '2046-05-15',
                              'Price': '101.617188',
                              'SecurityId': '912810RS Govt',
                              'Template': 'Instrument.Govt.Bond.CurveMember'}],
    'Template': 'TermStructure.Yield.BondCurve'
}


class TestCurves(TestCase):

    def setUp(self):
        self._bond_data = copy.deepcopy(_bond_sample_data)

    def test_us_bond_curve(self):
        res = Controller([self._bond_data])
        asof_date = qlc.to_date(self._bond_data[Field.ASOF_DATE.id])

        res.process(asof_date)
        curve = self._bond_data[Field.OBJECT.id]
        self.assertIsInstance(curve, ql.YieldTermStructure)

        tenors = [0, 12, 60, 90, 120]
        vals = [1.0, 0.995463027383, 0.944034654878, 0.895839444646, 0.848938836737]
        calendar = ql.UnitedStates()
        for t,v in zip(tenors, vals):
            p = ql.Period(t, ql.Months)
            d = calendar.advance(asof_date, ql.Period(t, ql.Months))
            o = curve.discount(d)
            self.assertAlmostEqual(o, v, 10, msg="("+str(t)+","+str(d)+","+str(o)+","+str(v)+")")