from typing import List, Union
from typing_extensions import Literal
from uuid import UUID

from dapodik import __semester__
from dapodik.base import BaseDapodik, Message, UID
from dapodik.rest import TingkatPendidikan
from . import (
    AnggotaRombel,
    Pembelajaran,
    RombelPortal,
    RombonganBelajar,
)

__fetch__ = (
    AnggotaRombel,
    Pembelajaran,
    RombelPortal,
    RombonganBelajar,
)


class BaseRombonganBelajar(BaseDapodik):
    __all__ = __fetch__

    def anggota_rombel(
        self,
        rombongan_belajar_id: Union[UUID, str],
        page: int = 1,
        start: int = 0,
        limit: Union[int, Literal["unlimited"]] = 25,
    ) -> List[AnggotaRombel]:
        """Mengammbil data-data anggota rombel

        Args:
            rombongan_belajar_id (Union[UUID, str]): ID rombongan belajar
            page (int, optional): Halaman data ke. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.
            limit (Union[int, Literal[, optional): Batas data yang dikembalikan. Defaults to 25.

        Returns:
            List[AnggotaRombel]: list dari AnggotaRombel
        """
        url = "allanggotarombel/" + str(rombongan_belajar_id)
        res = self._get_rest(
            url,
            page=page,
            start=start,
            limit=limit,
            prefix="customrest/",
        )
        return self._fl(AnggotaRombel, res.json())

    def rombel_portal(
        self,
        sekolah_id: UID,
        page: int = 1,
        start: int = 0,
        limit: int = 25,
    ) -> List[RombelPortal]:
        """rombel_portal dashboard

        Args:
            sekolah_id (UID): ID sekolah
            page (int, optional): Halaman ke. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.
            limit (int, optional): Batas data yang dikembalikan. Defaults to 25.

        Returns:
            List[RombelPortal]: list dari RombelPortal
        """
        params = dict(sekolah_id=sekolah_id)
        res = self._get_rest(
            "RombelPortal",
            params,
            page,
            start,
            limit,
            prefix="customrest/",
        )
        return self._fl(RombelPortal, res.json())

    def rombongan_belajar(
        self,
        sekolah_id: str,
        semester_id: str = __semester__,
        ascending: str = "#INjenis_rombel,tingkat_pendidikan_id,nama",
        callback: str = "rombonganbelajar",
        jenis_rombel: str = "#IN1,5,6,7,8,9,10",
        sks=0,
        limit: Union[int, Literal["unlimited"]] = "unlimited",
        page: int = 1,
        start: int = 0,
    ) -> List[RombonganBelajar]:
        """Mengammbil data-data rombongan belajar

        Args:
            sekolah_id (str): ID sekolah
            semester_id (str, optional): ID semester. Defaults to __semester__.
            ascending (str, optional): Sortir. Defaults to "#INjenis_rombel,tingkat_pendidikan_id,nama".
            callback (str, optional): Callback. Defaults to "rombonganbelajar".
            jenis_rombel (str, optional): Filter jenis rombel. Defaults to "#IN1,5,6,7,8,9,10".
            sks (int, optional): Jumlah sks. Defaults to 0.
            limit (Union[int, Literal[, optional): Batas data yang dikembalikan. Defaults to "unlimited".
            page (int, optional): Halaman data-data yang diambil. Defaults to 1.
            start (int, optional): Mulai. Defaults to 0.

        Returns:
            List[RombonganBelajar]: list dari RombonganBelajar
        """
        params = {
            "sekolah_id": sekolah_id,
            "semester_id": semester_id,
            "ascending": ascending,
            "callback": callback,
            "jenis_rombel": jenis_rombel,
            "sks": sks,
        }
        res = self._get_rest("RombonganBelajar", params, page, start, limit)
        data: dict = res.json()
        return self._fr(RombonganBelajar, data)

    def kenaikan_kelas(
        self, rombongan_belajar_id: Union[UUID, str], semester_id: str = __semester__
    ) -> Message:
        """kenaikan_kelas rombongan belajar

        Args:
            rombongan_belajar_id (Union[UUID, str]): ID dari rombongan belajar
            semester_id (str, optional): Naikkan ke semester. Defaults dapodik.__semester__.

        Returns:
            Message: Pesan sukses / tidak
        """
        data = dict(
            rombongan_belajar_id=rombongan_belajar_id,
            semester_id=semester_id,
        )
        res = self._post("kenaikankelas", data)
        return self._msg(res.json())

    def filter_tingkat_pendidikan(
        self,
        fromui: str = None,
        callback: str = "rombonganbelajar",
        jurusan_id: str = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[TingkatPendidikan]:
        """filter_tingkat_pendidikan [summary]

        Args:
            fromui (str, optional): Misal tingkatpendidikanpaud. Defaults "".
            callback (str, optional): callback. Defaults "rombonganbelajar".
            jurusan_id (str, optional): id jurusan. Defaults "".
            page (int, optional): halaman. Defaults 1.
            start (int, optional): mulai. Defaults 0.
            limit (int, optional): batas. Defaults 50.

        Returns:
            List[TingkatPendidikan]: list dari TingkatPendidikan
        """
        params = {
            "callback": callback,
            "jurusan_id": jurusan_id or "",
            "fromui": fromui or "",
            "page": page,
            "start": start,
            "limit": limit,
        }
        res = self._get("filtertingkatpendidikan", params)
        return self._fr(TingkatPendidikan, res.json())
