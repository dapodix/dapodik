from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dapodik import Dapodik


class BaseProp(object):
    @property
    def dapodik(self) -> "Dapodik":
        return getattr(self, "_dapodik")  # type: ignore
