from qtk.fields import Field as fl
import QuantLib as ql
from qtk.common import CheckedDataFieldGetter
from qtk.common import Instrument, SecuritySubTypeList
from .common import CreatorBase
from qtk.templates import Template


class ScheduleCreator(object):

    @staticmethod
    def create(data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)

        maturity_date = dfg.get(fl.MATURITY_DATE)
        issue_date = dfg.get(fl.ISSUE_DATE)
        #asof_date = asof_date
        coupon_freq = dfg.get(fl.COUPON_FREQ)
        period = ql.Period(coupon_freq)
        calendar = dfg.get(fl.CALENDAR, ql.UnitedStates())
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        termination_convention = dfg.get(fl.DAY_CONVENTION_TERMINATION, convention)
        end_of_month = dfg.get(fl.END_OF_MONTH, True)

        schedule = ql.Schedule(issue_date,
                               maturity_date,
                               period,
                               calendar,
                               convention,
                               termination_convention,
                               ql.DateGeneration.Backward,
                               end_of_month)
        return schedule


class DepositRateHelperCreator(CreatorBase):
    _templates = [Template.CRV_INST_GOVT_ZCB]
    _req_fields = [fl.ISSUE_DATE, fl.MATURITY_DATE, fl.COUPON, fl.PRICE]
    _opt_fields = []

    @classmethod
    def _create(cls, data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)
        rate = dfg.get(fl.PRICE)
        maturity_date = dfg.get(fl.MATURITY_DATE)

        settlement_days = dfg.get(fl.SETTLEMENT_DAYS, 2)
        day_count = dfg.get(fl.DAYCOUNT)
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        calendar = dfg.get(fl.CALENDAR, ql.UnitedStates())
        days = day_count.dayCount(asof_date, maturity_date)
        tenor = ql.Period(days, ql.Days)
        end_of_month = dfg.get(fl.END_OF_MONTH, True)

        depo_rate_helper = ql.DepositRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(rate/100.0)),
            tenor,
            settlement_days,
            calendar,
            convention,
            end_of_month,
            day_count
        )
        return depo_rate_helper


class BondRateHelperCreator(CreatorBase):
    _templates = [Template.CRV_INST_GOVT_BOND]
    _req_fields = [fl.ISSUE_DATE, fl.MATURITY_DATE, fl.COUPON, fl.COUPON_FREQ, fl.PRICE]
    _opt_fields = []


    @staticmethod
    def _create(data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)
        schedule = ScheduleCreator.create(data, asof_date, convention)
        face_amount = dfg.get(fl.FACE_AMOUNT, 100.0)
        settlement_days = dfg.get(fl.SETTLEMENT_DAYS, 2)
        day_count = dfg.get(fl.DAYCOUNT)
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        price = dfg.get(fl.PRICE)
        coupon = dfg.get(fl.COUPON)
        bond_helper = ql.FixedRateBondHelper(
            ql.QuoteHandle(ql.SimpleQuote(price)),
            settlement_days,
            face_amount,
            schedule,
            [coupon/100.0],
            day_count,
            convention
        )
        return bond_helper


class BondYieldCurveCreator(CreatorBase):

    _templates = [Template.TS_YIELD_BOND]
    _req_fields = [fl.INSTRUMENT_COLLECTION, fl.ASOF_DATE, ]
    _opt_fields = []


    def _create(self, data, asof_date, conventions=None):
        curve_members = data[fl.INSTRUMENT_COLLECTION.id]
        conventions = data.get(fl.CONVENTIONS.id, conventions)
        rate_helpers = []
        for c in curve_members:
            loc_conventions = conventions or c.get(fl.CONVENTIONS.id)
            dfg = CheckedDataFieldGetter(c, loc_conventions)
            instance = dfg.get(fl.TEMPLATE)
            loc_asof_date = dfg.get(fl.ASOF_DATE, asof_date)

            if isinstance(instance, Instrument) and (instance.security_subtype == SecuritySubTypeList.ZCB):
                depo_rate_helper = DepositRateHelperCreator(c).create(loc_asof_date, conventions)
                rate_helpers.append(depo_rate_helper)
            elif isinstance(instance, Instrument) and (instance.security_subtype == SecuritySubTypeList.BOND):
                bond_rate_helper = BondRateHelperCreator(c).create(loc_asof_date, conventions)
                rate_helpers.append(bond_rate_helper)

        day_count = ql.Actual360()

        yc_curve = ql.PiecewiseLinearZero(
            asof_date,
            rate_helpers,
            day_count
        )

        return yc_curve
