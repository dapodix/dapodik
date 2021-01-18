from typing import List, Union
from typing_extensions import Literal
from uuid import UUID

from dapodik import __semester__
from dapodik.base import BaseDapodik
from . import (
    AnggotaRombel,
    Pembelajaran,
    RombonganBelajar,
)

__fetch__ = (
    AnggotaRombel,
    Pembelajaran,
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
        url = "allanggotarombel/" + str(rombongan_belajar_id)
        res = self._get_rest(
            url, page=page, start=start, limit=limit, prefix="customrest/"
        )
        data: dict = res.json()
        return self._fl(AnggotaRombel, data.get("rows"))

    def pembelajaran(self) -> List[Pembelajaran]:
        res = self._get_rest("Pembelajaran")
        data: dict = res.json()
        return self._fl(Pembelajaran, data.get("rows"))

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
