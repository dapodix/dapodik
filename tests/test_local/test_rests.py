from logging import getLogger
from random import randint

from dapodik import Dapodik
from dapodik.base import Results
from dapodik.rest import (
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

logger = getLogger(__name__)


class TestRest:
    @staticmethod
    def r_slice(datas: Results) -> Results:
        length = len(datas)
        if length > 0:
            if length > 50:
                few = randint(5, 10)
            elif length > 25:
                few = randint(3, 5)
            elif length > 5:
                few = randint(2, 3)
            elif length > 3:
                few = randint(1, 2)
            else:
                few = 1
            return datas[1:few]  # type: ignore
        return datas

    def test_get_agama(self, dapodik: Dapodik):
        agamas = dapodik.rest.agama()
        for agama in self.r_slice(agamas):
            assert isinstance(agama, Agama)

    def test_get_akreditasi(self, dapodik: Dapodik):
        akreditasis = dapodik.rest.akreditasi()
        for akreditasi in self.r_slice(akreditasis):
            assert isinstance(akreditasi, Akreditasi)

    def test_get_akses_internet(self, dapodik: Dapodik):
        akses_internets = dapodik.rest.akses_internet()
        for akses_internet in self.r_slice(akses_internets):
            assert isinstance(akses_internet, AksesInternet)

    def test_get_alat_transportasi(self, dapodik: Dapodik):
        alat_transportasis = dapodik.rest.alat_transportasi()
        for alat_transportasi in self.r_slice(alat_transportasis):
            assert isinstance(alat_transportasi, AlatTransportasi)

    def test_get_bank(self, dapodik: Dapodik):
        banks = dapodik.rest.bank()
        for bank in self.r_slice(banks):
            assert isinstance(bank, Bank)

    def test_get_bentuk_lembaga(self, dapodik: Dapodik):
        bentuk_lembagas = dapodik.rest.bentuk_lembaga()
        for bentuk_lembaga in self.r_slice(bentuk_lembagas):
            assert isinstance(bentuk_lembaga, BentukLembaga)

    def test_get_biblio(self, dapodik: Dapodik):
        biblios = dapodik.rest.biblio()
        for biblio in self.r_slice(biblios):
            assert isinstance(biblio, Biblio)

    def test_get_fasilitas_layanan(self, dapodik: Dapodik):
        fasilitas_layanans = dapodik.rest.fasilitas_layanan()
        for fasilitas_layanan in self.r_slice(fasilitas_layanans):
            assert isinstance(fasilitas_layanan, FasilitasLayanan)

    def test_get_gmd(self, dapodik: Dapodik):
        gmds = dapodik.rest.gmd()
        for gmd in self.r_slice(gmds):
            assert isinstance(gmd, Gmd)

    def test_get_jadwal_paud(self, dapodik: Dapodik):
        jadwal_pauds = dapodik.rest.jadwal_paud()
        for jadwal_paud in self.r_slice(jadwal_pauds):
            assert isinstance(jadwal_paud, JadwalPaud)

    def test_get_jenis_cita(self, dapodik: Dapodik):
        jenis_citas = dapodik.rest.jenis_cita()
        for jenis_cita in self.r_slice(jenis_citas):
            assert isinstance(jenis_cita, JenisCita)

    def test_get_jenis_gugus(self, dapodik: Dapodik):
        jenis_guguss = dapodik.rest.jenis_gugus()
        for jenis_gugus in self.r_slice(jenis_guguss):
            assert isinstance(jenis_gugus, JenisGugus)

    def test_get_jenis_hapus_buku(self, dapodik: Dapodik):
        jenis_hapus_bukus = dapodik.rest.jenis_hapus_buku()
        for jenis_hapus_buku in self.r_slice(jenis_hapus_bukus):
            assert isinstance(jenis_hapus_buku, JenisHapusBuku)

    def test_get_jenis_hobby(self, dapodik: Dapodik):
        jenis_hobbys = dapodik.rest.jenis_hobby()
        for jenis_hobby in self.r_slice(jenis_hobbys):
            assert isinstance(jenis_hobby, JenisHobby)

    def test_get_jenis_keluar(self, dapodik: Dapodik):
        jenis_keluars = dapodik.rest.jenis_keluar()
        for jenis_keluar in self.r_slice(jenis_keluars):
            assert isinstance(jenis_keluar, JenisKeluar)

    def test_get_jenis_lk(self, dapodik: Dapodik):
        jenis_lks = dapodik.rest.jenis_lk()
        for jenis_lk in self.r_slice(jenis_lks):
            assert isinstance(jenis_lk, JenisLk)

    def test_get_jenis_pendaftaran(self, dapodik: Dapodik):
        jenis_pendaftarans = dapodik.rest.jenis_pendaftaran()
        for jenis_pendaftaran in self.r_slice(jenis_pendaftarans):
            assert isinstance(jenis_pendaftaran, JenisPendaftaran)

    def test_get_jenis_prasarana(self, dapodik: Dapodik):
        jenis_prasaranas = dapodik.rest.jenis_prasarana()
        for jenis_prasarana in self.r_slice(jenis_prasaranas):
            assert isinstance(jenis_prasarana, JenisPrasarana)

    def test_get_jenis_ptk(self, dapodik: Dapodik):
        jenis_ptks = dapodik.rest.jenis_ptk()
        for jenis_ptk in self.r_slice(jenis_ptks):
            assert isinstance(jenis_ptk, JenisPtk)

    def test_get_jenis_rombel(self, dapodik: Dapodik):
        jenis_rombels = dapodik.rest.jenis_rombel()
        for jenis_rombel in self.r_slice(jenis_rombels):
            assert isinstance(jenis_rombel, JenisRombel)

    def test_get_jenis_sarana(self, dapodik: Dapodik):
        jenis_saranas = dapodik.rest.jenis_sarana()
        for jenis_sarana in self.r_slice(jenis_saranas):
            assert isinstance(jenis_sarana, JenisSarana)

    def test_get_jenis_tinggal(self, dapodik: Dapodik):
        jenis_tinggals = dapodik.rest.jenis_tinggal()
        for jenis_tinggal in self.r_slice(jenis_tinggals):
            assert isinstance(jenis_tinggal, JenisTinggal)

    def test_get_jenjang_pendidikan(self, dapodik: Dapodik):
        jenjang_pendidikans = dapodik.rest.jenjang_pendidikan()
        for jenjang_pendidikan in self.r_slice(jenjang_pendidikans):
            assert isinstance(jenjang_pendidikan, JenjangPendidikan)

    def test_get_jurusan(self, dapodik: Dapodik):
        jurusans = dapodik.rest.jurusan()
        for jurusan in self.r_slice(jurusans):
            assert isinstance(jurusan, Jurusan)

    def test_get_kategori_tk(self, dapodik: Dapodik):
        kategori_tks = dapodik.rest.kategori_tk()
        for kategori_tk in self.r_slice(kategori_tks):
            assert isinstance(kategori_tk, KategoriTk)

    def test_get_keahlian_laboratorium(self, dapodik: Dapodik):
        keahlian_laboratoriums = dapodik.rest.keahlian_laboratorium()
        for keahlian_laboratorium in self.r_slice(keahlian_laboratoriums):
            assert isinstance(keahlian_laboratorium, KeahlianLaboratorium)

    def test_get_kebutuhan_khusus(self, dapodik: Dapodik):
        kebutuhan_khususs = dapodik.rest.kebutuhan_khusus()
        for kebutuhan_khusus in self.r_slice(kebutuhan_khususs):
            assert isinstance(kebutuhan_khusus, KebutuhanKhusus)

    def test_get_klasifikasi_lembaga(self, dapodik: Dapodik):
        klasifikasi_lembagas = dapodik.rest.klasifikasi_lembaga()
        for klasifikasi_lembaga in self.r_slice(klasifikasi_lembagas):
            assert isinstance(klasifikasi_lembaga, KlasifikasiLembaga)

    def test_get_kurikulum(self, dapodik: Dapodik):
        kurikulums = dapodik.rest.kurikulum()
        for kurikulum in self.r_slice(kurikulums):
            assert isinstance(kurikulum, Kurikulum)

    def test_get_lembaga_pengangkat(self, dapodik: Dapodik):
        lembaga_pengangkats = dapodik.rest.lembaga_pengangkat()
        for lembaga_pengangkat in self.r_slice(lembaga_pengangkats):
            assert isinstance(lembaga_pengangkat, LembagaPengangkat)

    def test_get_mata_pelajaran(self, dapodik: Dapodik):
        mata_pelajarans = dapodik.rest.mata_pelajaran()
        for mata_pelajaran in self.r_slice(mata_pelajarans):
            assert isinstance(mata_pelajaran, MataPelajaran)

    def test_get_mst_wilayah(self, dapodik: Dapodik):
        mst_wilayahs = dapodik.rest.mst_wilayah()
        for mst_wilayah in self.r_slice(mst_wilayahs):
            assert isinstance(mst_wilayah, MstWilayah)

    def test_get_pangkat_golongan(self, dapodik: Dapodik):
        pangkat_golongans = dapodik.rest.pangkat_golongan()
        for pangkat_golongan in self.r_slice(pangkat_golongans):
            assert isinstance(pangkat_golongan, PangkatGolongan)

    def test_get_pekerjaan(self, dapodik: Dapodik):
        pekerjaans = dapodik.rest.pekerjaan()
        for pekerjaan in self.r_slice(pekerjaans):
            assert isinstance(pekerjaan, Pekerjaan)

    def test_get_penghasilan(self, dapodik: Dapodik):
        penghasilans = dapodik.rest.penghasilan()
        for penghasilan in self.r_slice(penghasilans):
            assert isinstance(penghasilan, Penghasilan)

    def test_get_role_pengguna(self, dapodik: Dapodik):
        role_penggunas = dapodik.rest.role_pengguna()
        for role_pengguna in self.r_slice(role_penggunas):
            assert isinstance(role_pengguna, RolePengguna)

    def test_get_status_keaktifan_pegawai(self, dapodik: Dapodik):
        status_keaktifan_pegawais = dapodik.rest.status_keaktifan_pegawai()
        for status_keaktifan_pegawai in self.r_slice(status_keaktifan_pegawais):
            assert isinstance(status_keaktifan_pegawai, StatusKeaktifanPegawai)

    def test_get_status_kepegawaian(self, dapodik: Dapodik):
        status_kepegawaians = dapodik.rest.status_kepegawaian()
        for status_kepegawaian in self.r_slice(status_kepegawaians):
            assert isinstance(status_kepegawaian, StatusKepegawaian)

    def test_get_status_kepemilikan_sarpras(self, dapodik: Dapodik):
        status_kepemilikan_sarprass = dapodik.rest.status_kepemilikan_sarpras()
        for status_kepemilikan_sarpras in self.r_slice(status_kepemilikan_sarprass):
            assert isinstance(status_kepemilikan_sarpras, StatusKepemilikanSarpras)

    def test_get_sumber_air(self, dapodik: Dapodik):
        sumber_airs = dapodik.rest.sumber_air()
        for sumber_air in self.r_slice(sumber_airs):
            assert isinstance(sumber_air, SumberAir)

    def test_get_sumber_dana_sekolah(self, dapodik: Dapodik):
        sumber_dana_sekolahs = dapodik.rest.sumber_dana_sekolah()
        for sumber_dana_sekolah in self.r_slice(sumber_dana_sekolahs):
            assert isinstance(sumber_dana_sekolah, SumberDanaSekolah)

    def test_get_sumber_gaji(self, dapodik: Dapodik):
        sumber_gajis = dapodik.rest.sumber_gaji()
        for sumber_gaji in self.r_slice(sumber_gajis):
            assert isinstance(sumber_gaji, SumberGaji)

    def test_get_sumber_listrik(self, dapodik: Dapodik):
        sumber_listriks = dapodik.rest.sumber_listrik()
        for sumber_listrik in self.r_slice(sumber_listriks):
            assert isinstance(sumber_listrik, SumberListrik)

    def test_get_sync_log(self, dapodik: Dapodik):
        sync_logs = dapodik.rest.sync_log()
        for sync_log in self.r_slice(sync_logs):
            assert isinstance(sync_log, SyncLog)

    def test_get_tahun_ajaran(self, dapodik: Dapodik):
        tahun_ajarans = dapodik.rest.tahun_ajaran()
        for tahun_ajaran in self.r_slice(tahun_ajarans):
            assert isinstance(tahun_ajaran, TahunAjaran)

    def test_get_tingkat_pendidikan(self, dapodik: Dapodik):
        tingkat_pendidikans = dapodik.rest.tingkat_pendidikan()
        for tingkat_pendidikan in self.r_slice(tingkat_pendidikans):
            assert isinstance(tingkat_pendidikan, TingkatPendidikan)

    def test_get_waktu_penyelenggaraan(self, dapodik: Dapodik):
        waktu_penyelenggaraans = dapodik.rest.waktu_penyelenggaraan()
        for waktu_penyelenggaraan in self.r_slice(waktu_penyelenggaraans):
            assert isinstance(waktu_penyelenggaraan, WaktuPenyelenggaraan)
