from datetime import datetime, date
from typing import Optional
from uuid import UUID
from dapodik.base import dataclass, field, freeze


@dataclass
class PesertaDidik:
    peserta_didik_id: UUID = freeze(default="Admin.model.PesertaDidik-1")
    nama: str = freeze()
    jenis_kelamin: str = freeze()
    nisn: str = freeze(default="")
    nik: str = freeze(default="")
    no_kk: str
    tempat_lahir: str = freeze()
    tanggal_lahir: date = freeze()
    agama_id: int
    kebutuhan_khusus_id: int
    alamat_jalan: str
    rt: int
    rw: int
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: int
    lintang: str = "0"
    bujur: str = "0"
    jenis_tinggal_id: int
    alat_transportasi_id: int
    nik_ayah: str
    nik_ibu: str
    anak_keberapa: int = 1
    nik_wali: Optional[str]
    nomor_telepon_rumah: Optional[str]
    nomor_telepon_seluler: Optional[str]
    email: Optional[str]
    penerima_kps: int
    no_kps: Optional[str]
    layak_pip: int
    penerima_kip: int
    no_kip: Optional[str]
    nm_kip: int
    no_kks: Optional[str]
    reg_akta_lahir: str
    id_layak_pip: Optional[int]
    id_bank: Optional[int] = freeze()
    rekening_bank: Optional[str] = freeze()
    nama_kcp: Optional[str] = freeze()
    rekening_atas_nama: Optional[str] = freeze()
    status_data: int = freeze()
    nama_ayah: str
    tahun_lahir_ayah: int
    jenjang_pendidikan_ayah: int
    pekerjaan_id_ayah: int
    penghasilan_id_ayah: int
    kebutuhan_khusus_id_ayah: int
    nama_ibu_kandung: str = freeze()
    tahun_lahir_ibu: int
    jenjang_pendidikan_ibu: int
    penghasilan_id_ibu: int
    pekerjaan_id_ibu: int
    kebutuhan_khusus_id_ibu: int
    nama_wali: Optional[str]
    tahun_lahir_wali: int
    jenjang_pendidikan_wali: int
    pekerjaan_id_wali: int
    penghasilan_id_wali: int
    kewarganegaraan: str = field(default="ID")
    create_date: datetime = freeze()
    last_update: datetime = freeze()
    soft_delete: int = freeze()
    last_sync: datetime = freeze()
    updater_id: UUID = freeze()
    registrasi_id: UUID = freeze()
    jurusan_sp_id: None
    sekolah_id: UUID = freeze()
    jenis_pendaftaran_id: int
    nipd: int
    tanggal_masuk_sekolah: date
    jenis_keluar_id: Optional[int]
    tanggal_keluar: Optional[datetime]
    keterangan: str
    no_skhun: Optional[str]
    no_peserta_ujian: Optional[str]
    no_seri_ijazah: Optional[str]
    a_pernah_paud: int
    a_pernah_tk: int
    sekolah_asal: Optional[str]
    id_hobby: int
    id_cita: int
    nama_sorter: str
    jenis_pendaftaran_id_str: str
    ket_keluar: Optional[str]
    anggota_rombel_id: Optional[UUID]
    tingkat_pendidikan_id: Optional[int]
    rombel_saat_ini: None
    rombel: None
    id_bank_str: None
    kewarganegaraan_str: str = ""
    nomor_induk_pd: int
    yatim_piatu: bool
    konfirmasi_mutasi: int
    vld_count: int = 0
