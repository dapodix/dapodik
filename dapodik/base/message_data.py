from typing import Generic, List, TypeVar, Union

T = TypeVar("T")


class MessageData(Generic[T]):
    success: bool
    message: str
    rows: Union[List[T], T]

    def __init__(
        self,
        success: bool,
        message: str,
        rows: Union[List[T], T],
    ) -> None:
        self.success = success
        self.message = message
        self.rows = rows

    @property
    def data(self) -> Union[List[T], T]:
        return self.rows

    def __bool__(self):
        return self.success

    def __str__(self):
        return self.message
