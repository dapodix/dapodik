from typing import List

from dapodik import (
    BaseDapodik,
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
    JenisGugus,
    JenisHapusBuku,
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
    def register_rest(self) -> bool:
        try:
            self.Agama = Agama.maker(self, "rest/Agama")
            self.Akreditasi = Akreditasi.maker(self, "rest/Akreditasi")
            self.AksesInternet = AksesInternet.maker(self, "rest/AksesInternet")
            self.AlatTransportasi = AlatTransportasi.maker(
                self, "rest/AlatTransportasi"
            )
            self.Bank = Bank.maker(self, "rest/Bank")
            self.BentukLembaga = BentukLembaga.maker(self, "rest/BentukLembaga")
            self.Biblio = Biblio.maker(self, "rest/Biblio")
            self.ChildDelete = ChildDelete.maker(self, "rest/ChildDelete")
            self.FasilitasLayanan = FasilitasLayanan.maker(
                self, "rest/FasilitasLayanan"
            )
            self.Gmd = Gmd.maker(self, "rest/Gmd")
            self.JadwalPaud = JadwalPaud.maker(self, "rest/JadwalPaud")
            self.JenisGugus = JenisGugus.maker(self, "rest/JenisGugus")
            self.JenisHapusBuku = JenisHapusBuku.maker(self, "rest/JenisHapusBuku")
            self.JenisKeluar = JenisKeluar.maker(self, "rest/JenisKeluar")
            self.JenisLk = JenisLk.maker(self, "rest/JenisLk")
            self.JenisPendaftaran = JenisPendaftaran.maker(
                self, "rest/JenisPendaftaran"
            )
            self.JenisPrasarana = JenisPrasarana.maker(self, "rest/JenisPrasarana")
            self.JenisPtk = JenisPtk.maker(self, "rest/JenisPtk")
            self.JenisRombel = JenisRombel.maker(self, "rest/JenisRombel")
            self.JenisSarana = JenisSarana.maker(self, "rest/JenisSarana")
            self.JenisTinggal = JenisTinggal.maker(self, "rest/JenisTinggal")
            self.JenjangPendidikan = JenjangPendidikan.maker(
                self, "rest/JenjangPendidikan"
            )
            self.Jurusan = Jurusan.maker(self, "rest/Jurusan")
            self.KategoriTk = KategoriTk.maker(self, "rest/KategoriTk")
            self.KeahlianLaboratorium = KeahlianLaboratorium.maker(
                self, "rest/KeahlianLaboratorium"
            )
            self.KebutuhanKhusus = KebutuhanKhusus.maker(self, "rest/KebutuhanKhusus")
            self.KlasifikasiLembaga = KlasifikasiLembaga.maker(
                self, "rest/KlasifikasiLembaga"
            )
            self.Kurikulum = Kurikulum.maker(self, "rest/Kurikulum")
            self.LembagaPengangkat = LembagaPengangkat.maker(
                self, "rest/LembagaPengangkat"
            )
            self.MataPelajaran = MataPelajaran.maker(self, "rest/MataPelajaran")
            self.MstWilayah = MstWilayah.maker(self, "rest/MstWilayah")
            self.PangkatGolongan = PangkatGolongan.maker(self, "rest/PangkatGolongan")
            self.Pekerjaan = Pekerjaan.maker(self, "rest/Pekerjaan")
            self.Penghasilan = Penghasilan.maker(self, "rest/Penghasilan")
            self.RolePengguna = RolePengguna.maker(self, "rest/RolePengguna")
            self.StatusKeaktifanPegawai = StatusKeaktifanPegawai.maker(
                self, "rest/StatusKeaktifanPegawai"
            )
            self.StatusKepegawaian = StatusKepegawaian.maker(
                self, "rest/StatusKepegawaian"
            )
            self.StatusKepemilikanSarpras = StatusKepemilikanSarpras.maker(
                self, "rest/StatusKepemilikanSarpras"
            )
            self.SumberAir = SumberAir.maker(self, "rest/SumberAir")
            self.SumberDanaSekolah = SumberDanaSekolah.maker(
                self, "rest/SumberDanaSekolah"
            )
            self.SumberGaji = SumberGaji.maker(self, "rest/SumberGaji")
            self.SumberListrik = SumberListrik.maker(self, "rest/SumberListrik")
            self.SyncLog = SyncLog.maker(self, "rest/SyncLog")
            self.TahunAjaran = TahunAjaran.maker(self, "rest/TahunAjaran")
            self.TingkatPendidikan = TingkatPendidikan.maker(
                self, "rest/TingkatPendidikan"
            )
            self.WaktuPenyelenggaraan = WaktuPenyelenggaraan.maker(
                self, "rest/WaktuPenyelenggaraan"
            )
            self.logger.debug("Berhasil memulai rest")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def agama(self) -> List[Agama]:
        return self.Agama()  # type: ignore

    @property
    def akreditasi(self) -> List[Akreditasi]:
        return self.Akreditasi()  # type: ignore

    @property
    def aksesinternet(self) -> List[AksesInternet]:
        return self.AksesInternet()  # type: ignore

    @property
    def alattransportasi(self) -> List[AlatTransportasi]:
        return self.AlatTransportasi()  # type: ignore

    @property
    def bank(self) -> List[Bank]:
        return self.Bank()  # type: ignore

    @property
    def bentuklembaga(self) -> List[BentukLembaga]:
        return self.BentukLembaga()  # type: ignore

    @property
    def biblio(self) -> List[Biblio]:
        return self.Biblio()  # type: ignore

    @property
    def childdelete(self) -> List[ChildDelete]:
        return self.ChildDelete()  # type: ignore

    @property
    def fasilitaslayanan(self) -> List[FasilitasLayanan]:
        return self.FasilitasLayanan()  # type: ignore

    @property
    def gmd(self) -> List[Gmd]:
        return self.Gmd()  # type: ignore

    @property
    def jadwalpaud(self) -> List[JadwalPaud]:
        return self.JadwalPaud()  # type: ignore

    @property
    def jenisgugus(self) -> List[JenisGugus]:
        return self.JenisGugus()  # type: ignore

    @property
    def jenishapusbuku(self) -> List[JenisHapusBuku]:
        return self.JenisHapusBuku()  # type: ignore

    @property
    def jeniskeluar(self) -> List[JenisKeluar]:
        return self.JenisKeluar()  # type: ignore

    @property
    def jenislk(self) -> List[JenisLk]:
        return self.JenisLk()  # type: ignore

    @property
    def jenispendaftaran(self) -> List[JenisPendaftaran]:
        return self.JenisPendaftaran()  # type: ignore

    @property
    def jenisprasarana(self) -> List[JenisPrasarana]:
        return self.JenisPrasarana()  # type: ignore

    @property
    def jenisptk(self) -> List[JenisPtk]:
        return self.JenisPtk()  # type: ignore

    @property
    def jenisrombel(self) -> List[JenisRombel]:
        return self.JenisRombel()  # type: ignore

    @property
    def jenissarana(self) -> List[JenisSarana]:
        return self.JenisSarana()  # type: ignore

    @property
    def jenistinggal(self) -> List[JenisTinggal]:
        return self.JenisTinggal()  # type: ignore

    @property
    def jenjangpendidikan(self) -> List[JenjangPendidikan]:
        return self.JenjangPendidikan()  # type: ignore

    @property
    def jurusan(self) -> List[Jurusan]:
        return self.Jurusan()  # type: ignore

    @property
    def kategoritk(self) -> List[KategoriTk]:
        return self.KategoriTk()  # type: ignore

    @property
    def keahlianlaboratorium(self) -> List[KeahlianLaboratorium]:
        return self.KeahlianLaboratorium()  # type: ignore

    @property
    def kebutuhankhusus(self) -> List[KebutuhanKhusus]:
        return self.KebutuhanKhusus()  # type: ignore

    @property
    def klasifikasilembaga(self) -> List[KlasifikasiLembaga]:
        return self.KlasifikasiLembaga()  # type: ignore

    @property
    def kurikulum(self) -> List[Kurikulum]:
        return self.Kurikulum()  # type: ignore

    @property
    def lembagapengangkat(self) -> List[LembagaPengangkat]:
        return self.LembagaPengangkat()  # type: ignore

    @property
    def matapelajaran(self) -> List[MataPelajaran]:
        return self.MataPelajaran()  # type: ignore

    @property
    def mstwilayah(self) -> List[MstWilayah]:
        return self.MstWilayah()  # type: ignore

    @property
    def pangkatgolongan(self) -> List[PangkatGolongan]:
        return self.PangkatGolongan()  # type: ignore

    @property
    def pekerjaan(self) -> List[Pekerjaan]:
        return self.Pekerjaan()  # type: ignore

    @property
    def penghasilan(self) -> List[Penghasilan]:
        return self.Penghasilan()  # type: ignore

    @property
    def rolepengguna(self) -> List[RolePengguna]:
        return self.RolePengguna()  # type: ignore

    @property
    def statuskeaktifanpegawai(self) -> List[StatusKeaktifanPegawai]:
        return self.StatusKeaktifanPegawai()  # type: ignore

    @property
    def statuskepegawaian(self) -> List[StatusKepegawaian]:
        return self.StatusKepegawaian()  # type: ignore

    @property
    def statuskepemilikansarpras(self) -> List[StatusKepemilikanSarpras]:
        return self.StatusKepemilikanSarpras()  # type: ignore

    @property
    def sumberair(self) -> List[SumberAir]:
        return self.SumberAir()  # type: ignore

    @property
    def sumberdanasekolah(self) -> List[SumberDanaSekolah]:
        return self.SumberDanaSekolah()  # type: ignore

    @property
    def sumbergaji(self) -> List[SumberGaji]:
        return self.SumberGaji()  # type: ignore

    @property
    def sumberlistrik(self) -> List[SumberListrik]:
        return self.SumberListrik()  # type: ignore

    @property
    def synclog(self) -> List[SyncLog]:
        return self.SyncLog()  # type: ignore

    @property
    def tahunajaran(self) -> List[TahunAjaran]:
        return self.TahunAjaran()  # type: ignore

    @property
    def tingkatpendidikan(self) -> List[TingkatPendidikan]:
        return self.TingkatPendidikan()  # type: ignore

    @property
    def waktupenyelenggaraan(self) -> List[WaktuPenyelenggaraan]:
        return self.WaktuPenyelenggaraan()  # type: ignore
