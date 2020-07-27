from dapodik.base import Rest
from .akreditasi import Akreditasi
from .blockgrant import BlockGrant
from .kepanitiaan import Kepanitiaan
from .program_inklusi import ProgramInklusi
from .sanitasi import Sanitasi
from .sekolah import Sekolah
from .sekolah_longitudinal import SekolahLongitudinal
from .sekolah_paud import SekolahPaud
from .yayasan import Yayasan


class BaseSekolah(object):
    sekolah_id: str = None
    _Akreditasi: Akreditasi = None
    _BlockGrant: BlockGrant = None
    _Kepanitiaan: Kepanitiaan = None
    _ProgramInklusi: ProgramInklusi = None
    _Sanitasi: Sanitasi = None
    _Sekolah: Sekolah = None
    _SekolahLongitudinal: SekolahLongitudinal = None
    _SekolahPaud: SekolahPaud = None
    _Yayasan: Yayasan = None

    @property
    def Akreditasi(self) -> Akreditasi:
        if self._Akreditasi:
            return self._Akreditasi
        self._Akreditasi = Rest(
            self, Akreditasi, 'rest/Akreditasi'
        )
        return self._Akreditasi

    @property
    def BlockGrant(self) -> BlockGrant:
        if self._BlockGrant:
            return self._BlockGrant
        self._BlockGrant = Rest(
            self, BlockGrant, 'rest/BlockGrant'
        )
        return self._BlockGrant

    @property
    def Kepanitiaan(self) -> Kepanitiaan:
        if self._Kepanitiaan:
            return self._Kepanitiaan
        self._Kepanitiaan = Rest(
            self, Kepanitiaan, 'rest/Kepanitiaan'
        )
        return self._Kepanitiaan

    @property
    def ProgramInklusi(self) -> ProgramInklusi:
        if self._ProgramInklusi:
            return self._ProgramInklusi
        self._ProgramInklusi = Rest(
            self, ProgramInklusi, 'rest/ProgramInklusi'
        )
        return self._ProgramInklusi

    @property
    def Sanitasi(self) -> Sanitasi:
        if self._Sanitasi:
            return self._Sanitasi
        self._Sanitasi = Rest(
            self, Sanitasi, 'rest/Sanitasi'
        )
        return self._Sanitasi

    @property
    def Sekolah(self) -> Sekolah:
        if self._Sekolah:
            return self._Sekolah
        self._Sekolah = Rest(
            self, Sekolah, 'rest/Sekolah'
        )
        return self._Sekolah

    @property
    def SekolahLongitudinal(self) -> SekolahLongitudinal:
        if self._SekolahLongitudinal:
            return self._SekolahLongitudinal
        self._SekolahLongitudinal = Rest(
            self, SekolahLongitudinal, 'rest/SekolahLongitudinal'
        )
        return self._SekolahLongitudinal

    @property
    def SekolahPaud(self) -> SekolahPaud:
        if self._SekolahPaud:
            return self._SekolahPaud
        self._SekolahPaud = Rest(
            self, SekolahPaud, 'rest/SekolahPaud'
        )
        return self._SekolahPaud

    @property
    def Yayasan(self) -> Yayasan:
        if self._Yayasan:
            return self._Yayasan
        self._Yayasan = Rest(
            self, Yayasan, 'rest/Yayasan'
        )
        return self._Yayasan
