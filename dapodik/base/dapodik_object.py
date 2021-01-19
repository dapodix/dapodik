from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from dapodik import Dapodik
from . import UID


class DapodikObject(object):
    __slots__ = ()
    __id__: str = ""
    __dapodik__: Optional["Dapodik"] = None

    def __attr_post_init__(self):
        pass

    @property
    def id(self) -> UID:
        return getattr(self, self.__id__)

    def __str__(self):
        return getattr(self, "nama", repr(self))
