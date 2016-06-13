from .common import Name, Instance


class CollectionName(Name, Instance):
    _id_map = {}

    def __init__(self, name):
        collection_id = self.toid(name)
        super(CollectionName, self).__init__(name, collection_id, True)
        Instance.__init__(self, "Collection")

class Collection(object):
    SECURITIES = CollectionName("Securities")
    CURVE_MEMBERS = CollectionName("Curve Members")

