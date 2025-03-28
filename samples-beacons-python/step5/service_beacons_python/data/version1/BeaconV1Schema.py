from pip_services4_commons.convert import TypeCode
from pip_services4_data.validate import ObjectSchema

class BeaconV1Schema(ObjectSchema):
    def __init__(self):
        super(BeaconV1Schema, self).__init__()

        self.with_optional_property("id", TypeCode.String)
        self.with_required_property("site_id", TypeCode.String)
        self.with_optional_property("type", TypeCode.String)
        self.with_required_property("udi", TypeCode.String)
        self.with_optional_property("label", TypeCode.String)
        self.with_optional_property("center", TypeCode.Map)
        self.with_optional_property("radius", TypeCode.Float)
