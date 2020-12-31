from typing import List

from dapodik import (
    BaseDapodik,
    PesertaDidik,
    PesertaDidikBaru,
    PesertaDidikLongitudinal,
    RegistrasiPesertaDidik,
)


class BasePesertaDidik(BaseDapodik):
    def register_peserta_didik(self) -> bool:
        try:
            self.PesertaDidik = PesertaDidik.maker(self, "rest/PesertaDidik")
            self.PesertaDidikBaru = PesertaDidikBaru.maker(
                self, "rest/PesertaDidikBaru"
            )
            self.PesertaDidikLongitudinal = PesertaDidikLongitudinal.maker(
                self, "rest/PesertaDidikLongitudinal"
            )
            self.RegistrasiPesertaDidik = RegistrasiPesertaDidik.maker(
                self, "rest/RegistrasiPesertaDidik"
            )
            self.logger.debug("Berhasil memulai peserta didik")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def peserta_didik(self) -> List[PesertaDidik]:
        return self.PesertaDidik()  # type: ignore

    @property
    def peserta_didik_baru(self) -> List[PesertaDidikBaru]:
        return self.PesertaDidikBaru()  # type: ignore

    @property
    def peserta_didik_longitudinal(self) -> List[PesertaDidikLongitudinal]:
        return self.PesertaDidikLongitudinal()  # type: ignore

    @property
    def registrasi_peserta_didik(self) -> List[RegistrasiPesertaDidik]:
        return self.RegistrasiPesertaDidik()  # type: ignore
