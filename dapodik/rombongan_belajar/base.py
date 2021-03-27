from typing import List, Union

from dapodik.base import BaseDapodik, DapodikMessage
from dapodik.rest import TingkatPendidikan
from dapodik.version import __semester__

from . import AnggotaRombel
# from . import Pembelajaran
from . import RombelPortal
from . import RombonganBelajar


class BaseRombonganBelajar(BaseDapodik):
    def anggota_rombel(
        self,
        rombongan_belajar_id: str,
        page: int = 1,
        start: int = 0,
        limit: Union[int, str] = 25,
    ) -> List[AnggotaRombel]:
        """Mengammbil data-data anggota rombel
        Args:
            rombongan_belajar_id (Union[UUID, str]): ID rombongan belajar
            page (int, optional): Halaman data ke. Defaults to 1.
            start (int, optional): Mulai dari. Defaults to 0.
            limit (int, str, optional): Batas data yang dikembalikan. Defaults to 25. int atau unlimited
        Returns:
            List[AnggotaRombel]: list dari AnggotaRombel
        """
        return self._get_rest(
            path="allanggotarombel/" + str(rombongan_belajar_id),
            cl=List[AnggotaRombel],
            page=page,
            start=start,
            limit=limit,
            prefix="customrest/",
            key=lambda x: x,
        )

    def rombel_portal(
        self,
        sekolah_id: str,
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
        return self._get_rest(
            path="RombelPortal",
            cl=List[RombelPortal],
            page=page,
            start=start,
            limit=limit,
            query={"sekolah_id": sekolah_id},
            prefix="customrest/",
        )

    def rombongan_belajar(
        self,
        sekolah_id: str,
        semester_id: str = __semester__,
        ascending: str = "#INjenis_rombel,tingkat_pendidikan_id,nama",
        callback: str = "rombonganbelajar",
        jenis_rombel: str = "#IN1,5,6,7,8,9,10",
        sks=0,
        limit: Union[int, str] = "unlimited",
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
            "page": page,
            "start": start,
            "limit": limit,
        }
        return self._get_rest(
            path="RombonganBelajar",
            cl=List[RombonganBelajar],
            query=params,
        )

    def kenaikan_kelas(
        self, rombongan_belajar_id: str, semester_id: str = __semester__
    ) -> DapodikMessage:
        """kenaikan_kelas rombongan belajar
        Args:
            rombongan_belajar_id (Union[UUID, str]): ID dari rombongan belajar
            semester_id (str, optional): Naikkan ke semester. Defaults dapodik.__semester__.
        Returns:
            DapodikMessage: Pesan sukses / tidak
        """
        data = dict(
            rombongan_belajar_id=rombongan_belajar_id,
            semester_id=semester_id,
        )
        res = self._post("kenaikankelas", data)
        return DapodikMessage.from_str(res.text)

    def filter_tingkat_pendidikan(
        self,
        fromui: str = None,
        callback: str = "rombonganbelajar",
        jurusan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[TingkatPendidikan]:
        """filter_tingkat_pendidikan [summary]
        Args:
            fromui (str, optional): Misal tingkatpendidikanpaud. Defaults "".
            callback (str, optional): callback. Defaults "rombonganbelajar".
            jurusan_id (int, optional): id jurusan. Defaults "".
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
        return self._get_rest(
            path="filtertingkatpendidikan",
            cl=List[TingkatPendidikan],
            query=params,
        )
