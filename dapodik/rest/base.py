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
    ChildDelete,
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
    ChildDelete,
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

    def agama(self) -> List[Agama]:
        res = self._get_rest("Agama")
        return self._fl(Agama, res.json())

    def akreditasi(self) -> List[Akreditasi]:
        res = self._get_rest("Akreditasi")
        return self._fl(Akreditasi, res.json())

    def akses_internet(self) -> List[AksesInternet]:
        res = self._get_rest("AksesInternet")
        return self._fl(AksesInternet, res.json())

    def alat_transportasi(self) -> List[AlatTransportasi]:
        res = self._get_rest("AlatTransportasi")
        return self._fl(AlatTransportasi, res.json())

    def bank(self) -> List[Bank]:
        res = self._get_rest("Bank")
        return self._fl(Bank, res.json())

    def bentuk_lembaga(self) -> List[BentukLembaga]:
        res = self._get_rest("BentukLembaga")
        return self._fl(BentukLembaga, res.json())

    def biblio(self) -> List[Biblio]:
        res = self._get_rest("Biblio")
        return self._fl(Biblio, res.json())

    def child_delete(self) -> List[ChildDelete]:
        res = self._get_rest("ChildDelete")
        return self._fl(ChildDelete, res.json())

    def fasilitas_layanan(self) -> List[FasilitasLayanan]:
        res = self._get_rest("FasilitasLayanan")
        return self._fl(FasilitasLayanan, res.json())

    def gmd(self) -> List[Gmd]:
        res = self._get_rest("Gmd")
        return self._fl(Gmd, res.json())

    def jadwal_paud(self) -> List[JadwalPaud]:
        res = self._get_rest("JadwalPaud")
        return self._fl(JadwalPaud, res.json())

    def jenis_cita(self) -> List[JenisCita]:
        res = self._get_rest("JenisCita")
        return self._fl(JenisCita, res.json())

    def jenis_gugus(self) -> List[JenisGugus]:
        res = self._get_rest("JenisGugus")
        return self._fl(JenisGugus, res.json())

    def jenis_hapus_buku(self) -> List[JenisHapusBuku]:
        res = self._get_rest("JenisHapusBuku")
        return self._fl(JenisHapusBuku, res.json())

    def jenis_hobby(self) -> List[JenisHobby]:
        res = self._get_rest("JenisHobby")
        return self._fl(JenisHobby, res.json())

    def jenis_keluar(self) -> List[JenisKeluar]:
        res = self._get_rest("JenisKeluar")
        return self._fl(JenisKeluar, res.json())

    def jenis_lk(self) -> List[JenisLk]:
        res = self._get_rest("JenisLk")
        return self._fl(JenisLk, res.json())

    def jenis_pendaftaran(self) -> List[JenisPendaftaran]:
        res = self._get_rest("JenisPendaftaran")
        return self._fl(JenisPendaftaran, res.json())

    def jenis_prasarana(self) -> List[JenisPrasarana]:
        res = self._get_rest("JenisPrasarana")
        return self._fl(JenisPrasarana, res.json())

    def jenis_ptk(self) -> List[JenisPtk]:
        res = self._get_rest("JenisPtk")
        return self._fl(JenisPtk, res.json())

    def jenis_rombel(self) -> List[JenisRombel]:
        res = self._get_rest("JenisRombel")
        return self._fl(JenisRombel, res.json())

    def jenis_sarana(self) -> List[JenisSarana]:
        res = self._get_rest("JenisSarana")
        return self._fl(JenisSarana, res.json())

    def jenis_tinggal(self) -> List[JenisTinggal]:
        res = self._get_rest("JenisTinggal")
        return self._fl(JenisTinggal, res.json())

    def jenjang_pendidikan(self) -> List[JenjangPendidikan]:
        res = self._get_rest("JenjangPendidikan")
        return self._fl(JenjangPendidikan, res.json())

    def jurusan(self) -> List[Jurusan]:
        res = self._get_rest("Jurusan")
        return self._fl(Jurusan, res.json())

    def kategori_tk(self) -> List[KategoriTk]:
        res = self._get_rest("KategoriTk")
        return self._fl(KategoriTk, res.json())

    def keahlian_laboratorium(self) -> List[KeahlianLaboratorium]:
        res = self._get_rest("KeahlianLaboratorium")
        return self._fl(KeahlianLaboratorium, res.json())

    def kebutuhan_khusus(self) -> List[KebutuhanKhusus]:
        res = self._get_rest("KebutuhanKhusus")
        return self._fl(KebutuhanKhusus, res.json())

    def klasifikasi_lembaga(self) -> List[KlasifikasiLembaga]:
        res = self._get_rest("KlasifikasiLembaga")
        return self._fl(KlasifikasiLembaga, res.json())

    def kurikulum(self) -> List[Kurikulum]:
        res = self._get_rest("Kurikulum")
        return self._fl(Kurikulum, res.json())

    def lembaga_pengangkat(self) -> List[LembagaPengangkat]:
        res = self._get_rest("LembagaPengangkat")
        return self._fl(LembagaPengangkat, res.json())

    def mata_pelajaran(self) -> List[MataPelajaran]:
        res = self._get_rest("MataPelajaran")
        return self._fl(MataPelajaran, res.json())

    def mst_wilayah(self) -> List[MstWilayah]:
        res = self._get_rest("MstWilayah")
        return self._fl(MstWilayah, res.json())

    def pangkat_golongan(self) -> List[PangkatGolongan]:
        res = self._get_rest("PangkatGolongan")
        return self._fl(PangkatGolongan, res.json())

    def pekerjaan(self) -> List[Pekerjaan]:
        res = self._get_rest("Pekerjaan")
        return self._fl(Pekerjaan, res.json())

    def penghasilan(self) -> List[Penghasilan]:
        res = self._get_rest("Penghasilan")
        return self._fl(Penghasilan, res.json())

    def role_pengguna(self) -> List[RolePengguna]:
        res = self._get_rest("RolePengguna")
        return self._fl(RolePengguna, res.json())

    def status_keaktifan_pegawai(self) -> List[StatusKeaktifanPegawai]:
        res = self._get_rest("StatusKeaktifanPegawai")
        return self._fl(StatusKeaktifanPegawai, res.json())

    def status_kepegawaian(self) -> List[StatusKepegawaian]:
        res = self._get_rest("StatusKepegawaian")
        return self._fl(StatusKepegawaian, res.json())

    def status_kepemilikan_sarpras(self) -> List[StatusKepemilikanSarpras]:
        res = self._get_rest("StatusKepemilikanSarpras")
        return self._fl(StatusKepemilikanSarpras, res.json())

    def sumber_air(self) -> List[SumberAir]:
        res = self._get_rest("SumberAir")
        return self._fl(SumberAir, res.json())

    def sumber_dana_sekolah(self) -> List[SumberDanaSekolah]:
        res = self._get_rest("SumberDanaSekolah")
        return self._fl(SumberDanaSekolah, res.json())

    def sumber_gaji(self) -> List[SumberGaji]:
        res = self._get_rest("SumberGaji")
        return self._fl(SumberGaji, res.json())

    def sumber_listrik(self) -> List[SumberListrik]:
        res = self._get_rest("SumberListrik")
        return self._fl(SumberListrik, res.json())

    def sync_log(self) -> List[SyncLog]:
        res = self._get_rest("SyncLog")
        return self._fl(SyncLog, res.json())

    def tahun_ajaran(self) -> List[TahunAjaran]:
        res = self._get_rest("TahunAjaran")
        return self._fl(TahunAjaran, res.json())

    def tingkat_pendidikan(self) -> List[TingkatPendidikan]:
        res = self._get_rest("TingkatPendidikan")
        return self._fl(TingkatPendidikan, res.json())

    def waktu_penyelenggaraan(self) -> List[WaktuPenyelenggaraan]:
        res = self._get_rest("WaktuPenyelenggaraan")
        return self._fl(WaktuPenyelenggaraan, res.json())
