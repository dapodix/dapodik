from typing import MutableMapping, TypeVar, Union

T = TypeVar("T")

TResult = MutableMapping[Union[int, str], T]
