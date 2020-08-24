from dapodik import BaseDapodik, Rest
from dapodik import Pembelajaran
from dapodik import RombonganBelajar


class BaseRombonganBelajar(BaseDapodik):
    def register_rombongan_belajar(self) -> bool:
        try:
            self.Pembelajaran = Rest(
                self, Pembelajaran, 'rest/Pembelajaran'
            )
            self.RombonganBelajar = Rest(
                self, RombonganBelajar, 'rest/RombonganBelajar'
            )
            self.logger.debug('Berhasil memulai rombongan belajar')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
