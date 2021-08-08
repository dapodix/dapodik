from typing import List

from dapodik.base import BaseDapodik
from dapodik.utils.helper import cached

from . import Agama
from . import Akreditasi
from . import AksesInternet
from . import AlasanLayakPip
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
    @cached("agama")
    def agama(
        self, agama_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Agama]:
        return self._get_rest(
            "Agama",
            List[Agama],
            page,
            start,
            limit,
            query=self._query(agama_id=agama_id),
        )

    @cached("akreditasi")
    def akreditasi(
        self, akreditasi_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Akreditasi]:
        return self._get_rest(
            "Akreditasi",
            List[Akreditasi],
            page,
            start,
            limit,
            query=self._query(akreditasi_id=akreditasi_id),
        )

    @cached("akses_internet")
    def akses_internet(
        self,
        akses_internet_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[AksesInternet]:
        return self._get_rest(
            "AksesInternet",
            List[AksesInternet],
            page,
            start,
            limit,
            query=self._query(akses_internet_id=akses_internet_id),
        )

    @cached("alasan_layak_pip")
    def alasan_layak_pip(
        self,
        id_layak_pip: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[AlasanLayakPip]:
        return self._get_rest(
            "AlasanLayakPip",
            List[AlasanLayakPip],
            page,
            start,
            limit,
            query=self._query(id_layak_pip=id_layak_pip),
        )

    @cached("alat_transportasi")
    def alat_transportasi(
        self,
        alat_transportasi_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[AlatTransportasi]:
        return self._get_rest(
            "AlatTransportasi",
            List[AlatTransportasi],
            page,
            start,
            limit,
            self._query(alat_transportasi_id=alat_transportasi_id),
        )

    @cached("bank")
    def bank(
        self, id_bank: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Bank]:
        return self._get_rest(
            "Bank", List[Bank], page, start, limit, query=self._query(id_bank=id_bank)
        )

    @cached("bentuk_lembaga")
    def bentuk_lembaga(
        self,
        bentuk_lembaga_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[BentukLembaga]:
        return self._get_rest(
            "BentukLembaga",
            List[BentukLembaga],
            page,
            start,
            limit,
            query=self._query(bentuk_lembaga_id=bentuk_lembaga_id),
        )

    @cached("biblio")
    def biblio(
        self, id_biblio: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Biblio]:
        return self._get_rest(
            "Biblio",
            List[Biblio],
            page,
            start,
            limit,
            query=self._query(id_biblio=id_biblio),
        )

    @cached("fasilitas_layanan")
    def fasilitas_layanan(
        self,
        fasilitas_layanan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[FasilitasLayanan]:
        return self._get_rest(
            "FasilitasLayanan",
            List[FasilitasLayanan],
            page,
            start,
            limit,
            query=self._query(fasilitas_layanan_id=fasilitas_layanan_id),
        )

    @cached("gmd")
    def gmd(
        self, id_gmd: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Gmd]:
        return self._get_rest(
            "Gmd", List[Gmd], page, start, limit, query=self._query(id_gmd=id_gmd)
        )

    @cached("jadwal_paud")
    def jadwal_paud(
        self, jadwal_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JadwalPaud]:
        return self._get_rest(
            "JadwalPaud",
            List[JadwalPaud],
            page,
            start,
            limit,
            query=self._query(jadwal_id=jadwal_id),
        )

    @cached("jenis_cita")
    def jenis_cita(
        self, id_cita: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisCita]:
        return self._get_rest(
            "JenisCita",
            List[JenisCita],
            page,
            start,
            limit,
            query=self._query(id_cita=id_cita),
        )

    @cached("jenis_gugus")
    def jenis_gugus(
        self, jenis_gugus_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisGugus]:
        return self._get_rest(
            "JenisGugus",
            List[JenisGugus],
            page,
            start,
            limit,
            query=self._query(jenis_gugus_id=jenis_gugus_id),
        )

    @cached("jenis_hapus_buku")
    def jenis_hapus_buku(
        self, id_hapus_buku: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisHapusBuku]:
        return self._get_rest(
            "JenisHapusBuku",
            List[JenisHapusBuku],
            page,
            start,
            limit,
            query=self._query(id_hapus_buku=id_hapus_buku),
        )

    @cached("jenis_hobby")
    def jenis_hobby(
        self, id_hobby: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisHobby]:
        return self._get_rest(
            "JenisHobby",
            List[JenisHobby],
            page,
            start,
            limit,
            query=self._query(id_hobby=id_hobby),
        )

    @cached("jenis_keluar")
    def jenis_keluar(
        self,
        jenis_keluar_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenisKeluar]:
        return self._get_rest(
            "JenisKeluar",
            List[JenisKeluar],
            page,
            start,
            limit,
            query=self._query(jenis_keluar_id=jenis_keluar_id),
        )

    @cached("jenis_lk")
    def jenis_lk(
        self, id_jenis_lk: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisLk]:
        return self._get_rest(
            "JenisLk", List[JenisLk], page, start, limit, query=self._query(id_jenis_lk)
        )

    @cached("jenis_pendaftaran")
    def jenis_pendaftaran(
        self,
        jenis_pendaftaran_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenisPendaftaran]:
        return self._get_rest(
            "JenisPendaftaran",
            List[JenisPendaftaran],
            page,
            start,
            limit,
            query=self._query(jenis_pendaftaran_id=jenis_pendaftaran_id),
        )

    @cached("jenis_prasarana")
    def jenis_prasarana(
        self,
        jenis_prasarana_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenisPrasarana]:
        return self._get_rest(
            "JenisPrasarana",
            List[JenisPrasarana],
            page,
            start,
            limit,
            query=self._query(jenis_prasarana_id=jenis_prasarana_id),
        )

    @cached("jenis_ptk")
    def jenis_ptk(
        self, jenis_ptk_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisPtk]:
        return self._get_rest(
            "JenisPtk",
            List[JenisPtk],
            page,
            start,
            limit,
            query=self._query(jenis_ptk_id=jenis_ptk_id),
        )

    @cached("jenis_rombel")
    def jenis_rombel(
        self, jenis_rombel: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[JenisRombel]:
        return self._get_rest(
            "JenisRombel",
            List[JenisRombel],
            page,
            start,
            limit,
            query=self._query(jenis_rombel=jenis_rombel),
        )

    @cached("jenis_sarana")
    def jenis_sarana(
        self,
        jenis_sarana_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenisSarana]:
        return self._get_rest(
            "JenisSarana",
            List[JenisSarana],
            page,
            start,
            limit,
            query=self._query(jenis_sarana_id=jenis_sarana_id),
        )

    @cached("jenis_tinggal")
    def jenis_tinggal(
        self,
        jenis_tinggal_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenisTinggal]:
        return self._get_rest(
            "JenisTinggal",
            List[JenisTinggal],
            page,
            start,
            limit,
            query=self._query(jenis_tinggal_id=jenis_tinggal_id),
        )

    @cached("jenjang_pendidikan")
    def jenjang_pendidikan(
        self,
        jenjang_pendidikan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[JenjangPendidikan]:
        return self._get_rest(
            "JenjangPendidikan",
            List[JenjangPendidikan],
            page,
            start,
            limit,
            query=self._query(jenjang_pendidikan_id=jenjang_pendidikan_id),
        )

    @cached("jurusan")
    def jurusan(
        self, jurusan_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Jurusan]:
        return self._get_rest(
            "Jurusan",
            List[Jurusan],
            page,
            start,
            limit,
            query=self._query(jurusan_id=jurusan_id),
        )

    @cached("kategori_tk")
    def kategori_tk(
        self, kategori_tk_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[KategoriTk]:
        return self._get_rest(
            "KategoriTk",
            List[KategoriTk],
            page,
            start,
            limit,
            query=self._query(kategori_tk_id=kategori_tk_id),
        )

    @cached("keahlian_laboratorium")
    def keahlian_laboratorium(
        self,
        keahlian_laboratorium_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[KeahlianLaboratorium]:
        return self._get_rest(
            "KeahlianLaboratorium",
            List[KeahlianLaboratorium],
            page,
            start,
            limit,
            query=self._query(keahlian_laboratorium_id=keahlian_laboratorium_id),
        )

    @cached("kebutuhan_khusus")
    def kebutuhan_khusus(
        self,
        kebutuhan_khusus_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[KebutuhanKhusus]:
        return self._get_rest(
            "KebutuhanKhusus",
            List[KebutuhanKhusus],
            page,
            start,
            limit,
            query=self._query(kebutuhan_khusus_id=kebutuhan_khusus_id),
        )

    @cached("klasifikasi_lembaga")
    def klasifikasi_lembaga(
        self,
        klasifikasi_lembaga_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[KlasifikasiLembaga]:
        return self._get_rest(
            "KlasifikasiLembaga",
            List[KlasifikasiLembaga],
            page,
            start,
            limit,
            query=self._query(klasifikasi_lembaga_id=klasifikasi_lembaga_id),
        )

    @cached("kurikulum")
    def kurikulum(
        self, kurikulum_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Kurikulum]:
        return self._get_rest(
            "Kurikulum",
            List[Kurikulum],
            page,
            start,
            limit,
            query=self._query(kurikulum_id=kurikulum_id),
        )

    @cached("lembaga_pengangkat")
    def lembaga_pengangkat(
        self,
        lembaga_pengangkat_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[LembagaPengangkat]:
        return self._get_rest(
            "LembagaPengangkat",
            List[LembagaPengangkat],
            page,
            start,
            limit,
            query=self._query(lembaga_pengangkat_id=lembaga_pengangkat_id),
        )

    @cached("mata_pelajaran")
    def mata_pelajaran(
        self,
        mata_pelajaran_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[MataPelajaran]:
        return self._get_rest(
            "MataPelajaran",
            List[MataPelajaran],
            page,
            start,
            limit,
            query=self._query(mata_pelajaran_id=mata_pelajaran_id),
        )

    @cached("mst_wilayah")
    def mst_wilayah(
        self, kode_wilayah: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[MstWilayah]:
        return self._get_rest(
            "MstWilayah",
            List[MstWilayah],
            page,
            start,
            limit,
            query=self._query(kode_wilayah=kode_wilayah),
        )

    @cached("pangkat_golongan")
    def pangkat_golongan(
        self,
        pangkat_golongan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[PangkatGolongan]:
        return self._get_rest(
            "PangkatGolongan",
            List[PangkatGolongan],
            page,
            start,
            limit,
            query=self._query(pangkat_golongan_id=pangkat_golongan_id),
        )

    @cached("pekerjaan")
    def pekerjaan(
        self, pekerjaan_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Pekerjaan]:
        return self._get_rest(
            "Pekerjaan",
            List[Pekerjaan],
            page,
            start,
            limit,
            query=self._query(pekerjaan_id=pekerjaan_id),
        )

    @cached("penghasilan")
    def penghasilan(
        self, penghasilan_id: int = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[Penghasilan]:
        return self._get_rest(
            "Penghasilan",
            List[Penghasilan],
            page,
            start,
            limit,
            query=self._query(penghasilan_id=penghasilan_id),
        )

    @cached("role_pengguna")
    def role_pengguna(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[RolePengguna]:
        return self._get_rest("RolePengguna", List[RolePengguna], page, start, limit)

    @cached("status_keaktifan_pegawai")
    def status_keaktifan_pegawai(
        self,
        status_keaktifan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[StatusKeaktifanPegawai]:
        return self._get_rest(
            "StatusKeaktifanPegawai",
            List[StatusKeaktifanPegawai],
            page,
            start,
            limit,
            query=self._query(status_keaktifan_id=status_keaktifan_id),
        )

    @cached("status_kepegawaian")
    def status_kepegawaian(
        self,
        status_kepegawaian_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[StatusKepegawaian]:
        return self._get_rest(
            "StatusKepegawaian",
            List[StatusKepegawaian],
            page,
            start,
            limit,
            query=self._query(status_kepegawaian_id=status_kepegawaian_id),
        )

    @cached("status_kepemilikan_sarpras")
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

    @cached("sumber_air")
    def sumber_air(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberAir]:
        return self._get_rest("SumberAir", List[SumberAir], page, start, limit)

    @cached("sumber_dana_sekolah")
    def sumber_dana_sekolah(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberDanaSekolah]:
        return self._get_rest(
            "SumberDanaSekolah", List[SumberDanaSekolah], page, start, limit
        )

    @cached("sumber_gaji")
    def sumber_gaji(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberGaji]:
        return self._get_rest("SumberGaji", List[SumberGaji], page, start, limit)

    @cached("sumber_listrik")
    def sumber_listrik(
        self, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SumberListrik]:
        return self._get_rest("SumberListrik", List[SumberListrik], page, start, limit)

    @cached("sync_log")
    def sync_log(
        self, sync_log_id: str = None, page: int = 1, start: int = 0, limit: int = 50
    ) -> List[SyncLog]:
        return self._get_rest(
            "SyncLog",
            List[SyncLog],
            page,
            start,
            limit,
            query=self._query(sync_log_id=sync_log_id),
        )

    @cached("tahun_ajaran")
    def tahun_ajaran(
        self,
        tahun_ajaran_id: str = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[TahunAjaran]:
        return self._get_rest(
            "TahunAjaran",
            List[TahunAjaran],
            page,
            start,
            limit,
            query=self._query(tahun_ajaran_id=tahun_ajaran_id),
        )

    @cached("tingkat_pendidikan")
    def tingkat_pendidikan(
        self,
        tingkat_pendidikan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[TingkatPendidikan]:
        return self._get_rest(
            "TingkatPendidikan",
            List[TingkatPendidikan],
            page,
            start,
            limit,
            query=self._query(tingkat_pendidikan_id=tingkat_pendidikan_id),
        )

    @cached("waktu_penyelenggaraan")
    def waktu_penyelenggaraan(
        self,
        waktu_penyelenggaraan_id: int = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[WaktuPenyelenggaraan]:
        return self._get_rest(
            "WaktuPenyelenggaraan",
            List[WaktuPenyelenggaraan],
            page,
            start,
            limit,
            query=self._query(waktu_penyelenggaraan_id=waktu_penyelenggaraan_id),
        )
