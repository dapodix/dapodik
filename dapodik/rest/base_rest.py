from dapodik import (
    BaseDapodik,
    Rest,
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
    JenisRombel,
    JenisSarana,
    JenisTinggal,
    JenjangPendidikan,
    Jurusan,
    KategoriTk,
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
            self.Agama = Rest(self, Agama, 'rest/Agama')
            self.Akreditasi = Rest(self, Akreditasi, 'rest/Akreditasi')
            self.AksesInternet = Rest(self, AksesInternet,
                                      'rest/AksesInternet')
            self.AlatTransportasi = Rest(self, AlatTransportasi,
                                         'rest/AlatTransportasi')
            self.Bank = Rest(self, Bank, 'rest/Bank')
            self.BentukLembaga = Rest(self, BentukLembaga,
                                      'rest/BentukLembaga')
            self.Biblio = Rest(self, Biblio, 'rest/Biblio')
            self.ChildDelete = Rest(self, ChildDelete, 'rest/ChildDelete')
            self.FasilitasLayanan = Rest(self, FasilitasLayanan,
                                         'rest/FasilitasLayanan')
            self.Gmd = Rest(self, Gmd, 'rest/Gmd')
            self.JadwalPaud = Rest(self, JadwalPaud, 'rest/JadwalPaud')
            self.JenisGugus = Rest(self, JenisGugus, 'rest/JenisGugus')
            self.JenisHapusBuku = Rest(self, JenisHapusBuku,
                                       'rest/JenisHapusBuku')
            self.JenisKeluar = Rest(self, JenisKeluar, 'rest/JenisKeluar')
            self.JenisLk = Rest(self, JenisLk, 'rest/JenisLk')
            self.JenisPendaftaran = Rest(self, JenisPendaftaran,
                                         'rest/JenisPendaftaran')
            self.JenisPrasarana = Rest(self, JenisPrasarana,
                                       'rest/JenisPrasarana')
            self.JenisRombel = Rest(self, JenisRombel, 'rest/JenisRombel')
            self.JenisSarana = Rest(self, JenisSarana, 'rest/JenisSarana')
            self.JenisTinggal = Rest(self, JenisTinggal, 'rest/JenisTinggal')
            self.JenjangPendidikan = Rest(self, JenjangPendidikan,
                                          'rest/JenjangPendidikan')
            self.Jurusan = Rest(self, Jurusan, 'rest/Jurusan')
            self.KategoriTk = Rest(self, KategoriTk, 'rest/KategoriTk')
            self.KebutuhanKhusus = Rest(self, KebutuhanKhusus,
                                        'rest/KebutuhanKhusus')
            self.KlasifikasiLembaga = Rest(self, KlasifikasiLembaga,
                                           'rest/KlasifikasiLembaga')
            self.Kurikulum = Rest(self, Kurikulum, 'rest/Kurikulum')
            self.LembagaPengangkat = Rest(self, LembagaPengangkat,
                                          'rest/LembagaPengangkat')
            self.MataPelajaran = Rest(self, MataPelajaran,
                                      'rest/MataPelajaran')
            self.MstWilayah = Rest(self, MstWilayah, 'rest/MstWilayah')
            self.PangkatGolongan = Rest(self, PangkatGolongan,
                                        'rest/PangkatGolongan')
            self.Pekerjaan = Rest(self, Pekerjaan, 'rest/Pekerjaan')
            self.Penghasilan = Rest(self, Penghasilan, 'rest/Penghasilan')
            self.RolePengguna = Rest(self, RolePengguna, 'rest/RolePengguna')
            self.StatusKeaktifanPegawai = Rest(self, StatusKeaktifanPegawai,
                                               'rest/StatusKeaktifanPegawai')
            self.StatusKepegawaian = Rest(self, StatusKepegawaian,
                                          'rest/StatusKepegawaian')
            self.StatusKepemilikanSarpras = Rest(
                self, StatusKepemilikanSarpras,
                'rest/StatusKepemilikanSarpras')
            self.SumberAir = Rest(self, SumberAir, 'rest/SumberAir')
            self.SumberDanaSekolah = Rest(self, SumberDanaSekolah,
                                          'rest/SumberDanaSekolah')
            self.SumberGaji = Rest(self, SumberGaji, 'rest/SumberGaji')
            self.SumberListrik = Rest(self, SumberListrik,
                                      'rest/SumberListrik')
            self.SyncLog = Rest(self, SyncLog, 'rest/SyncLog')
            self.TahunAjaran = Rest(self, TahunAjaran, 'rest/TahunAjaran')
            self.TingkatPendidikan = Rest(self, TingkatPendidikan,
                                          'rest/TingkatPendidikan')
            self.WaktuPenyelenggaraan = Rest(self, WaktuPenyelenggaraan,
                                             'rest/WaktuPenyelenggaraan')
            self.logger.debug('Berhasil memulai rest')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
