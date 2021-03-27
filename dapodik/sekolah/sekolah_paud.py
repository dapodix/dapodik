from datetime import datetime

import attr


@attr.dataclass
class SekolahPaud:
    sekolah_id: str
    kategori_tk_id: int
    klasifikasi_lembaga_id: int
    sumber_dana_sekolah_id: str
    fasilitas_layanan_id: int
    jadwal_pmtas: str
    lembaga_pengangkat_id: int
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
