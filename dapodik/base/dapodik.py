from requests import Session, Response
from typing import Type, TypeVar
from .config import HEADERS

T = TypeVar("T", bound="BaseDapodik")


class BaseDapodik:
    def __init__(
        self,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
        semester_id: str = "20202",
    ):
        self.__server = server
        self.__session = session
        self.__session.headers.update(HEADERS)
        self.__semester_id = semester_id

    def _get(self, url: str, *kwargs: str) -> Response:
        return self.__session.get(url, params=kwargs)

    @classmethod
    def _inject(cls: Type[T], parent: Type[T]) -> T:
        kwargs = {
            "server": getattr(parent, "__server"),
            "session": getattr(parent, "__session"),
            "semester_id": getattr(parent, "__semester_id"),
        }
        return cls(**kwargs)
