from dapodik.base import BaseDapodik
from typing import List

from . import AkreditasiSp
from . import BlockGrant
from . import JurusanSp
from . import Kepanitiaan
from . import ProgramInklusi
from . import Sanitasi
from . import SekolahLongitudinal
from . import SekolahPaud
from . import Sekolah
from . import Semester
from . import Yayasan


class BaseSekolah(BaseDapodik):
    def akreditasi_sp(self) -> List[AkreditasiSp]:
        return self._get_rows("/rest/AkreditasiSp", List[AkreditasiSp])

    def blockgrant(self) -> List[BlockGrant]:
        return self._get_rows("/rest/BlockGrant", List[BlockGrant])

    def jurusan_sp(self) -> List[JurusanSp]:
        return self._get_rows("/rest/JurusanSp", List[JurusanSp])

    def kepanitiaan(self) -> List[Kepanitiaan]:
        return self._get_rows("/rest/Kepanitiaan", List[Kepanitiaan])

    def program_inklusi(self) -> List[ProgramInklusi]:
        return self._get_rows("/rest/ProgramInklusi", List[ProgramInklusi])

    def sanitasi(self) -> List[Sanitasi]:
        return self._get_rows("/rest/Sanitasi", List[Sanitasi])

    def sekolah_longitudinal(self) -> List[SekolahLongitudinal]:
        return self._get_rows("/rest/SekolahLongitudinal", List[SekolahLongitudinal])

    def sekolah_paud(self) -> List[SekolahPaud]:
        return self._get_rows("/rest/SekolahPaud", List[SekolahPaud])

    def sekolah(self, index: int = 0) -> Sekolah:
        return self._get_rows("/rest/Sekolah", List[Sekolah])[index]

    def semester(self) -> List[Semester]:
        return self._get_rows("/rest/Semester", List[Semester])

    def yayasan(self) -> List[Yayasan]:
        return self._get_rows("/rest/Yayasan", List[Yayasan])
