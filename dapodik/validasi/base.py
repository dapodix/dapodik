from typing import List

from dapodik.base import BaseDapodik
from . import Validasi


class BaseValidasi(BaseDapodik):
    def sekolah(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Validasi]:
        """Data validasi Sekolah

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("sekolah", page, start, limit)

    def prasarana(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        """Data validasi Sarpras

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("prasarana", page, start, limit)

    def peserta_didik(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        """Data validasi Peserta Didik

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("peserta_didik", page, start, limit)

    def ptk(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Validasi]:
        """Data validasi GTK

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("ptk", page, start, limit)

    def rombongan_belajar(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        """Data validasi Rombongan Belajar & Jadwal

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("rombongan_belajar", page, start, limit)

    def pembelajaran(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        """Data validasi Pembelajaran

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("pembelajaran", page, start, limit)

    def nilai(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Validasi]:
        """Data validasi Nilai

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("nilai", page, start, limit)

    def referensi(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        """Data validasi Referensi

        Args:
            page (int, optional): Halaman. Defaults to 1.
            start (int, optional): Dimulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 50.

        Returns:
            List[Validasi]: list dari validasi
        """
        return self._validasi("referensi", page, start, limit)

    def _validasi(
        self, jenis_validasi: str, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        params = {
            "jenis_validasi": jenis_validasi,
            "page": page,
            "start": start,
            "limit": limit,
        }
        res = self._get("validation", params=params)
        return self._fr(Validasi, res.json())
