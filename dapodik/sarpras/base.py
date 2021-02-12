from typing import List

from dapodik.base import BaseDapodik
from . import (
    AlatDariBlockgrant,
    AlatLongitudinal,
    Alat,
    AngkutanDariBlockgrant,
    Angkutan,
    BangunanDariBlockgrant,
    BangunanLongitudinal,
    Bangunan,
    BukuLongitudinal,
    Buku,
    RuangLongitudinal,
    Ruang,
    TanahDariBlockgrant,
    TanahLongitudinal,
    Tanah,
)

__fetch__ = (
    AlatDariBlockgrant,
    AlatLongitudinal,
    Alat,
    AngkutanDariBlockgrant,
    Angkutan,
    BangunanDariBlockgrant,
    BangunanLongitudinal,
    Bangunan,
    BukuLongitudinal,
    Buku,
    RuangLongitudinal,
    Ruang,
    TanahDariBlockgrant,
    TanahLongitudinal,
    Tanah,
)


class BaseSarpras(BaseDapodik):
    def __add_sarpras__(self) -> None:
        self.__all__ += __fetch__

    def alat_dari_blockgrant(self) -> List[AlatDariBlockgrant]:
        res = self._get_rest("AlatDariBlockgrant")
        return self._fr(AlatDariBlockgrant, res.json())

    def alat_longitudinal(self) -> List[AlatLongitudinal]:
        res = self._get_rest("AlatLongitudinal")
        return self._fr(AlatLongitudinal, res.json())

    def alat(self) -> List[Alat]:
        res = self._get_rest("Alat")
        return self._fr(Alat, res.json())

    def angkutan_dari_blockgrant(self) -> List[AngkutanDariBlockgrant]:
        res = self._get_rest("AngkutanDariBlockgrant")
        return self._fr(AngkutanDariBlockgrant, res.json())

    def angkutan(self) -> List[Angkutan]:
        res = self._get_rest("Angkutan")
        return self._fr(Angkutan, res.json())

    def bangunan_dari_blockgrant(self) -> List[BangunanDariBlockgrant]:
        res = self._get_rest("BangunanDariBlockgrant")
        return self._fr(BangunanDariBlockgrant, res.json())

    def bangunan_longitudinal(self) -> List[BangunanLongitudinal]:
        res = self._get_rest("BangunanLongitudinal")
        return self._fr(BangunanLongitudinal, res.json())

    def bangunan(self) -> List[Bangunan]:
        res = self._get_rest("Bangunan")
        return self._fr(Bangunan, res.json())

    def buku_longitudinal(self) -> List[BukuLongitudinal]:
        res = self._get_rest("BukuLongitudinal")
        return self._fr(BukuLongitudinal, res.json())

    def buku(self) -> List[Buku]:
        res = self._get_rest("Buku")
        return self._fr(Buku, res.json())

    def ruang_longitudinal(self) -> List[RuangLongitudinal]:
        res = self._get_rest("RuangLongitudinal")
        return self._fr(RuangLongitudinal, res.json())

    def ruang(self) -> List[Ruang]:
        res = self._get_rest("Ruang")
        return self._fr(Ruang, res.json())

    def tanah_dari_blockgrant(self) -> List[TanahDariBlockgrant]:
        res = self._get_rest("TanahDariBlockgrant")
        return self._fr(TanahDariBlockgrant, res.json())

    def tanah_longitudinal(self) -> List[TanahLongitudinal]:
        res = self._get_rest("TanahLongitudinal")
        return self._fr(TanahLongitudinal, res.json())

    def tanah(self) -> List[Tanah]:
        res = self._get_rest("Tanah")
        return self._fr(Tanah, res.json())
