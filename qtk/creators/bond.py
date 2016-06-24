from .common import CreatorBase
from qtk.templates import Template
from qtk.fields import Field


class FixedRateBondCreator(CreatorBase):
    _templates = [Template.INST_GOVT_BOND]
    _req_fields = [Field.FACE_AMOUNT]

    def _create(self, data, asof_date=None, conventions=None):
        pass
