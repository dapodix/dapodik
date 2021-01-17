from dapodik.base import BaseDapodik
from . import Sekolah


class BaseSekolah(BaseDapodik):
    def __call__(self) -> Sekolah:
        return self.sekolah()

    def sekolah(self) -> Sekolah:
        res = self._get_rest("Sekolah")
        data: dict = res.json()
        _sekolah: list = data.get("rows", list())
        return self._fd(Sekolah, _sekolah[0])
