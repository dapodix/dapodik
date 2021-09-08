from dapodik.base import BaseDapodik
from typing import List

from . import SekolahPaud
from . import Sekolah
from . import Semester
from . import Yayasan


class BaseSekolah(BaseDapodik):
    def sekolah_paud(self) -> List[SekolahPaud]:
        return self._get_rows("/rest/SekolahPaud", List[SekolahPaud])

    def sekolah(self, index: int = 0) -> Sekolah:
        return self._get_rows("/rest/Sekolah", List[Sekolah])[index]

    def semester(self) -> List[Semester]:
        return self._get_rows("/rest/Semester", List[Semester])

    def yayasan(self) -> List[Yayasan]:
        return self._get_rows("/rest/Yayasan", List[Yayasan])
