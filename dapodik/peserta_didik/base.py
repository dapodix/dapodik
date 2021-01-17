from typing import List

from dapodik.base import BaseDapodik
from . import (
    PesertaDidikBaru,
    PesertaDidikLongitudinal,
    PesertaDidik,
    RegistrasiPesertaDidik,
)

__fetch__ = (
    PesertaDidikBaru,
    PesertaDidikLongitudinal,
    PesertaDidik,
    RegistrasiPesertaDidik,
)


class BasePesertaDidik(BaseDapodik):
    __all__ = __fetch__

    def __call__(self, sekolah_id: str) -> List[PesertaDidik]:
        return self.peserta_didik(sekolah_id)

    def peserta_didik_baru(self) -> List[PesertaDidikBaru]:
        res = self._get_rest("PesertaDidikBaru")
        data: dict = res.json()
        return self._fl(PesertaDidikBaru, data.get("rows"))

    def peserta_didik_longitudinal(self) -> List[PesertaDidikLongitudinal]:
        res = self._get_rest("PesertaDidikLongitudinal")
        data: dict = res.json()
        return self._fl(PesertaDidikLongitudinal, data.get("rows"))

    def peserta_didik(
        self,
        sekolah_id: str,
        pd_module: str = "pdterdaftar",
        page: int = 1,
        start: int = 0,
        limit: int = 25,
    ) -> List[PesertaDidik]:
        params = {
            "sekolah_id": sekolah_id,
            "pd_module": pd_module,
            "page": page,
            "start": start,
            "limit": limit,
        }
        res = self._get_rest("PesertaDidik", params)
        data: dict = res.json()
        return self._fl(PesertaDidik, data.get("rows"))

    def peserta_didik_keluar(
        self,
        sekolah_id: str,
        pd_module: str = "pdkeluar",
        page: int = 1,
        start: int = 0,
        limit: int = 25,
    ) -> List[PesertaDidik]:
        return self.peserta_didik(sekolah_id, pd_module, page, start, limit)

    def registrasi_peserta_didik(self) -> List[RegistrasiPesertaDidik]:
        res = self._get_rest("RegistrasiPesertaDidik")
        data: dict = res.json()
        return self._fl(RegistrasiPesertaDidik, data.get("rows"))
