from dapodik.base import BaseDapodik, Rest
from .alat import Alat
from .alat_dari_blockgrant import AlatDariBlockgrant
from .alat_longitudinal import AlatLongitudinal
from .bangunan import Bangunan
from .bangunan_dari_blockgrant import BangunanDariBlockgrant
from .bangunan_longitudinal import BangunanLongitudinal
from .ruang import Ruang
from .ruang_longitudinal import RuangLongitudinal
from .tanah import Tanah


class BaseSarpras(BaseDapodik):
    def register_sarpras(self):
        try:
            self.Alat = Rest(
                self, Alat, 'rest/Alat'
            )
            self.AlatDariBlockgrant = Rest(
                self, AlatDariBlockgrant, 'rest/AlatDariBlockgrant'
            )
            self.AlatLongitudinal = Rest(
                self, AlatLongitudinal, 'rest/AlatLongitudinal'
            )
            self.Bangunan = Rest(
                self, Bangunan, 'rest/Bangunan'
            )
            self.BangunanDariBlockgrant = Rest(
                self, BangunanDariBlockgrant, 'rest/BangunanDariBlockgrant'
            )
            self.BangunanLongitudinal = Rest(
                self, BangunanLongitudinal, 'rest/BangunanLongitudinal'
            )
            self.Ruang = Rest(
                self, Ruang, 'rest/Ruang'
            )
            self.RuangLongitudinal = Rest(
                self, RuangLongitudinal, 'rest/RuangLongitudinal'
            )
            self.Tanah = Rest(
                self, Tanah, 'rest/Tanah'
            )
            self.logger.debug('Berhasil memulai sarpras')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
