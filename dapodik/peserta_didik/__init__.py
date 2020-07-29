from dapodik.base import BaseDapodik
from dapodik.base import BaseDapodik, Rest
from .peserta_didik import PesertaDidik
from .peserta_didik_baru import PesertaDidikBaru
from .peserta_didik_longitudinal import PesertaDidikLongitudinal
from .registrasi_peserta_didik import RegistrasiPesertaDidik


class BasePesertaDidik(BaseDapodik):
    _PesertaDidik: PesertaDidik = None
    _PesertaDidikBaru: PesertaDidikBaru = None
    _PesertaDidikLongitudinal: PesertaDidikLongitudinal = None
    _RegistrasiPesertaDidik: RegistrasiPesertaDidik = None

    @property
    def PesertaDidik(self) -> [PesertaDidik]:
        if self._PesertaDidik:
            return self._PesertaDidik
        params = {
            'sekolah_id': self.sekolah_id,
        }
        self._PesertaDidik = Rest(
            self, PesertaDidik, 'rest/PesertaDidik', params=params)
        return self._PesertaDidik

    @property
    def PesertaDidikBaru(self) -> [PesertaDidikBaru]:
        if self._PesertaDidikBaru:
            return self._PesertaDidikBaru
        self._PesertaDidikBaru = Rest(
            self, PesertaDidikBaru, 'rest/PesertaDidikBaru'
        )
        return self._PesertaDidikBaru

    @property
    def PesertaDidikLongitudinal(self) -> [PesertaDidikLongitudinal]:
        if self._PesertaDidikLongitudinal:
            return self._PesertaDidikLongitudinal
        self._PesertaDidikLongitudinal = Rest(
            self, PesertaDidikLongitudinal, 'rest/PesertaDidikLongitudinal'
        )
        return self._PesertaDidikLongitudinal

    @property
    def RegistrasiPesertaDidik(self) -> [RegistrasiPesertaDidik]:
        if self._RegistrasiPesertaDidik:
            return self._RegistrasiPesertaDidik
        self._RegistrasiPesertaDidik = Rest(
            self, RegistrasiPesertaDidik, 'rest/RegistrasiPesertaDidik'
        )
        return self._RegistrasiPesertaDidik
