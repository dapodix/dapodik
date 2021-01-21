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
    __all__ = __fetch__
    pass
