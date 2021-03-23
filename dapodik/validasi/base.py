from dapodik.base import BaseDapodik
from typing import List, Type, TypeVar

from . import Validasi
from . import ValidasiSekolah
from . import ValidasiPrasarana
from . import ValidasiPesertaDidik
from . import ValidasiPtk
from . import ValidasiRombonganBelajar
from . import ValidasiPembelajaran
from . import ValidasiNilai
from . import ValidasiReferensi

V = TypeVar("V", bound=Validasi)


class BaseValidasi(BaseDapodik):
    def validasi_sekolah(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiSekolah]:
        """Data validasi Sekolah
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("sekolah", List[ValidasiSekolah], page, start, limit)

    def validasi_prasarana(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiPrasarana]:
        """Data validasi Sarpras
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("prasarana", List[ValidasiPrasarana], page, start, limit)

    def validasi_peserta_didik(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiPesertaDidik]:
        """Data validasi Peserta Didik
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi(
            "peserta_didik", List[ValidasiPesertaDidik], page, start, limit
        )

    def validasi_ptk(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiPtk]:
        """Data validasi GTK
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("ptk", List[ValidasiPtk], page, start, limit)

    def validasi_rombongan_belajar(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiRombonganBelajar]:
        """Data validasi Rombongan Belajar & Jadwal
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi(
            "rombongan_belajar", List[ValidasiRombonganBelajar], page, start, limit
        )

    def validasi_pembelajaran(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiPembelajaran]:
        """Data validasi Pembelajaran
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi(
            "pembelajaran", List[ValidasiPembelajaran], page, start, limit
        )

    def validasi_nilai(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiNilai]:
        """Data validasi Nilai
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("nilai", List[ValidasiNilai], page, start, limit)

    def validasi_referensi(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[ValidasiReferensi]:
        """Data validasi Referensi
        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.
        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("referensi", List[ValidasiReferensi], page, start, limit)

    def _validasi(
        self,
        jenis_validasi: str,
        tipe_validasi: Type[List[V]],
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[V]:
        params = {
            "jenis_validasi": jenis_validasi,
            "page": page,
            "start": start,
            "limit": limit,
        }
        return self._get_rows(path="validation", query=params, cl=tipe_validasi)
