from typing import List

from dapodik.base import BaseDapodik
from . import (
    Agama,
    Akreditasi,
    AksesInternet,
    AlatTransportasi,
    Bank,
    BentukLembaga,
    Biblio,
    FasilitasLayanan,
    Gmd,
    JadwalPaud,
    JenisCita,
    JenisGugus,
    JenisHapusBuku,
    JenisHobby,
    JenisKeluar,
    JenisLk,
    JenisPendaftaran,
    JenisPrasarana,
    JenisPtk,
    JenisRombel,
    JenisSarana,
    JenisTinggal,
    JenjangPendidikan,
    Jurusan,
    KategoriTk,
    KeahlianLaboratorium,
    KebutuhanKhusus,
    KlasifikasiLembaga,
    Kurikulum,
    LembagaPengangkat,
    MataPelajaran,
    MstWilayah,
    PangkatGolongan,
    Pekerjaan,
    Penghasilan,
    RolePengguna,
    StatusKeaktifanPegawai,
    StatusKepegawaian,
    StatusKepemilikanSarpras,
    SumberAir,
    SumberDanaSekolah,
    SumberGaji,
    SumberListrik,
    SyncLog,
    TahunAjaran,
    TingkatPendidikan,
    WaktuPenyelenggaraan,
)

__fetch__ = (
    Agama,
    Akreditasi,
    AksesInternet,
    AlatTransportasi,
    Bank,
    BentukLembaga,
    Biblio,
    FasilitasLayanan,
    Gmd,
    JadwalPaud,
    JenisCita,
    JenisGugus,
    JenisHapusBuku,
    JenisHobby,
    JenisKeluar,
    JenisLk,
    JenisPendaftaran,
    JenisPrasarana,
    JenisPtk,
    JenisRombel,
    JenisSarana,
    JenisTinggal,
    JenjangPendidikan,
    Jurusan,
    KategoriTk,
    KeahlianLaboratorium,
    KebutuhanKhusus,
    KlasifikasiLembaga,
    Kurikulum,
    LembagaPengangkat,
    MataPelajaran,
    MstWilayah,
    PangkatGolongan,
    Pekerjaan,
    Penghasilan,
    RolePengguna,
    StatusKeaktifanPegawai,
    StatusKepegawaian,
    StatusKepemilikanSarpras,
    SumberAir,
    SumberDanaSekolah,
    SumberGaji,
    SumberListrik,
    SyncLog,
    TahunAjaran,
    TingkatPendidikan,
    WaktuPenyelenggaraan,
)


