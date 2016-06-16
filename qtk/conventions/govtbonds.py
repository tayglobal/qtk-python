from qtk.common import NameBase


class ConventionName(NameBase):
    _id_map = {}

    def __init__(self, instance):
        super(ConventionName, self).__init__(instance.id, instance.id)


