from functools import partialmethod
from json import loads
from typing import List
from typing_extensions import Literal

from dapodik.base import BaseDapodik, UID, Message
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
        return self._fr(PesertaDidikBaru, res.json())

    def peserta_didik_longitudinal(
        self,
        peserta_didik_id: UID,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[PesertaDidikLongitudinal]:
        params = {"peserta_didik_id": peserta_didik_id}
        res = self._get_rest(
            "PesertaDidikLongitudinal",
            params=params,
            page=page,
            start=start,
            limit=limit,
        )
        return self._fr(PesertaDidikLongitudinal, res.json())

    def peserta_didik(
        self,
        sekolah_id: str,
        page: int = 1,
        start: int = 0,
        limit: int = 25,
        nama: str = None,
        pd_module: Literal["pdterdaftar", "pdkeluar"] = "pdterdaftar",
    ) -> List[PesertaDidik]:
        """Dapatkan data peserta didik

        Args:
            sekolah_id (str): ID sekolah
            pd_module (str, optional): Modul. Defaults to "pdterdaftar".
            nama (str, optional): Filter berdasarkan nama. Defaults to None.
            page (int, optional): Halaman data. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.
            limit (int, optional): Batas data. Defaults to 25.

        Returns:
            List[PesertaDidik]: list dari peserta didik
        """
        params = {
            "sekolah_id": sekolah_id,
            "pd_module": pd_module,
            "page": page,
            "start": start,
            "limit": limit,
        }
        if isinstance(nama, str):
            params["nama"] = nama
        res = self._get_rest("PesertaDidik", params)
        return self._fr(PesertaDidik, res.json())

    peserta_didik_keluar = partialmethod(peserta_didik, pd_module="pdkeluar")

    def registrasi_peserta_didik(self) -> List[RegistrasiPesertaDidik]:
        res = self._get_rest("RegistrasiPesertaDidik")
        return self._fr(RegistrasiPesertaDidik, res.json())

    def salin_periodik_longitudinal(
        self,
        sekolah_id: str,
        semester_yl: str,
        semester_now: str,
        table: str = "peserta_didik_longitudinal",
    ) -> Message:
        """Menyalin semua Data Periodik Peserta Didik aktif dari semester_yl ke semester_now

        Args:
            sekolah_id (str): ID sekolah
            semester_yl (str): ID semester sumber
            semester_now (str): ID semester sekarang
            table (str, optional): Table dari data. Defaults to "peserta_didik_longitudinal".

        Returns:
            Message: Pesan
        """
        data = {
            "table": table,
            "sekolah_id": sekolah_id,
            "semester_yl": semester_yl,
            "semester_now": semester_now,
        }
        res = self._post("salinPeriodik", data)
        text = res.text.replace("'", '"')
        return self._fd(Message, loads(text))
