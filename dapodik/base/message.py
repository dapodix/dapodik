import attr
import cattr
import json


@attr.dataclass(frozen=True, slots=True)
class DapodikMessage:
    success: bool = True
    message: str = ""

    @classmethod
    def from_str(cls, obj: str) -> "DapodikMessage":
        obj = obj.replace("'", '"')
        data = json.loads(obj)
        return cattr.structure(data, cls)
