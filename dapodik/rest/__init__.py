from dapodik.base import BaseDapodik, Rest
from .agama import Agama
from .akreditasi import Akreditasi
from .akses_internet import AksesInternet
from .bank import Bank
from .bentuk_lembaga import BentukLembaga
from .child_delete import ChildDelete
from .fasilitas_layanan import FasilitasLayanan
from .gmd import Gmd
from .jadwal_paud import JadwalPaud
from .jenis_gugus import JenisGugus
from .jenis_hapus_buku import JenisHapusBuku
from .jenis_lk import JenisLk
from .jenis_prasarana import JenisPrasarana
from .jenis_sarana import JenisSarana
from .kategori_tk import KategoriTk
from .kebutuhan_khusus import KebutuhanKhusus
from .klasifikasi_lembaga import KlasifikasiLembaga
from .mst_wilayah import MstWilayah
from .status_kepemilikan_sarpras import StatusKepemilikanSarpras
from .sumber_air import SumberAir
from .sumber_dana_sekolah import SumberDanaSekolah
from .sumber_listrik import SumberListrik
from .sync_log import SyncLog
from .tingkat_pendidikan import TingkatPendidikan
from .waktu_penyelenggaraan import WaktuPenyelenggaraan


class BaseRest(BaseDapodik):
    _Agama: Agama = None
    _Akreditasi: Akreditasi = None
    _AksesInternet: AksesInternet = None
    _Bank: Bank = None
    _BentukLembaga: BentukLembaga = None
    _ChildDelete: ChildDelete = None
    _FasilitasLayanan: FasilitasLayanan = None
    _Gmd: Gmd = None
    _JadwalPaud: JadwalPaud = None
    _JenisGugus: JenisGugus = None
    _JenisHapusBuku: JenisHapusBuku = None
    _JenisLk: JenisLk = None
    _JenisPrasarana: JenisPrasarana = None
    _JenisSarana: JenisSarana = None
    _KategoriTk: KategoriTk = None
    _KebutuhanKhusus: KebutuhanKhusus = None
    _KlasifikasiLembaga: KlasifikasiLembaga = None
    _MstWilayah: MstWilayah = None
    _StatusKepemilikanSarpras: StatusKepemilikanSarpras = None
    _SumberAir: SumberAir = None
    _SumberDanaSekolah: SumberDanaSekolah = None
    _SumberListrik: SumberListrik = None
    _SyncLog: SyncLog = None
    _TingkatPendidikan: TingkatPendidikan = None
    _WaktuPenyelenggaraan: WaktuPenyelenggaraan = None

    @property
    def Agama(self) -> Rest:
        if self._Agama:
            return self._Agama
        self._Agama = Rest(
            sef, Agama, 'rest/Agama', edit=False
        )
        return self._Agama

    @property
    def Akreditasi(self) -> Rest:
        if self._Akreditasi:
            return self._Akreditasi
        self._Akreditasi = Rest(
            sef, Akreditasi, 'rest/Akreditasi', edit=False
        )
        return self._Akreditasi

    @property
    def AksesInternet(self) -> Rest:
        if self._AksesInternet:
            return self._AksesInternet
        self._AksesInternet = Rest(
            sef, AksesInternet, 'rest/AksesInternet', edit=False
        )
        return self._AksesInternet

    @property
    def Bank(self) -> Rest:
        if self._Bank:
            return self._Bank
        self._Bank = Rest(
            sef, Bank, 'rest/Bank', edit=False
        )
        return self._Bank

    @property
    def BentukLembaga(self) -> Rest:
        if self._BentukLembaga:
            return self._BentukLembaga
        self._BentukLembaga = Rest(
            sef, BentukLembaga, 'rest/BentukLembaga', edit=False
        )
        return self._BentukLembaga

    @property
    def ChildDelete(self) -> Rest:
        if self._ChildDelete:
            return self._ChildDelete
        self._ChildDelete = Rest(
            sef, ChildDelete, 'rest/ChildDelete', edit=False
        )
        return self._ChildDelete

    @property
    def FasilitasLayanan(self) -> Rest:
        if self._FasilitasLayanan:
            return self._FasilitasLayanan
        self._FasilitasLayanan = Rest(
            sef, FasilitasLayanan, 'rest/FasilitasLayanan', edit=False
        )
        return self._FasilitasLayanan

    @property
    def Gmd(self) -> Rest:
        if self._Gmd:
            return self._Gmd
        self._Gmd = Rest(
            sef, Gmd, 'rest/Gmd', edit=False
        )
        return self._Gmd

    @property
    def JadwalPaud(self) -> Rest:
        if self._JadwalPaud:
            return self._JadwalPaud
        self._JadwalPaud = Rest(
            sef, JadwalPaud, 'rest/JadwalPaud', edit=False
        )
        return self._JadwalPaud

    @property
    def JenisGugus(self) -> Rest:
        if self._JenisGugus:
            return self._JenisGugus
        self._JenisGugus = Rest(
            sef, JenisGugus, 'rest/JenisGugus', edit=False
        )
        return self._JenisGugus

    @property
    def JenisHapusBuku(self) -> Rest:
        if self._JenisHapusBuku:
            return self._JenisHapusBuku
        self._JenisHapusBuku = Rest(
            sef, JenisHapusBuku, 'rest/JenisHapusBuku', edit=False
        )
        return self._JenisHapusBuku

    @property
    def JenisLk(self) -> Rest:
        if self._JenisLk:
            return self._JenisLk
        self._JenisLk = Rest(
            sef, JenisLk, 'rest/JenisLk', edit=False
        )
        return self._JenisLk

    @property
    def JenisPrasarana(self) -> Rest:
        if self._JenisPrasarana:
            return self._JenisPrasarana
        self._JenisPrasarana = Rest(
            sef, JenisPrasarana, 'rest/JenisPrasarana', edit=False
        )
        return self._JenisPrasarana

    @property
    def JenisSarana(self) -> Rest:
        if self._JenisSarana:
            return self._JenisSarana
        self._JenisSarana = Rest(
            sef, JenisSarana, 'rest/JenisSarana', edit=False
        )
        return self._JenisSarana

    @property
    def KategoriTk(self) -> Rest:
        if self._KategoriTk:
            return self._KategoriTk
        self._KategoriTk = Rest(
            sef, KategoriTk, 'rest/KategoriTk', edit=False
        )
        return self._KategoriTk

    @property
    def KebutuhanKhusus(self) -> Rest:
        if self._KebutuhanKhusus:
            return self._KebutuhanKhusus
        self._KebutuhanKhusus = Rest(
            sef, KebutuhanKhusus, 'rest/KebutuhanKhusus', edit=False
        )
        return self._KebutuhanKhusus

    @property
    def KlasifikasiLembaga(self) -> Rest:
        if self._KlasifikasiLembaga:
            return self._KlasifikasiLembaga
        self._KlasifikasiLembaga = Rest(
            sef, KlasifikasiLembaga, 'rest/KlasifikasiLembaga', edit=False
        )
        return self._KlasifikasiLembaga

    @property
    def MstWilayah(self) -> Rest:
        if self._MstWilayah:
            return self._MstWilayah
        self._MstWilayah = Rest(
            sef, MstWilayah, 'rest/MstWilayah', edit=False
        )
        return self._MstWilayah

    @property
    def StatusKepemilikanSarpras(self) -> Rest:
        if self._StatusKepemilikanSarpras:
            return self._StatusKepemilikanSarpras
        self._StatusKepemilikanSarpras = Rest(
            sef, StatusKepemilikanSarpras, 'rest/StatusKepemilikanSarpras', edit=False
        )
        return self._StatusKepemilikanSarpras

    @property
    def SumberAir(self) -> Rest:
        if self._SumberAir:
            return self._SumberAir
        self._SumberAir = Rest(
            sef, SumberAir, 'rest/SumberAir', edit=False
        )
        return self._SumberAir

    @property
    def SumberDanaSekolah(self) -> Rest:
        if self._SumberDanaSekolah:
            return self._SumberDanaSekolah
        self._SumberDanaSekolah = Rest(
            sef, SumberDanaSekolah, 'rest/SumberDanaSekolah', edit=False
        )
        return self._SumberDanaSekolah

    @property
    def SumberListrik(self) -> Rest:
        if self._SumberListrik:
            return self._SumberListrik
        self._SumberListrik = Rest(
            sef, SumberListrik, 'rest/SumberListrik', edit=False
        )
        return self._SumberListrik

    @property
    def SyncLog(self) -> Rest:
        if self._SyncLog:
            return self._SyncLog
        self._SyncLog = Rest(
            sef, SyncLog, 'rest/SyncLog', edit=False
        )
        return self._SyncLog

    @property
    def TingkatPendidikan(self) -> Rest:
        if self._TingkatPendidikan:
            return self._TingkatPendidikan
        self._TingkatPendidikan = Rest(
            sef, TingkatPendidikan, 'rest/TingkatPendidikan', edit=False
        )
        return self._TingkatPendidikan

    @property
    def WaktuPenyelenggaraan(self) -> Rest:
        if self._WaktuPenyelenggaraan:
            return self._WaktuPenyelenggaraan
        self._WaktuPenyelenggaraan = Rest(
            sef, WaktuPenyelenggaraan, 'rest/WaktuPenyelenggaraan', edit=False
        )
        return self._WaktuPenyelenggaraan
