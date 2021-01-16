from typing import List

from dapodik.base import BaseDapodik
from . import Validasi


class BaseValidasi(BaseDapodik):
    def sekolah(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Validasi]:
        res = self._validasi("sekolah", page, start, limit)
        data: dict = res.json()
        return self._fl(Validasi, data.get("rows"))

    def peserta_didik(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Validasi]:
        res = self._validasi("peserta_didik", page, start, limit)
        data: dict = res.json()
        return self._fl(Validasi, data.get("rows"))

    def _validasi(
        self, jenis_validasi: str, page: int = 1, start: int = 0, limit: int = 50
    ):
        params = {
            "jenis_validasi": jenis_validasi,
            "page": page,
            "start": start,
            "limit": limit,
        }
        return self._get("validation", params=params)
