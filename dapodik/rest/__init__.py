from dapodik.base import BaseDapodik, Rest
from .agama import Agama
from .akreditasi import Akreditasi
from .akses_internet import AksesInternet
from .bank import Bank
from .bentuk_lembaga import BentukLembaga
from .child_delete import ChildDelete
from .fasilitas_layanan import FasilitasLayanan
from .jadwal_paud import JadwalPaud
from .jenis_gugus import JenisGugus
from .jenis_lk import JenisLk
from .kategori_tk import KategoriTk
from .kebutuhan_khusus import KebutuhanKhusus
from .klasifikasi_lembaga import KlasifikasiLembaga
from .mst_wilayah import MstWilayah
from .sumber_air import SumberAir
from .sumber_dana_sekolah import SumberDanaSekolah
from .sumber_listrik import SumberListrik
from .sync_log import SyncLog
from .waktu_penyelenggaraan import WaktuPenyelenggaraan


class BaseRest(BaseDapodik):
    _Agama: Agama = None
    _Akreditasi: Akreditasi = None
    _AksesInternet: AksesInternet = None
    _Bank: Bank = None
    _BentukLembaga: BentukLembaga = None
    _ChildDelete: ChildDelete = None
    _FasilitasLayanan: FasilitasLayanan = None
    _JadwalPaud: JadwalPaud = None
    _JenisGugus: JenisGugus = None
    _JenisLk: JenisLk = None
    _KategoriTk: KategoriTk = None
    _KebutuhanKhusus: KebutuhanKhusus = None
    _KlasifikasiLembaga: KlasifikasiLembaga = None
    _MstWilayah: MstWilayah = None
    _SumberAir: SumberAir = None
    _SumberDanaSekolah: SumberDanaSekolah = None
    _SumberListrik: SumberListrik = None
    _SyncLog: SyncLog = None
    _WaktuPenyelenggaraan: WaktuPenyelenggaraan = None

    @property
    def Agama(self):
        if self._Agama:
            return self._Agama
        self._Agama = Rest(
            self, Agama, 'rest/Agama'
        )
        return self._Agama

    @property
    def Akreditasi(self):
        if self._Akreditasi:
            return self._Akreditasi
        self._Akreditasi = Rest(
            self, Akreditasi, 'rest/Akreditasi'
        )
        return self._Akreditasi

    @property
    def AksesInternet(self):
        if self._AksesInternet:
            return self._AksesInternet
        self._AksesInternet = Rest(
            self, AksesInternet, 'rest/AksesInternet'
        )
        return self._AksesInternet

    @property
    def Bank(self):
        if self._Bank:
            return self._Bank
        self._Bank = Rest(
            self, Bank, 'rest/Bank'
        )
        return self._Bank

    @property
    def BentukLembaga(self):
        if self._BentukLembaga:
            return self._BentukLembaga
        self._BentukLembaga = Rest(
            self, BentukLembaga, 'rest/BentukLembaga'
        )
        return self._BentukLembaga

    @property
    def ChildDelete(self):
        if self._ChildDelete:
            return self._ChildDelete
        self._ChildDelete = Rest(
            self, ChildDelete, 'rest/ChildDelete'
        )
        return self._ChildDelete

    @property
    def FasilitasLayanan(self):
        if self._FasilitasLayanan:
            return self._FasilitasLayanan
        self._FasilitasLayanan = Rest(
            self, FasilitasLayanan, 'rest/FasilitasLayanan'
        )
        return self._FasilitasLayanan

    @property
    def JadwalPaud(self):
        if self._JadwalPaud:
            return self._JadwalPaud
        self._JadwalPaud = Rest(
            self, JadwalPaud, 'rest/JadwalPaud'
        )
        return self._JadwalPaud

    @property
    def JenisGugus(self):
        if self._JenisGugus:
            return self._JenisGugus
        self._JenisGugus = Rest(
            self, JenisGugus, 'rest/JenisGugus'
        )
        return self._JenisGugus

    @property
    def JenisLk(self):
        if self._JenisLk:
            return self._JenisLk
        self._JenisLk = Rest(
            self, JenisLk, 'rest/JenisLk'
        )
        return self._JenisLk

    @property
    def KategoriTk(self):
        if self._KategoriTk:
            return self._KategoriTk
        self._KategoriTk = Rest(
            self, KategoriTk, 'rest/KategoriTk'
        )
        return self._KategoriTk

    @property
    def KebutuhanKhusus(self):
        if self._KebutuhanKhusus:
            return self._KebutuhanKhusus
        self._KebutuhanKhusus = Rest(
            self, KebutuhanKhusus, 'rest/KebutuhanKhusus'
        )
        return self._KebutuhanKhusus

    @property
    def KlasifikasiLembaga(self):
        if self._KlasifikasiLembaga:
            return self._KlasifikasiLembaga
        self._KlasifikasiLembaga = Rest(
            self, KlasifikasiLembaga, 'rest/KlasifikasiLembaga'
        )
        return self._KlasifikasiLembaga

    @property
    def MstWilayah(self):
        if self._MstWilayah:
            return self._MstWilayah
        self._MstWilayah = Rest(
            self, MstWilayah, 'rest/MstWilayah'
        )
        return self._MstWilayah

    @property
    def SumberAir(self):
        if self._SumberAir:
            return self._SumberAir
        self._SumberAir = Rest(
            self, SumberAir, 'rest/SumberAir'
        )
        return self._SumberAir

    @property
    def SumberDanaSekolah(self):
        if self._SumberDanaSekolah:
            return self._SumberDanaSekolah
        self._SumberDanaSekolah = Rest(
            self, SumberDanaSekolah, 'rest/SumberDanaSekolah'
        )
        return self._SumberDanaSekolah

    @property
    def SumberListrik(self):
        if self._SumberListrik:
            return self._SumberListrik
        self._SumberListrik = Rest(
            self, SumberListrik, 'rest/SumberListrik'
        )
        return self._SumberListrik

    @property
    def SyncLog(self):
        if self._SyncLog:
            return self._SyncLog
        self._SyncLog = Rest(
            self, SyncLog, 'rest/SyncLog'
        )
        return self._SyncLog

    @property
    def WaktuPenyelenggaraan(self):
        if self._WaktuPenyelenggaraan:
            return self._WaktuPenyelenggaraan
        self._WaktuPenyelenggaraan = Rest(
            self, WaktuPenyelenggaraan, 'rest/WaktuPenyelenggaraan'
        )
        return self._WaktuPenyelenggaraan
