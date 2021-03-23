from dapodik.base import BaseDapodik
from typing import List

from . import Sekolah


class BaseSekolah(BaseDapodik):
    def sekolah(self, index: int = 0) -> Sekolah:
        return self._get_rows("/rest/Sekolah", List[Sekolah])[index]
