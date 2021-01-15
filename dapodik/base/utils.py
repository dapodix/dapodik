from typing import List, Type, TypeVar


T = TypeVar("T")


def from_dict(t: Type[T], data: dict) -> T:
    return t(**data)  # type: ignore


def from_list(t: Type[T], datas: List[dict]) -> List[T]:
    results: List[T] = list()
    for data in datas:
        results.append(from_dict(t, data))
    return results
