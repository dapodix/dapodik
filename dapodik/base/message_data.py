from typing import Generic, List, TypeVar, Union

T = TypeVar("T")

SAFE = [
    ("'success'", '"success"'),
    ("'message' : '", '"message" : "'),
    ("', 'rows'", '", "rows"'),
    ("' }", '" }'),
]


class MessageData(Generic[T]):
    success: bool
    message: str
    rows: Union[List[T], T, None]

    def __init__(
        self,
        success: bool,
        message: str,
        rows: Union[List[T], T, None] = None,
    ) -> None:
        self.success = success
        self.message = message
        self.rows = rows

    @property
    def data(self) -> Union[List[T], T, None]:
        return self.rows

    def __bool__(self):
        return self.success

    def __str__(self):
        return self.message

    def __repr__(self):
        return repr(self.rows)

    @staticmethod
    def safe(text: str) -> str:
        for o, n in SAFE:
            text = text.replace(o, n)
        return text
