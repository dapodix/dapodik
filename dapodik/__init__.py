#!/usr/bin/env python

from .base.base import BaseDapodik
from .base.dapodik_object import DapodikObject
from .base.rest import Rest
from .base.results import Results

from .rest.agama import Agama
from .rest.akreditasi import Akreditasi
from .rest.akses_internet import AksesInternet
from .rest.alat_transportasi import AlatTransportasi
from .rest.bank import Bank
from .rest.bentuk_lembaga import BentukLembaga
from .rest.child_delete import ChildDelete
from .rest.fasilitas_layanan import FasilitasLayanan
from .rest.gmd import Gmd
from .rest.jadwal_paud import JadwalPaud
from .rest.jenis_gugus import JenisGugus
from .rest.jenis_hapus_buku import JenisHapusBuku
from .rest.jenis_keluar import JenisKeluar
from .rest.jenis_lk import JenisLk
from .rest.jenis_pendaftaran import JenisPendaftaran
from .rest.jenis_prasarana import JenisPrasarana
from .rest.jenis_sarana import JenisSarana
from .rest.jenis_tinggal import JenisTinggal
from .rest.jenjang_pendidikan import JenjangPendidikan
from .rest.kategori_tk import KategoriTk
from .rest.kebutuhan_khusus import KebutuhanKhusus
from .rest.klasifikasi_lembaga import KlasifikasiLembaga
from .rest.lembaga_pengangkat import LembagaPengangkat
from .rest.mst_wilayah import MstWilayah
from .rest.pangkat_golongan import PangkatGolongan
from .rest.pekerjaan import Pekerjaan
from .rest.pengguna import Pengguna
from .rest.penghasilan import Penghasilan
from .rest.role_pengguna import RolePengguna
from .rest.status_keaktifan_pegawai import StatusKeaktifanPegawai
from .rest.status_kepegawaian import StatusKepegawaian
from .rest.status_kepemilikan_sarpras import StatusKepemilikanSarpras
from .rest.sumber_air import SumberAir
from .rest.sumber_dana_sekolah import SumberDanaSekolah
from .rest.sumber_gaji import SumberGaji
from .rest.sumber_listrik import SumberListrik
from .rest.sync_log import SyncLog
from .rest.tingkat_pendidikan import TingkatPendidikan
from .rest.waktu_penyelenggaraan import WaktuPenyelenggaraan

from .peserta_didik.peserta_didik import PesertaDidik
from .peserta_didik.peserta_didik_baru import PesertaDidikBaru
from .peserta_didik.registrasi_peserta_didik import RegistrasiPesertaDidik

from .ptk.ptk import Ptk
from .ptk.ptk_terdaftar import PtkTerdaftar

from .rombongan_belajar.pembelajaran import Pembelajaran
from .rombongan_belajar.rombongan_belajar import RombonganBelajar

from .sarpras.alat import Alat
from .sarpras.alat_dari_blockgrant import AlatDariBlockgrant
from .sarpras.alat_longitudinal import AlatLongitudinal
from .sarpras.bangunan import Bangunan
from .sarpras.bangunan_dari_blockgrant import BangunanDariBlockgrant
from .sarpras.bangunan_longitudinal import BangunanLongitudinal
from .sarpras.ruang import Ruang
from .sarpras.ruang_longitudinal import RuangLongitudinal
from .sarpras.tanah import Tanah

from .sekolah.akreditasi_sp import AkreditasiSp
from .sekolah.blockgrant import BlockGrant
from .sekolah.kepanitiaan import Kepanitiaan
from .sekolah.program_inklusi import ProgramInklusi
from .sekolah.sanitasi import Sanitasi
from .sekolah.sekolah import Sekolah
from .sekolah.sekolah_longitudinal import SekolahLongitudinal
from .sekolah.sekolah_paud import SekolahPaud
from .sekolah.yayasan import Yayasan

from .peserta_didik import BasePesertaDidik
from .ptk import BasePtk
from .rest import BaseRest
from .rombongan_belajar import BaseRombonganBelajar
from .sarpras import BaseSarpras
from .sekolah import BaseSekolah
from .dapodik import Dapodik

from .config import BASE_URL, DOMAIN, SEMESTER_ID, USER_AGENT  # NOQA
from .version import __version__, __dapodik_version__  # NOQA

__author__ = 'hexatester (Habib Rohman)'

__all__ = [
    'Agama', 'Akreditasi', 'AkreditasiSp', 'AksesInternet', 'Alat',
    'AlatDariBlockgrant', 'AlatLongitudinal', 'AlatTransportasi', 'Bangunan',
    'BangunanDariBlockgrant', 'BangunanLongitudinal', 'Bank', 'BaseDapodik',
    'BasePesertaDidik', 'BasePtk', 'BaseRest', 'BaseRombonganBelajar',
    'BaseSarpras', 'BaseSekolah', 'BentukLembaga', 'BlockGrant', 'ChildDelete',
    'Dapodik', 'DapodikObject', 'FasilitasLayanan', 'Gmd', 'JadwalPaud',
    'JenisGugus', 'JenisHapusBuku', 'JenisKeluar', 'JenisLk',
    'JenisPendaftaran', 'JenisPrasarana', 'JenisSarana', 'JenisTinggal',
    'JenjangPendidikan', 'KategoriTk', 'KebutuhanKhusus', 'Kepanitiaan',
    'KlasifikasiLembaga', 'LembagaPengangkat', 'MstWilayah', 'PangkatGolongan',
    'Pekerjaan', 'Pembelajaran', 'Pengguna', 'Penghasilan', 'PesertaDidik',
    'PesertaDidikBaru', 'ProgramInklusi', 'Ptk', 'PtkTerdaftar',
    'RegistrasiPesertaDidik', 'Rest', 'Results', 'RolePengguna',
    'RombonganBelajar', 'Ruang', 'RuangLongitudinal', 'Sanitasi', 'Sekolah',
    'SekolahLongitudinal', 'SekolahPaud', 'StatusKeaktifanPegawai',
    'StatusKepegawaian', 'StatusKepemilikanSarpras', 'SumberAir',
    'SumberDanaSekolah', 'SumberGaji', 'SumberListrik', 'SyncLog', 'Tanah',
    'TingkatPendidikan', 'WaktuPenyelenggaraan', 'Yayasan'
]
