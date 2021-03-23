from typing import List

from dapodik.base import BaseDapodik

from . import AlatDariBlockgrant
from . import AlatLongitudinal
from . import Alat
from . import AngkutanDariBlockgrant
from . import Angkutan
from . import BangunanDariBlockgrant
from . import BangunanLongitudinal
from . import Bangunan
from . import BukuLongitudinal
from . import Buku
from . import RuangLongitudinal
from . import Ruang
from . import TanahDariBlockgrant
from . import TanahLongitudinal
from . import Tanah


class BaseSarpras(BaseDapodik):
    def alat_dari_blockgrant(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[AlatDariBlockgrant]:
        return self._get_rest(
            "AlatDariBlockgrant", List[AlatDariBlockgrant], page, start, limit
        )

    def alat_longitudinal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[AlatLongitudinal]:
        return self._get_rest(
            "AlatLongitudinal", List[AlatLongitudinal], page, start, limit
        )

    def alat(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Alat]:
        return self._get_rest("Alat", List[Alat], page, start, limit)

    def angkutan_dari_blockgrant(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[AngkutanDariBlockgrant]:
        return self._get_rest(
            "AngkutanDariBlockgrant", List[AngkutanDariBlockgrant], page, start, limit
        )

    def angkutan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Angkutan]:
        return self._get_rest("Angkutan", List[Angkutan], page, start, limit)

    def bangunan_dari_blockgrant(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[BangunanDariBlockgrant]:
        return self._get_rest(
            "BangunanDariBlockgrant", List[BangunanDariBlockgrant], page, start, limit
        )

    def bangunan_longitudinal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[BangunanLongitudinal]:
        return self._get_rest(
            "BangunanLongitudinal", List[BangunanLongitudinal], page, start, limit
        )

    def bangunan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Bangunan]:
        return self._get_rest("Bangunan", List[Bangunan], page, start, limit)

    def buku_longitudinal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[BukuLongitudinal]:
        return self._get_rest(
            "BukuLongitudinal", List[BukuLongitudinal], page, start, limit
        )

    def buku(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Buku]:
        return self._get_rest("Buku", List[Buku], page, start, limit)

    def ruang_longitudinal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[RuangLongitudinal]:
        return self._get_rest(
            "RuangLongitudinal", List[RuangLongitudinal], page, start, limit
        )

    def ruang(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Ruang]:
        return self._get_rest("Ruang", List[Ruang], page, start, limit)

    def tanah_dari_blockgrant(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[TanahDariBlockgrant]:
        return self._get_rest(
            "TanahDariBlockgrant", List[TanahDariBlockgrant], page, start, limit
        )

    def tanah_longitudinal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[TanahLongitudinal]:
        return self._get_rest(
            "TanahLongitudinal", List[TanahLongitudinal], page, start, limit
        )

    def tanah(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Tanah]:
        return self._get_rest("Tanah", List[Tanah], page, start, limit)
