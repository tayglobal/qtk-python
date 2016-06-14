from .common import Name, Instance


class Collection(Name, Instance):
    _id_map = {}

    def __init__(self, name):
        collection_id = self.toid(name)
        super(Collection, self).__init__(name, collection_id, True)
        Instance.__init__(self)


class CollectionList(object):
    SECURITIES = Collection("Securities")
    CURVE_MEMBERS = Collection("Curve Members")