class BaseRest(BaseDapodik):
    __all__ = __fetch__

    def agama(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Agama]:
        res = self._get_rest(
            "Agama",
            page=page,
            limit=limit,
        )
        return self._fr(Agama, res.json())

    def akreditasi(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Akreditasi]:
        res = self._get_rest(
            "Akreditasi",
            page=page,
            limit=limit,
        )
        return self._fr(Akreditasi, res.json())

    def akses_internet(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[AksesInternet]:
        res = self._get_rest(
            "AksesInternet",
            page=page,
            limit=limit,
        )
        return self._fr(AksesInternet, res.json())

    def alat_transportasi(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[AlatTransportasi]:
        res = self._get_rest(
            "AlatTransportasi",
            page=page,
            limit=limit,
        )
        return self._fr(AlatTransportasi, res.json())

    def bank(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Bank]:
        res = self._get_rest(
            "Bank",
            page=page,
            limit=limit,
        )
        return self._fr(Bank, res.json())

    def bentuk_lembaga(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[BentukLembaga]:
        res = self._get_rest(
            "BentukLembaga",
            page=page,
            limit=limit,
        )
        return self._fr(BentukLembaga, res.json())

    def biblio(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Biblio]:
        res = self._get_rest(
            "Biblio",
            page=page,
            limit=limit,
        )
        return self._fr(Biblio, res.json())

    def fasilitas_layanan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[FasilitasLayanan]:
        res = self._get_rest(
            "FasilitasLayanan",
            page=page,
            limit=limit,
        )
        return self._fr(FasilitasLayanan, res.json())

    def gmd(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Gmd]:
        res = self._get_rest(
            "Gmd",
            page=page,
            limit=limit,
        )
        return self._fr(Gmd, res.json())

    def jadwal_paud(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JadwalPaud]:
        res = self._get_rest(
            "JadwalPaud",
            page=page,
            limit=limit,
        )
        return self._fr(JadwalPaud, res.json())

    def jenis_cita(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisCita]:
        res = self._get_rest(
            "JenisCita",
            page=page,
            limit=limit,
        )
        return self._fr(JenisCita, res.json())

    def jenis_gugus(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisGugus]:
        res = self._get_rest(
            "JenisGugus",
            page=page,
            limit=limit,
        )
        return self._fr(JenisGugus, res.json())

    def jenis_hapus_buku(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisHapusBuku]:
        res = self._get_rest(
            "JenisHapusBuku",
            page=page,
            limit=limit,
        )
        return self._fr(JenisHapusBuku, res.json())

    def jenis_hobby(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisHobby]:
        res = self._get_rest(
            "JenisHobby",
            page=page,
            limit=limit,
        )
        return self._fr(JenisHobby, res.json())

    def jenis_keluar(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisKeluar]:
        res = self._get_rest(
            "JenisKeluar",
            page=page,
            limit=limit,
        )
        return self._fr(JenisKeluar, res.json())

    def jenis_lk(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisLk]:
        res = self._get_rest(
            "JenisLk",
            page=page,
            limit=limit,
        )
        return self._fr(JenisLk, res.json())

    def jenis_pendaftaran(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisPendaftaran]:
        res = self._get_rest(
            "JenisPendaftaran",
            page=page,
            limit=limit,
        )
        return self._fr(JenisPendaftaran, res.json())

    def jenis_prasarana(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisPrasarana]:
        res = self._get_rest(
            "JenisPrasarana",
            page=page,
            limit=limit,
        )
        return self._fr(JenisPrasarana, res.json())

    def jenis_ptk(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisPtk]:
        res = self._get_rest(
            "JenisPtk",
            page=page,
            limit=limit,
        )
        return self._fr(JenisPtk, res.json())

    def jenis_rombel(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisRombel]:
        res = self._get_rest(
            "JenisRombel",
            page=page,
            limit=limit,
        )
        return self._fr(JenisRombel, res.json())

    def jenis_sarana(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisSarana]:
        res = self._get_rest(
            "JenisSarana",
            page=page,
            limit=limit,
        )
        return self._fr(JenisSarana, res.json())

    def jenis_tinggal(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenisTinggal]:
        res = self._get_rest(
            "JenisTinggal",
            page=page,
            limit=limit,
        )
        return self._fr(JenisTinggal, res.json())

    def jenjang_pendidikan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[JenjangPendidikan]:
        res = self._get_rest(
            "JenjangPendidikan",
            page=page,
            limit=limit,
        )
        return self._fr(JenjangPendidikan, res.json())

    def jurusan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Jurusan]:
        res = self._get_rest(
            "Jurusan",
            page=page,
            limit=limit,
        )
        return self._fr(Jurusan, res.json())

    def kategori_tk(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[KategoriTk]:
        res = self._get_rest(
            "KategoriTk",
            page=page,
            limit=limit,
        )
        return self._fr(KategoriTk, res.json())

    def keahlian_laboratorium(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[KeahlianLaboratorium]:
        res = self._get_rest(
            "KeahlianLaboratorium",
            page=page,
            limit=limit,
        )
        return self._fr(KeahlianLaboratorium, res.json())

    def kebutuhan_khusus(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[KebutuhanKhusus]:
        res = self._get_rest(
            "KebutuhanKhusus",
            page=page,
            limit=limit,
        )
        return self._fr(KebutuhanKhusus, res.json())

    def klasifikasi_lembaga(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[KlasifikasiLembaga]:
        res = self._get_rest(
            "KlasifikasiLembaga",
            page=page,
            limit=limit,
        )
        return self._fr(KlasifikasiLembaga, res.json())

    def kurikulum(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Kurikulum]:
        res = self._get_rest(
            "Kurikulum",
            page=page,
            limit=limit,
        )
        return self._fr(Kurikulum, res.json())

    def lembaga_pengangkat(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[LembagaPengangkat]:
        res = self._get_rest(
            "LembagaPengangkat",
            page=page,
            limit=limit,
        )
        return self._fr(LembagaPengangkat, res.json())

    def mata_pelajaran(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[MataPelajaran]:
        res = self._get_rest(
            "MataPelajaran",
            page=page,
            limit=limit,
        )
        return self._fr(MataPelajaran, res.json())

    def mst_wilayah(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[MstWilayah]:
        res = self._get_rest(
            "MstWilayah",
            page=page,
            limit=limit,
        )
        return self._fr(MstWilayah, res.json())

    def pangkat_golongan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[PangkatGolongan]:
        res = self._get_rest(
            "PangkatGolongan",
            page=page,
            limit=limit,
        )
        return self._fr(PangkatGolongan, res.json())

    def pekerjaan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Pekerjaan]:
        res = self._get_rest(
            "Pekerjaan",
            page=page,
            limit=limit,
        )
        return self._fr(Pekerjaan, res.json())

    def penghasilan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[Penghasilan]:
        res = self._get_rest(
            "Penghasilan",
            page=page,
            limit=limit,
        )
        return self._fr(Penghasilan, res.json())

    def role_pengguna(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[RolePengguna]:
        res = self._get_rest(
            "RolePengguna",
            page=page,
            limit=limit,
        )
        return self._fr(RolePengguna, res.json())

    def status_keaktifan_pegawai(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[StatusKeaktifanPegawai]:
        res = self._get_rest(
            "StatusKeaktifanPegawai",
            page=page,
            limit=limit,
        )
        return self._fr(StatusKeaktifanPegawai, res.json())

    def status_kepegawaian(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[StatusKepegawaian]:
        res = self._get_rest(
            "StatusKepegawaian",
            page=page,
            limit=limit,
        )
        return self._fr(StatusKepegawaian, res.json())

    def status_kepemilikan_sarpras(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[StatusKepemilikanSarpras]:
        res = self._get_rest(
            "StatusKepemilikanSarpras",
            page=page,
            limit=limit,
        )
        return self._fr(StatusKepemilikanSarpras, res.json())

    def sumber_air(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[SumberAir]:
        res = self._get_rest(
            "SumberAir",
            page=page,
            limit=limit,
        )
        return self._fr(SumberAir, res.json())

    def sumber_dana_sekolah(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[SumberDanaSekolah]:
        res = self._get_rest(
            "SumberDanaSekolah",
            page=page,
            limit=limit,
        )
        return self._fr(SumberDanaSekolah, res.json())

    def sumber_gaji(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[SumberGaji]:
        res = self._get_rest(
            "SumberGaji",
            page=page,
            limit=limit,
        )
        return self._fr(SumberGaji, res.json())

    def sumber_listrik(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[SumberListrik]:
        res = self._get_rest(
            "SumberListrik",
            page=page,
            limit=limit,
        )
        return self._fr(SumberListrik, res.json())

    def sync_log(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[SyncLog]:
        res = self._get_rest(
            "SyncLog",
            page=page,
            limit=limit,
        )
        return self._fr(SyncLog, res.json())

    def tahun_ajaran(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[TahunAjaran]:
        res = self._get_rest(
            "TahunAjaran",
            page=page,
            limit=limit,
        )
        return self._fr(TahunAjaran, res.json())

    def tingkat_pendidikan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[TingkatPendidikan]:
        res = self._get_rest(
            "TingkatPendidikan",
            page=page,
            limit=limit,
        )
        return self._fr(TingkatPendidikan, res.json())

    def waktu_penyelenggaraan(
        self,
        page: int = 1,
        limit: int = 50,
    ) -> List[WaktuPenyelenggaraan]:
        res = self._get_rest(
            "WaktuPenyelenggaraan",
            page=page,
            limit=limit,
        )
        return self._fr(WaktuPenyelenggaraan, res.json())
