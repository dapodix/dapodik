from dapodik.base import BaseDapodik, Rest
from .agama import Agama
from .akreditasi import Akreditasi
from .akses_internet import AksesInternet
from .alat_transportasi import AlatTransportasi
from .bank import Bank
from .bentuk_lembaga import BentukLembaga
from .child_delete import ChildDelete
from .fasilitas_layanan import FasilitasLayanan
from .gmd import Gmd
from .jadwal_paud import JadwalPaud
from .jenis_gugus import JenisGugus
from .jenis_hapus_buku import JenisHapusBuku
from .jenis_keluar import JenisKeluar
from .jenis_lk import JenisLk
from .jenis_pendaftaran import JenisPendaftaran
from .jenis_prasarana import JenisPrasarana
from .jenis_sarana import JenisSarana
from .jenis_tinggal import JenisTinggal
from .jenjang_pendidikan import JenjangPendidikan
from .kategori_tk import KategoriTk
from .kebutuhan_khusus import KebutuhanKhusus
from .klasifikasi_lembaga import KlasifikasiLembaga
from .lembaga_pengangkat import LembagaPengangkat
from .mst_wilayah import MstWilayah
from .pangkat_golongan import PangkatGolongan
from .pekerjaan import Pekerjaan
from .pengguna import Pengguna
from .penghasilan import Penghasilan
from .role_pengguna import RolePengguna
from .status_keaktifan_pegawai import StatusKeaktifanPegawai
from .status_kepegawaian import StatusKepegawaian
from .status_kepemilikan_sarpras import StatusKepemilikanSarpras
from .sumber_air import SumberAir
from .sumber_dana_sekolah import SumberDanaSekolah
from .sumber_gaji import SumberGaji
from .sumber_listrik import SumberListrik
from .sync_log import SyncLog
from .tingkat_pendidikan import TingkatPendidikan
from .waktu_penyelenggaraan import WaktuPenyelenggaraan


class BaseRest(BaseDapodik):
    def register_rest(self) -> bool:
        try:
            self.Agama = Rest(
                self, Agama, 'rest/Agama'
            )
            self.Akreditasi = Rest(
                self, Akreditasi, 'rest/Akreditasi'
            )
            self.AksesInternet = Rest(
                self, AksesInternet, 'rest/AksesInternet'
            )
            self.AlatTransportasi = Rest(
                self, AlatTransportasi, 'rest/AlatTransportasi'
            )
            self.Bank = Rest(
                self, Bank, 'rest/Bank'
            )
            self.BentukLembaga = Rest(
                self, BentukLembaga, 'rest/BentukLembaga'
            )
            self.ChildDelete = Rest(
                self, ChildDelete, 'rest/ChildDelete'
            )
            self.FasilitasLayanan = Rest(
                self, FasilitasLayanan, 'rest/FasilitasLayanan'
            )
            self.Gmd = Rest(
                self, Gmd, 'rest/Gmd'
            )
            self.JadwalPaud = Rest(
                self, JadwalPaud, 'rest/JadwalPaud'
            )
            self.JenisGugus = Rest(
                self, JenisGugus, 'rest/JenisGugus'
            )
            self.JenisHapusBuku = Rest(
                self, JenisHapusBuku, 'rest/JenisHapusBuku'
            )
            self.JenisKeluar = Rest(
                self, JenisKeluar, 'rest/JenisKeluar'
            )
            self.JenisLk = Rest(
                self, JenisLk, 'rest/JenisLk'
            )
            self.JenisPendaftaran = Rest(
                self, JenisPendaftaran, 'rest/JenisPendaftaran'
            )
            self.JenisPrasarana = Rest(
                self, JenisPrasarana, 'rest/JenisPrasarana'
            )
            self.JenisSarana = Rest(
                self, JenisSarana, 'rest/JenisSarana'
            )
            self.JenisTinggal = Rest(
                self, JenisTinggal, 'rest/JenisTinggal'
            )
            self.JenjangPendidikan = Rest(
                self, JenjangPendidikan, 'rest/JenjangPendidikan'
            )
            self.KategoriTk = Rest(
                self, KategoriTk, 'rest/KategoriTk'
            )
            self.KebutuhanKhusus = Rest(
                self, KebutuhanKhusus, 'rest/KebutuhanKhusus'
            )
            self.KlasifikasiLembaga = Rest(
                self, KlasifikasiLembaga, 'rest/KlasifikasiLembaga'
            )
            self.LembagaPengangkat = Rest(
                self, LembagaPengangkat, 'rest/LembagaPengangkat'
            )
            self.MstWilayah = Rest(
                self, MstWilayah, 'rest/MstWilayah'
            )
            self.PangkatGolongan = Rest(
                self, PangkatGolongan, 'rest/PangkatGolongan'
            )
            self.Pekerjaan = Rest(
                self, Pekerjaan, 'rest/Pekerjaan'
            )
            self.Pengguna = Rest(
                self, Pengguna, 'rest/Pengguna'
            )
            self.Penghasilan = Rest(
                self, Penghasilan, 'rest/Penghasilan'
            )
            self.RolePengguna = Rest(
                self, RolePengguna, 'rest/RolePengguna'
            )
            self.StatusKeaktifanPegawai = Rest(
                self, StatusKeaktifanPegawai, 'rest/StatusKeaktifanPegawai'
            )
            self.StatusKepegawaian = Rest(
                self, StatusKepegawaian, 'rest/StatusKepegawaian'
            )
            self.StatusKepemilikanSarpras = Rest(
                self, StatusKepemilikanSarpras, 'rest/StatusKepemilikanSarpras'
            )
            self.SumberAir = Rest(
                self, SumberAir, 'rest/SumberAir'
            )
            self.SumberDanaSekolah = Rest(
                self, SumberDanaSekolah, 'rest/SumberDanaSekolah'
            )
            self.SumberGaji = Rest(
                self, SumberGaji, 'rest/SumberGaji'
            )
            self.SumberListrik = Rest(
                self, SumberListrik, 'rest/SumberListrik'
            )
            self.SyncLog = Rest(
                self, SyncLog, 'rest/SyncLog'
            )
            self.TingkatPendidikan = Rest(
                self, TingkatPendidikan, 'rest/TingkatPendidikan'
            )
            self.WaktuPenyelenggaraan = Rest(
                self, WaktuPenyelenggaraan, 'rest/WaktuPenyelenggaraan'
            )
            self.logger.debug('Berhasil memulai rest')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
