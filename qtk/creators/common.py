
class CreatorBaseMeta(type):

    def __new__(meta, name, bases, dct):
        return super(CreatorBaseMeta, meta).__new__(meta, name, bases, dct)

    def __init__(self, name, bases, dct):
        templates = dct.get("_templates")
        if templates is not None:
            if isinstance(templates, list):
                for t in templates:
                    t._set_creator(self)
            else:
                raise ValueError("_template not of type list")
        elif name != "CreatorBase":
            raise AttributeError("Expected _templates class variable definition for creator ", self)

        req_fields = dct.get("_req_fields")
        if req_fields is not None:
            if isinstance(req_fields, list):
                t._set_req_fields(req_fields)
            else:
                raise ValueError("_req_fields not of type list")
        elif name != "CreatorBase":
            raise AttributeError("Expected _req_fields class variable definition for creator ", self)

        opt_fields = dct.get("_opt_fields")
        if opt_fields is not None:
            if isinstance(opt_fields, list):
                t._set_opt_fields(opt_fields)
            else:
                raise ValueError("_opt_fields not of type list")

        super(CreatorBaseMeta, self).__init__(name, bases, dct)


class CreatorBase(object):
    """
    Every creator must inherit this class. This class adds properties
    to link every template with a creator in an automated way. In order
    to do this, every class that inherits CreatorBase must define a variable
    "_templates" which is a list of all templates that it can instantiate.
    """
    __metaclass__ = CreatorBaseMeta

    @classmethod
    def get_templates(cls):
        return cls._templates




