from dapodik.base import BaseDapodik, Rest
from .pembelajaran import Pembelajaran
from .rombongan_belajar import RombonganBelajar


class BaseRombonganBelajar(BaseDapodik):
    _Pembelajaran: Pembelajaran = None
    _RombonganBelajar: RombonganBelajar = None

    @property
    def Pembelajaran(self):
        if self._Pembelajaran:
            return self._Pembelajaran
        self._Pembelajaran = Rest(
            self, Pembelajaran, 'rest/Pembelajaran'
        )
        return self._Pembelajaran

    @property
    def RombonganBelajar(self):
        if self._RombonganBelajar:
            return self._RombonganBelajar
        self._RombonganBelajar = Rest(
            self, RombonganBelajar, 'rest/RombonganBelajar'
        )
        return self._RombonganBelajar
