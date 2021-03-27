from functools import partialmethod
from typing import List

from dapodik.base import BaseDapodik, DapodikMessage
from . import (
    PesertaDidikBaru,
    PesertaDidikLongitudinal,
    PesertaDidik,
    RegistrasiPesertaDidik,
)


class BasePesertaDidik(BaseDapodik):
    def peserta_didik_baru(self) -> List[PesertaDidikBaru]:
        return self._get_rest("PesertaDidikBaru", List[PesertaDidikBaru])

    def peserta_didik_longitudinal(
        self,
        peserta_didik_id: str,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[PesertaDidikLongitudinal]:
        query = {
            "peserta_didik_id": peserta_didik_id,
            "page": page,
            "start": start,
            "limit": limit,
        }
        return self._get_rest(
            "PesertaDidikLongitudinal", List[PesertaDidikLongitudinal], query=query
        )

    def peserta_didik(
        self,
        sekolah_id: str,
        page: int = 1,
        start: int = 0,
        limit: int = 25,
        nama: str = None,
        pd_module: str = "pdterdaftar",
    ) -> List[PesertaDidik]:
        """Dapatkan data peserta didik
        Args:
            sekolah_id (str): ID sekolah
            pd_module (str, optional): Modul. Defaults to "pdterdaftar". pdkeluar | pdterdaftar
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
        return self._get_rest("PesertaDidik", List[PesertaDidik], query=params)

    peserta_didik_keluar = partialmethod(peserta_didik, pd_module="pdkeluar")

    def registrasi_peserta_didik(self) -> List[RegistrasiPesertaDidik]:
        return self._get_rest("RegistrasiPesertaDidik", List[RegistrasiPesertaDidik])

    def salin_periodik_longitudinal(
        self,
        sekolah_id: str,
        semester_yl: str,
        semester_now: str,
        table: str = "peserta_didik_longitudinal",
    ) -> DapodikMessage:
        """Menyalin semua Data Periodik Peserta Didik aktif dari semester_yl ke semester_now
        Args:
            sekolah_id (str): ID sekolah
            semester_yl (str): ID semester sumber
            semester_now (str): ID semester sekarang
            table (str, optional): Table dari data. Defaults to "peserta_didik_longitudinal".
        Returns:
            DapodikMessage: Pesan
        """
        data = {
            "table": table,
            "sekolah_id": sekolah_id,
            "semester_yl": semester_yl,
            "semester_now": semester_now,
        }
        res = self._post("salinPeriodik", data)
        return DapodikMessage.from_str(res.text)

    def save_pdb(self, pdb: PesertaDidikBaru) -> DapodikMessage:
        """Save Pdb to Pd
        Args:
            pdb (PesertaDidikBaru): Instance dari PesertaDidikBaru
        Returns:
            DapodikMessage: Pesan
        """
        data = {"pdb_id": pdb.pdb_id}
        res = self._post("customrest/savePdb", data)
        return DapodikMessage.from_str(res.text)
