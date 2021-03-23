from typing import List

from dapodik.base import BaseDapodik

from . import Agama
from . import Akreditasi
from . import AksesInternet
from . import AlatTransportasi
from . import Bank
from . import BentukLembaga
from . import Biblio
from . import FasilitasLayanan
from . import Gmd
from . import JadwalPaud
from . import JenisCita
from . import JenisGugus
from . import JenisHapusBuku
from . import JenisHobby
from . import JenisKeluar
from . import JenisLk
from . import JenisPendaftaran
from . import JenisPrasarana
from . import JenisPtk
from . import JenisRombel
from . import JenisSarana
from . import JenisTinggal
from . import JenjangPendidikan
from . import Jurusan
from . import KategoriTk
from . import KeahlianLaboratorium
from . import KebutuhanKhusus
from . import KlasifikasiLembaga
from . import Kurikulum
from . import LembagaPengangkat
from . import MataPelajaran
from . import MstWilayah
from . import PangkatGolongan
from . import Pekerjaan
from . import Penghasilan
from . import RolePengguna
from . import StatusKeaktifanPegawai
from . import StatusKepegawaian
from . import StatusKepemilikanSarpras
from . import SumberAir
from . import SumberDanaSekolah
from . import SumberGaji
from . import SumberListrik
from . import SyncLog
from . import TahunAjaran
from . import TingkatPendidikan
from . import WaktuPenyelenggaraan


