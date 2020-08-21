from dapodik.base import BaseDapodik, Rest
from .akreditasi_sp import AkreditasiSp
from .blockgrant import BlockGrant
from .kepanitiaan import Kepanitiaan
from .program_inklusi import ProgramInklusi
from .sanitasi import Sanitasi
from .sekolah import Sekolah
from .sekolah_longitudinal import SekolahLongitudinal
from .sekolah_paud import SekolahPaud
from .yayasan import Yayasan


class BaseSekolah(BaseDapodik):
    def register_sekolah(self) -> bool:
        try:
            self.AkreditasiSp = Rest(
                self, AkreditasiSp, 'rest/AkreditasiSp'
            )
            self.BlockGrant = Rest(
                self, BlockGrant, 'rest/BlockGrant'
            )
            self.Kepanitiaan = Rest(
                self, Kepanitiaan, 'rest/Kepanitiaan'
            )
            self.ProgramInklusi = Rest(
                self, ProgramInklusi, 'rest/ProgramInklusi'
            )
            self.Sanitasi = Rest(
                self, Sanitasi, 'rest/Sanitasi'
            )
            self.Sekolah = Rest(
                self, Sekolah, 'rest/Sekolah'
            )
            self.SekolahLongitudinal = Rest(
                self, SekolahLongitudinal, 'rest/SekolahLongitudinal'
            )
            self.SekolahPaud = Rest(
                self, SekolahPaud, 'rest/SekolahPaud'
            )
            self.Yayasan = Rest(
                self, Yayasan, 'rest/Yayasan'
            )
            self.logger.debug('Berhasil memulai sekolah')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
