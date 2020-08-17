from dapodik.base import BaseDapodik, Rest
from .ptk import Ptk
from .ptk_terdaftar import PtkTerdaftar


class BaseRombonganBelajar(BaseDapodik):
    _Ptk: Ptk = None
    _PtkTerdaftar: PtkTerdaftar = None

    @property
    def Ptk(self):
        if self._Ptk:
            return self._Ptk
        self._Ptk = Rest(
            self, Ptk, 'rest/Ptk'
        )
        return self._Ptk

    @property
    def PtkTerdaftar(self):
        if self._PtkTerdaftar:
            return self._PtkTerdaftar
        self._PtkTerdaftar = Rest(
            self, PtkTerdaftar, 'rest/PtkTerdaftar'
        )
        return self._PtkTerdaftar
