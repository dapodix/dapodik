from dataclasses import dataclass
from datetime import datetime
from dapodik import (
    DapodikObject,
    SekolahMixin,
    KategoriTk,
    KlasifikasiLembaga,
    SumberDanaSekolah,
    FasilitasLayanan,
    LembagaPengangkat,
)
from dapodik.utils.decorator import set_meta


@set_meta('sekolah_id')
@dataclass(eq=False)
class BaseSekolahPaud(DapodikObject):
    sekolah_id: str
    kategori_tk_id: str
    klasifikasi_lembaga_id: str
    sumber_dana_sekolah_id: str
    fasilitas_layanan_id: str
    jadwal_pmtas: str
    lembaga_pengangkat_id: str
    jadwal_ddtk: str
    freq_parenting: str
    bentuk_lembaga_id: str
    jadwal_kesehatan: str
    izin_paud: str
    pencatatan_ddtk: str
    rujukan_ddtk: str
    pelaksanaan_parenting: str
    parenting_kpo: str
    parenting_kelas: str
    parenting_kegiatan: str
    parenting_konsultasi: str
    parenting_kunjungan: str
    parenting_lainnya: str
    nilk: str
    nilm: str
    no_penetapan_pnf: str
    tanggal_penetapan_pnf: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str


@dataclass
class SekolahPaud(BaseSekolahPaud, SekolahMixin):
    @property
    @KategoriTk.getter
    def kategori_tk(self) -> KategoriTk:
        return self.kategori_tk_id

    @property
    @KlasifikasiLembaga.getter
    def klasifikasi_lembaga(self) -> KlasifikasiLembaga:
        return self.klasifikasi_lembaga_id

    @property
    @SumberDanaSekolah.getter
    def sumber_dana_sekolah(self) -> SumberDanaSekolah:
        return self.sumber_dana_sekolah_id

    @property
    @FasilitasLayanan.getter
    def fasilitas_layanan(self) -> FasilitasLayanan:
        return self.fasilitas_layanan_id

    @property
    @LembagaPengangkat.getter
    def lembaga_pengangkat(self) -> LembagaPengangkat:
        return self.lembaga_pengangkat_id
