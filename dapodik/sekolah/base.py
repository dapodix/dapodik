from dapodik.base import BaseDapodik
from . import (
    AkreditasiSp,
    BlockGrant,
    JurusanSp,
    Kepanitiaan,
    ProgramInklusi,
    Sanitasi,
    SekolahLongitudinal,
    SekolahPaud,
    Sekolah,
    Semester,
    Yayasan,
)

__fetch__ = (
    AkreditasiSp,
    BlockGrant,
    JurusanSp,
    Kepanitiaan,
    ProgramInklusi,
    Sanitasi,
    SekolahLongitudinal,
    SekolahPaud,
    Sekolah,
    Semester,
    Yayasan,
)


class BaseSekolah(BaseDapodik):
    __all__ = __fetch__

    def sekolah(self) -> Sekolah:
        res = self._get_rest("Sekolah")
        data: dict = res.json()
        _sekolah: list = data.get("rows", list())
        return self._fd(Sekolah, _sekolah[0])