class BaseRest(BaseDapodik):
    def agama(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Agama]:
        return self._get_rest("Agama", List[Agama], page, start, limit)

    def akreditasi(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Akreditasi]:
        return self._get_rest("Akreditasi", List[Akreditasi], page, start, limit)

    def akses_internet(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[AksesInternet]:
        return self._get_rest("AksesInternet", List[AksesInternet], page, start, limit)

    def alat_transportasi(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[AlatTransportasi]:
        return self._get_rest(
            "AlatTransportasi", List[AlatTransportasi], page, start, limit
        )

    def bank(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Bank]:
        return self._get_rest("Bank", List[Bank], page, start, limit)

    def bentuk_lembaga(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[BentukLembaga]:
        return self._get_rest("BentukLembaga", List[BentukLembaga], page, start, limit)

    def biblio(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Biblio]:
        return self._get_rest("Biblio", List[Biblio], page, start, limit)

    def fasilitas_layanan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[FasilitasLayanan]:
        return self._get_rest(
            "FasilitasLayanan", List[FasilitasLayanan], page, start, limit
        )

    def gmd(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Gmd]:
        return self._get_rest("Gmd", List[Gmd], page, start, limit)

    def jadwal_paud(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JadwalPaud]:
        return self._get_rest("JadwalPaud", List[JadwalPaud], page, start, limit)

    def jenis_cita(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisCita]:
        return self._get_rest("JenisCita", List[JenisCita], page, start, limit)

    def jenis_gugus(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisGugus]:
        return self._get_rest("JenisGugus", List[JenisGugus], page, start, limit)

    def jenis_hapus_buku(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisHapusBuku]:
        return self._get_rest(
            "JenisHapusBuku", List[JenisHapusBuku], page, start, limit
        )

    def jenis_hobby(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisHobby]:
        return self._get_rest("JenisHobby", List[JenisHobby], page, start, limit)

    def jenis_keluar(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisKeluar]:
        return self._get_rest("JenisKeluar", List[JenisKeluar], page, start, limit)

    def jenis_lk(self, page: int = 1, start: int = 0, limit: int = 50) -> List[JenisLk]:
        return self._get_rest("JenisLk", List[JenisLk], page, start, limit)

    def jenis_pendaftaran(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisPendaftaran]:
        return self._get_rest(
            "JenisPendaftaran", List[JenisPendaftaran], page, start, limit
        )

    def jenis_prasarana(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisPrasarana]:
        return self._get_rest(
            "JenisPrasarana", List[JenisPrasarana], page, start, limit
        )

    def jenis_ptk(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisPtk]:
        return self._get_rest("JenisPtk", List[JenisPtk], page, start, limit)

    def jenis_rombel(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisRombel]:
        return self._get_rest("JenisRombel", List[JenisRombel], page, start, limit)

    def jenis_sarana(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisSarana]:
        return self._get_rest("JenisSarana", List[JenisSarana], page, start, limit)

    def jenis_tinggal(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisTinggal]:
        return self._get_rest("JenisTinggal", List[JenisTinggal], page, start, limit)

    def jenjang_pendidikan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenjangPendidikan]:
        return self._get_rest(
            "JenjangPendidikan", List[JenjangPendidikan], page, start, limit
        )

    def jurusan(self, page: int = 1, start: int = 0, limit: int = 50) -> List[Jurusan]:
        return self._get_rest("Jurusan", List[Jurusan], page, start, limit)

    def kategori_tk(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[KategoriTk]:
        return self._get_rest("KategoriTk", List[KategoriTk], page, start, limit)

    def keahlian_laboratorium(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[KeahlianLaboratorium]:
        return self._get_rest(
            "KeahlianLaboratorium", List[KeahlianLaboratorium], page, start, limit
        )

    def kebutuhan_khusus(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[KebutuhanKhusus]:
        return self._get_rest(
            "KebutuhanKhusus", List[KebutuhanKhusus], page, start, limit
        )

    def klasifikasi_lembaga(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[KlasifikasiLembaga]:
        return self._get_rest(
            "KlasifikasiLembaga", List[KlasifikasiLembaga], page, start, limit
        )

    def kurikulum(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Kurikulum]:
        return self._get_rest("Kurikulum", List[Kurikulum], page, start, limit)

    def lembaga_pengangkat(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[LembagaPengangkat]:
        return self._get_rest(
            "LembagaPengangkat", List[LembagaPengangkat], page, start, limit
        )

    def mata_pelajaran(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[MataPelajaran]:
        return self._get_rest("MataPelajaran", List[MataPelajaran], page, start, limit)

    def mst_wilayah(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[MstWilayah]:
        return self._get_rest("MstWilayah", List[MstWilayah], page, start, limit)

    def pangkat_golongan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[PangkatGolongan]:
        return self._get_rest(
            "PangkatGolongan", List[PangkatGolongan], page, start, limit
        )

    def pekerjaan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Pekerjaan]:
        return self._get_rest("Pekerjaan", List[Pekerjaan], page, start, limit)

    def penghasilan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Penghasilan]:
        return self._get_rest("Penghasilan", List[Penghasilan], page, start, limit)

    def role_pengguna(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[RolePengguna]:
        return self._get_rest("RolePengguna", List[RolePengguna], page, start, limit)

    def status_keaktifan_pegawai(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[StatusKeaktifanPegawai]:
        return self._get_rest(
            "StatusKeaktifanPegawai", List[StatusKeaktifanPegawai], page, start, limit
        )

    def status_kepegawaian(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[StatusKepegawaian]:
        return self._get_rest(
            "StatusKepegawaian", List[StatusKepegawaian], page, start, limit
        )

    def status_kepemilikan_sarpras(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[StatusKepemilikanSarpras]:
        return self._get_rest(
            "StatusKepemilikanSarpras",
            List[StatusKepemilikanSarpras],
            page,
            start,
            limit,
        )

    def sumber_air(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberAir]:
        return self._get_rest("SumberAir", List[SumberAir], page, start, limit)

    def sumber_dana_sekolah(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberDanaSekolah]:
        return self._get_rest(
            "SumberDanaSekolah", List[SumberDanaSekolah], page, start, limit
        )

    def sumber_gaji(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberGaji]:
        return self._get_rest("SumberGaji", List[SumberGaji], page, start, limit)

    def sumber_listrik(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberListrik]:
        return self._get_rest("SumberListrik", List[SumberListrik], page, start, limit)

    def sync_log(self, page: int = 1, start: int = 0, limit: int = 50) -> List[SyncLog]:
        return self._get_rest("SyncLog", List[SyncLog], page, start, limit)

    def tahun_ajaran(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[TahunAjaran]:
        return self._get_rest("TahunAjaran", List[TahunAjaran], page, start, limit)

    def tingkat_pendidikan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[TingkatPendidikan]:
        return self._get_rest(
            "TingkatPendidikan", List[TingkatPendidikan], page, start, limit
        )

    def waktu_penyelenggaraan(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[WaktuPenyelenggaraan]:
        return self._get_rest(
            "WaktuPenyelenggaraan", List[WaktuPenyelenggaraan], page, start, limit
        )
