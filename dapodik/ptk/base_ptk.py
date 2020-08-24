from dapodik import BaseDapodik, Rest
from dapodik import PtkTerdaftar
from dapodik import Ptk


class BasePtk(BaseDapodik):
    def register_ptk(self) -> bool:
        try:
            self._Ptk = Rest(self, Ptk, 'rest/Ptk')
            self._PtkTerdaftar = Rest(self, PtkTerdaftar, 'rest/PtkTerdaftar')
            self.logger.debug('Berhasil memulai ptk')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
