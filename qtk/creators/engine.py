from .common import CreatorBase
from qtk.templates import Template as T


class DiscountingBondEngineCreator(CreatorBase):
    _templates = [T.ENG_BOND_DISCOUNTING]
    _req_fields = []
    _opt_fields = []

    def _create(self, asof_date):
        pass

