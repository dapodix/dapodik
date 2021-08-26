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

    @classmethod
    def from_fail(cls, res: str) -> "DapodikMessage":
        assert res.startswith("{ 'success' : false, 'message' : '")
        res = res.replace(
            "{ 'success' : false, 'message' : '", '{ "success" : false, "message" : "'
        )
        res = res.replace("' }", '" }')
        data = json.loads(res)
        return cattr.structure(data, cls)

    def __str__(self):
        return self.message

    def __bool__(self):
        return self.success
