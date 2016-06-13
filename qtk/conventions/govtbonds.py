from qtk.common import Name


class ConventionName(Name):
    _id_map = {}

    def __init__(self, instance):
        super(ConventionName, self).__init__(instance.id, instance.id)


