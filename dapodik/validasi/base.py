from typing import List, Type, TypeVar

from dapodik.base import BaseDapodik
from . import (
    Validasi,
    ValidasiSekolah,
    ValidasiPrasarana,
    ValidasiPesertaDidik,
    ValidasiPtk,
    ValidasiRombonganBelajar,
    ValidasiPembelajaran,
    ValidasiNilai,
    ValidasiReferensi,
)

V = TypeVar("V", bound=Validasi)

__fetch__ = (
    ValidasiSekolah,
    ValidasiPrasarana,
    ValidasiPesertaDidik,
    ValidasiPtk,
    ValidasiRombonganBelajar,
    ValidasiPembelajaran,
    ValidasiNilai,
    ValidasiReferensi,
)


class BaseValidasi(BaseDapodik):
    def __add_validasi__(self) -> None:
        self.__all__ += __fetch__

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
        return self._validasi(ValidasiSekolah, page, start, limit)

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
        return self._validasi(ValidasiPrasarana, page, start, limit)

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
        return self._validasi(ValidasiPesertaDidik, page, start, limit)

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
        return self._validasi(ValidasiPtk, page, start, limit)

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
        return self._validasi(ValidasiRombonganBelajar, page, start, limit)

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
        return self._validasi(ValidasiPembelajaran, page, start, limit)

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
        return self._validasi(ValidasiNilai, page, start, limit)

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
        return self._validasi(ValidasiReferensi, page, start, limit)

    def _validasi(
        self, jenis_validasi: Type[V], page: int = 1, start: int = 0, limit: int = 50
    ) -> List[V]:
        params = {
            "jenis_validasi": jenis_validasi,
            "page": page,
            "start": start,
            "limit": limit,
        }
        res = self._get(jenis_validasi.location(), params=params)
        return self._fr(jenis_validasi, res.json())
