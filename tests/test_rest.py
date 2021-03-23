import attr
from dapodik.base import BaseDapodik
from dapodik.rest import Agama
from dapodik.rest import Akreditasi
from dapodik.rest import AksesInternet
from dapodik.rest import AlatTransportasi
from dapodik.rest import Bank
from dapodik.rest import BentukLembaga
from dapodik.rest import Biblio
from dapodik.rest import ChildDelete
from dapodik.rest import FasilitasLayanan
from dapodik.rest import Gmd
from dapodik.rest import JadwalPaud
from dapodik.rest import JenisCita
from dapodik.rest import JenisGugus
from dapodik.rest import JenisHapusBuku
from dapodik.rest import JenisHobby
from dapodik.rest import JenisKeluar
from dapodik.rest import JenisLk
from dapodik.rest import JenisPendaftaran
from dapodik.rest import JenisPrasarana
from dapodik.rest import JenisPtk
from dapodik.rest import JenisRombel
from dapodik.rest import JenisSarana
from dapodik.rest import JenisTinggal
from dapodik.rest import JenjangPendidikan
from dapodik.rest import Jurusan
from dapodik.rest import KategoriTk
from dapodik.rest import KeahlianLaboratorium
from dapodik.rest import KebutuhanKhusus
from dapodik.rest import KlasifikasiLembaga
from dapodik.rest import Kurikulum
from dapodik.rest import LembagaPengangkat
from dapodik.rest import MataPelajaran
from dapodik.rest import MstWilayah
from dapodik.rest import PangkatGolongan
from dapodik.rest import Pekerjaan
from dapodik.rest import Penghasilan
from dapodik.rest import RolePengguna
from dapodik.rest import StatusKeaktifanPegawai
from dapodik.rest import StatusKepegawaian
from dapodik.rest import StatusKepemilikanSarpras
from dapodik.rest import SumberAir
from dapodik.rest import SumberDanaSekolah
from dapodik.rest import SumberGaji
from dapodik.rest import SumberListrik
from dapodik.rest import SyncLog
from dapodik.rest import TahunAjaran
from dapodik.rest import TingkatPendidikan
from dapodik.rest import WaktuPenyelenggaraan
from dapodik.rest import BaseRest


def test_base_rest():
    assert issubclass(BaseRest, BaseDapodik)


def test_member():
    assert attr.has(Agama)
    assert attr.has(Akreditasi)
    assert attr.has(AksesInternet)
    assert attr.has(AlatTransportasi)
    assert attr.has(Bank)
    assert attr.has(BentukLembaga)
    assert attr.has(Biblio)
    assert attr.has(ChildDelete)
    assert attr.has(FasilitasLayanan)
    assert attr.has(Gmd)
    assert attr.has(JadwalPaud)
    assert attr.has(JenisCita)
    assert attr.has(JenisGugus)
    assert attr.has(JenisHapusBuku)
    assert attr.has(JenisHobby)
    assert attr.has(JenisKeluar)
    assert attr.has(JenisLk)
    assert attr.has(JenisPendaftaran)
    assert attr.has(JenisPrasarana)
    assert attr.has(JenisPtk)
    assert attr.has(JenisRombel)
    assert attr.has(JenisSarana)
    assert attr.has(JenisTinggal)
    assert attr.has(JenjangPendidikan)
    assert attr.has(Jurusan)
    assert attr.has(KategoriTk)
    assert attr.has(KeahlianLaboratorium)
    assert attr.has(KebutuhanKhusus)
    assert attr.has(KlasifikasiLembaga)
    assert attr.has(Kurikulum)
    assert attr.has(LembagaPengangkat)
    assert attr.has(MataPelajaran)
    assert attr.has(MstWilayah)
    assert attr.has(PangkatGolongan)
    assert attr.has(Pekerjaan)
    assert attr.has(Penghasilan)
    assert attr.has(RolePengguna)
    assert attr.has(StatusKeaktifanPegawai)
    assert attr.has(StatusKepegawaian)
    assert attr.has(StatusKepemilikanSarpras)
    assert attr.has(SumberAir)
    assert attr.has(SumberDanaSekolah)
    assert attr.has(SumberGaji)
    assert attr.has(SumberListrik)
    assert attr.has(SyncLog)
    assert attr.has(TahunAjaran)
    assert attr.has(TingkatPendidikan)
    assert attr.has(WaktuPenyelenggaraan)
