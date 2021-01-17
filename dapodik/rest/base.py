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
        data: dict = res.json()
        return self._fl(Agama, data.get("rows"))

    def akreditasi(self) -> List[Akreditasi]:
        res = self._get_rest("Akreditasi")
        data: dict = res.json()
        return self._fl(Akreditasi, data.get("rows"))

    def akses_internet(self) -> List[AksesInternet]:
        res = self._get_rest("AksesInternet")
        data: dict = res.json()
        return self._fl(AksesInternet, data.get("rows"))

    def alat_transportasi(self) -> List[AlatTransportasi]:
        res = self._get_rest("AlatTransportasi")
        data: dict = res.json()
        return self._fl(AlatTransportasi, data.get("rows"))

    def bank(self) -> List[Bank]:
        res = self._get_rest("Bank")
        data: dict = res.json()
        return self._fl(Bank, data.get("rows"))

    def bentuk_lembaga(self) -> List[BentukLembaga]:
        res = self._get_rest("BentukLembaga")
        data: dict = res.json()
        return self._fl(BentukLembaga, data.get("rows"))

    def biblio(self) -> List[Biblio]:
        res = self._get_rest("Biblio")
        data: dict = res.json()
        return self._fl(Biblio, data.get("rows"))

    def child_delete(self) -> List[ChildDelete]:
        res = self._get_rest("ChildDelete")
        data: dict = res.json()
        return self._fl(ChildDelete, data.get("rows"))

    def fasilitas_layanan(self) -> List[FasilitasLayanan]:
        res = self._get_rest("FasilitasLayanan")
        data: dict = res.json()
        return self._fl(FasilitasLayanan, data.get("rows"))

    def gmd(self) -> List[Gmd]:
        res = self._get_rest("Gmd")
        data: dict = res.json()
        return self._fl(Gmd, data.get("rows"))

    def jadwal_paud(self) -> List[JadwalPaud]:
        res = self._get_rest("JadwalPaud")
        data: dict = res.json()
        return self._fl(JadwalPaud, data.get("rows"))

    def jenis_cita(self) -> List[JenisCita]:
        res = self._get_rest("JenisCita")
        data: dict = res.json()
        return self._fl(JenisCita, data.get("rows"))

    def jenis_gugus(self) -> List[JenisGugus]:
        res = self._get_rest("JenisGugus")
        data: dict = res.json()
        return self._fl(JenisGugus, data.get("rows"))

    def jenis_hapus_buku(self) -> List[JenisHapusBuku]:
        res = self._get_rest("JenisHapusBuku")
        data: dict = res.json()
        return self._fl(JenisHapusBuku, data.get("rows"))

    def jenis_hobby(self) -> List[JenisHobby]:
        res = self._get_rest("JenisHobby")
        data: dict = res.json()
        return self._fl(JenisHobby, data.get("rows"))

    def jenis_keluar(self) -> List[JenisKeluar]:
        res = self._get_rest("JenisKeluar")
        data: dict = res.json()
        return self._fl(JenisKeluar, data.get("rows"))

    def jenis_lk(self) -> List[JenisLk]:
        res = self._get_rest("JenisLk")
        data: dict = res.json()
        return self._fl(JenisLk, data.get("rows"))

    def jenis_pendaftaran(self) -> List[JenisPendaftaran]:
        res = self._get_rest("JenisPendaftaran")
        data: dict = res.json()
        return self._fl(JenisPendaftaran, data.get("rows"))

    def jenis_prasarana(self) -> List[JenisPrasarana]:
        res = self._get_rest("JenisPrasarana")
        data: dict = res.json()
        return self._fl(JenisPrasarana, data.get("rows"))

    def jenis_ptk(self) -> List[JenisPtk]:
        res = self._get_rest("JenisPtk")
        data: dict = res.json()
        return self._fl(JenisPtk, data.get("rows"))

    def jenis_rombel(self) -> List[JenisRombel]:
        res = self._get_rest("JenisRombel")
        data: dict = res.json()
        return self._fl(JenisRombel, data.get("rows"))

    def jenis_sarana(self) -> List[JenisSarana]:
        res = self._get_rest("JenisSarana")
        data: dict = res.json()
        return self._fl(JenisSarana, data.get("rows"))

    def jenis_tinggal(self) -> List[JenisTinggal]:
        res = self._get_rest("JenisTinggal")
        data: dict = res.json()
        return self._fl(JenisTinggal, data.get("rows"))

    def jenjang_pendidikan(self) -> List[JenjangPendidikan]:
        res = self._get_rest("JenjangPendidikan")
        data: dict = res.json()
        return self._fl(JenjangPendidikan, data.get("rows"))

    def jurusan(self) -> List[Jurusan]:
        res = self._get_rest("Jurusan")
        data: dict = res.json()
        return self._fl(Jurusan, data.get("rows"))

    def kategori_tk(self) -> List[KategoriTk]:
        res = self._get_rest("KategoriTk")
        data: dict = res.json()
        return self._fl(KategoriTk, data.get("rows"))

    def keahlian_laboratorium(self) -> List[KeahlianLaboratorium]:
        res = self._get_rest("KeahlianLaboratorium")
        data: dict = res.json()
        return self._fl(KeahlianLaboratorium, data.get("rows"))

    def kebutuhan_khusus(self) -> List[KebutuhanKhusus]:
        res = self._get_rest("KebutuhanKhusus")
        data: dict = res.json()
        return self._fl(KebutuhanKhusus, data.get("rows"))

    def klasifikasi_lembaga(self) -> List[KlasifikasiLembaga]:
        res = self._get_rest("KlasifikasiLembaga")
        data: dict = res.json()
        return self._fl(KlasifikasiLembaga, data.get("rows"))

    def kurikulum(self) -> List[Kurikulum]:
        res = self._get_rest("Kurikulum")
        data: dict = res.json()
        return self._fl(Kurikulum, data.get("rows"))

    def lembaga_pengangkat(self) -> List[LembagaPengangkat]:
        res = self._get_rest("LembagaPengangkat")
        data: dict = res.json()
        return self._fl(LembagaPengangkat, data.get("rows"))

    def mata_pelajaran(self) -> List[MataPelajaran]:
        res = self._get_rest("MataPelajaran")
        data: dict = res.json()
        return self._fl(MataPelajaran, data.get("rows"))

    def mst_wilayah(self) -> List[MstWilayah]:
        res = self._get_rest("MstWilayah")
        data: dict = res.json()
        return self._fl(MstWilayah, data.get("rows"))

    def pangkat_golongan(self) -> List[PangkatGolongan]:
        res = self._get_rest("PangkatGolongan")
        data: dict = res.json()
        return self._fl(PangkatGolongan, data.get("rows"))

    def pekerjaan(self) -> List[Pekerjaan]:
        res = self._get_rest("Pekerjaan")
        data: dict = res.json()
        return self._fl(Pekerjaan, data.get("rows"))

    def penghasilan(self) -> List[Penghasilan]:
        res = self._get_rest("Penghasilan")
        data: dict = res.json()
        return self._fl(Penghasilan, data.get("rows"))

    def role_pengguna(self) -> List[RolePengguna]:
        res = self._get_rest("RolePengguna")
        data: dict = res.json()
        return self._fl(RolePengguna, data.get("rows"))

    def status_keaktifan_pegawai(self) -> List[StatusKeaktifanPegawai]:
        res = self._get_rest("StatusKeaktifanPegawai")
        data: dict = res.json()
        return self._fl(StatusKeaktifanPegawai, data.get("rows"))

    def status_kepegawaian(self) -> List[StatusKepegawaian]:
        res = self._get_rest("StatusKepegawaian")
        data: dict = res.json()
        return self._fl(StatusKepegawaian, data.get("rows"))

    def status_kepemilikan_sarpras(self) -> List[StatusKepemilikanSarpras]:
        res = self._get_rest("StatusKepemilikanSarpras")
        data: dict = res.json()
        return self._fl(StatusKepemilikanSarpras, data.get("rows"))

    def sumber_air(self) -> List[SumberAir]:
        res = self._get_rest("SumberAir")
        data: dict = res.json()
        return self._fl(SumberAir, data.get("rows"))

    def sumber_dana_sekolah(self) -> List[SumberDanaSekolah]:
        res = self._get_rest("SumberDanaSekolah")
        data: dict = res.json()
        return self._fl(SumberDanaSekolah, data.get("rows"))

    def sumber_gaji(self) -> List[SumberGaji]:
        res = self._get_rest("SumberGaji")
        data: dict = res.json()
        return self._fl(SumberGaji, data.get("rows"))

    def sumber_listrik(self) -> List[SumberListrik]:
        res = self._get_rest("SumberListrik")
        data: dict = res.json()
        return self._fl(SumberListrik, data.get("rows"))

    def sync_log(self) -> List[SyncLog]:
        res = self._get_rest("SyncLog")
        data: dict = res.json()
        return self._fl(SyncLog, data.get("rows"))

    def tahun_ajaran(self) -> List[TahunAjaran]:
        res = self._get_rest("TahunAjaran")
        data: dict = res.json()
        return self._fl(TahunAjaran, data.get("rows"))

    def tingkat_pendidikan(self) -> List[TingkatPendidikan]:
        res = self._get_rest("TingkatPendidikan")
        data: dict = res.json()
        return self._fl(TingkatPendidikan, data.get("rows"))

    def waktu_penyelenggaraan(self) -> List[WaktuPenyelenggaraan]:
        res = self._get_rest("WaktuPenyelenggaraan")
        data: dict = res.json()
        return self._fl(WaktuPenyelenggaraan, data.get("rows"))
