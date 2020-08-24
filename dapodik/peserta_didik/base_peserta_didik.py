from dapodik import (
    BaseDapodik,
    Rest,
    PesertaDidik,
    PesertaDidikBaru,
    PesertaDidikLongitudinal,
    RegistrasiPesertaDidik,
)


class BasePesertaDidik(BaseDapodik):
    def register_peserta_didik(self) -> bool:
        try:
            self._PesertaDidik = Rest(self, PesertaDidik, 'rest/PesertaDidik')
            self._PesertaDidikBaru = Rest(self, PesertaDidikBaru,
                                          'rest/PesertaDidikBaru')
            self._PesertaDidikLongitudinal = Rest(
                self, PesertaDidikLongitudinal,
                'rest/PesertaDidikLongitudinal')
            self._RegistrasiPesertaDidik = Rest(self, RegistrasiPesertaDidik,
                                                'rest/RegistrasiPesertaDidik')
            self.logger.debug('Berhasil memulai peserta didik')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
