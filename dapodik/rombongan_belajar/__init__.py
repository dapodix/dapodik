from dapodik.base import BaseDapodik, Rest
from .pembelajaran import Pembelajaran


class BaseRombonganBelajar(BaseDapodik):
    _Pembelajaran: Pembelajaran = None

    def Pembelajaran(self):
        if self._Pembelajaran:
            return self._Pembelajaran
        self._Pembelajaran = Rest(
            self, Pembelajaran, 'rest/Pembelajaran'
        )