from .fields import Field as fl
import QuantLib as ql
from .common import CheckedDataFieldGetter, Instance
from .instruments import InstrumentName, SecuritySubType


class ScheduleCreator(object):

    @staticmethod
    def create(data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)

        maturity_date = dfg.get(fl.MATURITY_DATE)
        coupon_freq = dfg.get(fl.COUPON_FREQ)
        calendar = dfg.get(fl.CALENDAR, ql.UnitedStates()),
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        termination_convention = dfg.get(fl.DAY_CONVENTION_TERMINATION, convention)
        end_of_month = dfg.get(fl.END_OF_MONTH, True)

        schedule = ql.Schedule(asof_date,
                               maturity_date,
                               coupon_freq,
                               calendar,
                               convention,
                               termination_convention,
                               ql.DateGeneration.Backward,
                               end_of_month)
        return schedule


class DepositRateHelperCreator(object):

    @classmethod
    def create(cls, data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)
        rate = dfg.get(fl.PRICE_LAST)
        maturity_date = dfg.get(fl.MATURITY_DATE)
        tenor = cls._to_tenor(asof_date, maturity_date)
        settlement_days = dfg.get(fl.SETTLEMENT_DAYS, 2)
        day_count = dfg.get(fl.DAYCOUNT)
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        calendar = dfg.get(fl.CALENDAR, ql.UnitedStates())
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

    @classmethod
    def _to_tenor(cls, start_date, end_date):
        time_delta = end_date - start_date
        temp = 365./time_delta.days
        return round(temp)  # very ugly!!!


class BondRateHelperCreator(object):
    @staticmethod
    def create(self, data, asof_date, convention=None):
        dfg = CheckedDataFieldGetter(data, convention)
        schedule = ScheduleCreator.create(data, asof_date, convention)
        face_amount = dfg.get(fl.FACE_AMOUNT, 100.0)
        settlement_days = dfg.get(fl.SETTLEMENT_DAYS, 2)
        day_count = dfg.get(fl.DAYCOUNT)
        convention = dfg.get(fl.DAY_CONVENTION, ql.Following)
        price = dfg.get(fl.PRICE_LAST)
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


class BondYieldCurveCreator(object):
    @staticmethod
    def create(data, asof_date, conventions=None):
        curve_members = data[fl.CURVE_MEMBERS.id]
        conventions = data.get(fl.CONVENTIONS.id, conventions)
        rate_helpers = []
        for c in curve_members:
            loc_conventions = conventions or c.get(fl.CONVENTIONS.id)
            dfg = CheckedDataFieldGetter(c, loc_conventions)
            instance = dfg.get(fl.INSTANCE)
            loc_asof_date = dfg.get(fl.ASOF_DATE, asof_date)

            if isinstance(instance, InstrumentName) and (instance.security_subtype == SecuritySubType.ZCB):
                depo_rate_helper = DepositRateHelperCreator.create(c, loc_asof_date, conventions)
                rate_helpers.append(depo_rate_helper)
            elif isinstance(instance, InstrumentName) and (instance.security_subtype == SecuritySubType.BOND):
                bond_rate_helper = BondRateHelperCreator.create(c, loc_asof_date, conventions)
                rate_helpers.append(bond_rate_helper)

        day_count = ql.Actual360()

        yc_curve = ql.PiecewiseLogCubicDiscount(
            asof_date,
            rate_helpers,
            day_count
        )

        return yc_curve