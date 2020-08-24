from dapodik.base import BaseDapodik, Rest
from dapodik import Tanah
from dapodik import Bangunan
from dapodik import Ruang
from dapodik import Alat
from dapodik import Angkutan
from dapodik import Buku
from dapodik import BangunanLongitudinal
from dapodik import BangunanDariBlockgrant
from dapodik import RuangLongitudinal
from dapodik import AlatLongitudinal
from dapodik import AlatDariBlockgrant
from dapodik import AngkutanDariBlockgrant
from dapodik import BukuLongitudinal


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
            self.Angkutan = Rest(
                self, Angkutan, 'rest/Angkutan'
            )
            self.Buku = Rest(
                self, Buku, 'rest/Buku'
            )
            self.AngkutanDariBlockgrant = Rest(
                self, AngkutanDariBlockgrant, 'rest/AngkutanDariBlockgrant'
            )
            self.BukuLongitudinal = Rest(
                self, BukuLongitudinal, 'rest/BukuLongitudinal'
            )
            self.logger.debug('Berhasil memulai sarpras')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
