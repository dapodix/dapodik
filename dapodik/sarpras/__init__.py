from dapodik.base import BaseDapodik, Rest
from .alat import Alat
from .alat_dari_blockgrant import AlatDariBlockgrant
from .alat_longitudinal import AlatLongitudinal
from .bangunan import Bangunan
from .bangunan_dari_blockgrant import BangunanDariBlockgrant
from .bangunan_longitudinal import BangunanLongitudinal
from .ruang import Ruang
from .ruang_longitudinal import RuangLongitudinal
from .tanah import Tanah


class BaseSarpras(BaseDapodik):
    _Alat: Rest = None
    _AlatDariBlockgrant: Rest = None
    _AlatLongitudinal: Rest = None
    _Bangunan: Rest = None
    _BangunanDariBlockgrant: Rest = None
    _BangunanLongitudinal: Rest = None
    _Ruang: Rest = None
    _RuangLongitudinal: Rest = None
    _Tanah: Rest = None

    @property
    def Alat(self):
        if self._Alat:
            return self._Alat
        self._Alat = Rest(
            self, Alat, 'rest/Alat'
        )
        return self._Alat

    @property
    def AlatDariBlockgrant(self):
        if self._AlatDariBlockgrant:
            return self._AlatDariBlockgrant
        self._AlatDariBlockgrant = Rest(
            self, AlatDariBlockgrant, 'rest/AlatDariBlockgrant'
        )
        return self._AlatDariBlockgrant

    @property
    def AlatLongitudinal(self):
        if self._AlatLongitudinal:
            return self._AlatLongitudinal
        self._AlatLongitudinal = Rest(
            self, AlatLongitudinal, 'rest/AlatLongitudinal'
        )
        return self._AlatLongitudinal

    @property
    def Bangunan(self):
        if self._Bangunan:
            return self._Bangunan
        self._Bangunan = Rest(
            self, Bangunan, 'rest/Bangunan'
        )
        return self._Bangunan

    @property
    def BangunanDariBlockgrant(self):
        if self._BangunanDariBlockgrant:
            return self._BangunanDariBlockgrant
        self._BangunanDariBlockgrant = Rest(
            self, BangunanDariBlockgrant, 'rest/BangunanDariBlockgrant'
        )
        return self._BangunanDariBlockgrant

    @property
    def BangunanLongitudinal(self):
        if self._BangunanLongitudinal:
            return self._BangunanLongitudinal
        self._BangunanLongitudinal = Rest(
            self, BangunanLongitudinal, 'rest/BangunanLongitudinal'
        )
        return self._BangunanLongitudinal

    @property
    def Ruang(self):
        if self._Ruang:
            return self._Ruang
        self._Ruang = Rest(
            self, Ruang, 'rest/Ruang'
        )
        return self._Ruang

    @property
    def RuangLongitudinal(self):
        if self._RuangLongitudinal:
            return self._RuangLongitudinal
        self._RuangLongitudinal = Rest(
            self, RuangLongitudinal, 'rest/RuangLongitudinal'
        )
        return self._RuangLongitudinal

    @property
    def Tanah(self):
        if self._Tanah:
            return self._Tanah
        self._Tanah = Rest(
            self, Tanah, 'rest/Tanah'
        )
        return self._Tanah
