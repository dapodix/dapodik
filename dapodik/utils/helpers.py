from dataclasses import Field, _FIELD, _FIELDS, _FIELD_INITVAR  # type: ignore
from typing import TypeVar, Type, Any, List

AnyT = TypeVar("AnyT", bound=Any)


def get_dataclass_fields(data_class: Type[AnyT]) -> List[Field]:
    """Helper method to get fields of dataclass
    Args:
        data_class (Type[AnyT]): A dataclass object is preferred
    Returns:
        List[Field]: The fields of data_class
    """
    fields = getattr(data_class, _FIELDS)
    return [
        f for f in fields.values()
        if f._field_type is _FIELD or f._field_type is _FIELD_INITVAR
    ]
