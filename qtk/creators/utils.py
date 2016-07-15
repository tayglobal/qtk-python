from .common import CreatorBase
from qtk.templates import Template as T
from qtk.fields import Field as F
import QuantLib as ql


class ScheduleCreator(CreatorBase):
    _templates = [T.SCHEDULE]
    _req_fields = [F.ISSUE_DATE, F.MATURITY_DATE, F.COUPON_FREQ]
    _opt_fields = []

    def _create(self, asof_date):

        maturity_date = self.get(F.MATURITY_DATE)
        issue_date = self.get(F.ISSUE_DATE) or self.get(F.ASOF_DATE) or asof_date
        #asof_date = asof_date
        coupon_freq = self.get(F.COUPON_FREQ)
        period = ql.Period(coupon_freq)
        calendar = self.get(F.ACCRUAL_CALENDAR)
        convention = self.get(F.ACCRUAL_DAY_CONVENTION)
        termination_convention = self.get(F.TERMINATION_DAY_CONVENTION, convention)
        end_of_month = self.get(F.END_OF_MONTH, True)

        schedule = ql.Schedule(issue_date,
                               maturity_date,
                               period,
                               calendar,
                               convention,
                               termination_convention,
                               ql.DateGeneration.Backward,
                               end_of_month)
        return schedule