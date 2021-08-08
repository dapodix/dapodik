import attr
import cattr
import json
from typing import Generic, Optional, Type, TypeVar

T = TypeVar("T")


@attr.dataclass
class DapodikResponse(Generic[T]):
    success: bool
    message: str
    rows: Optional[T] = None

    @classmethod
    def from_str(cls, data: str, cl: Type[T]):
        data = data.replace("'success'", '"success"')
        data = data.replace("'message' : '", '"message" : "')
        data = data.replace("', 'rows'", '", "rows"')
        data_dict: dict = json.loads(data)
        if "rows" in data_dict and data_dict["rows"]:
            rows = cattr.structure(data_dict["rows"], cl)
            return cls(
                success=data_dict["success"], message=data_dict["message"], rows=rows
            )
        return cls(
            success=data_dict["success"], message=data_dict["message"], rows=None
        )
