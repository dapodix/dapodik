import attr
from datetime import datetime, date
from typing import Optional, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from dapodik import Dapodik


@attr.dataclass
class PesertaDidik:
    peserta_didik_id: UUID
    nama: str
    jenis_kelamin: str
    nisn: str
    nik: str
    no_kk: str
    tempat_lahir: str
    tanggal_lahir: date
    agama_id: int
    kebutuhan_khusus_id: int
    alamat_jalan: str
    rt: int
    rw: int
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: Optional[int]
    lintang: str
    bujur: str
    jenis_tinggal_id: int
    alat_transportasi_id: int
    nik_ayah: str
    nik_ibu: str
    anak_keberapa: int
    nik_wali: Optional[str]
    nomor_telepon_rumah: Optional[str]
    nomor_telepon_seluler: Optional[str]
    email: Optional[str]
    penerima_kps: int
    no_kps: Optional[str]
    layak_pip: int
    penerima_kip: int
    no_kip: Optional[str]
    nm_kip: Optional[str]
    no_kks: Optional[str]
    reg_akta_lahir: str
    id_layak_pip: Optional[int]
    id_bank: Optional[int]
    rekening_bank: Optional[str]
    nama_kcp: Optional[str]
    rekening_atas_nama: Optional[str]
    status_data: Optional[int]
    nama_ayah: str
    tahun_lahir_ayah: int
    jenjang_pendidikan_ayah: int
    pekerjaan_id_ayah: int
    penghasilan_id_ayah: int
    kebutuhan_khusus_id_ayah: int
    nama_ibu_kandung: str
    tahun_lahir_ibu: int
    jenjang_pendidikan_ibu: int
    penghasilan_id_ibu: int
    pekerjaan_id_ibu: int
    kebutuhan_khusus_id_ibu: int
    nama_wali: Optional[str]
    tahun_lahir_wali: Optional[str]
    jenjang_pendidikan_wali: int
    pekerjaan_id_wali: int
    penghasilan_id_wali: int
    kewarganegaraan: str
    yatim_piatu: Optional[bool] = None
    nama_sorter: Optional[str] = None
    rombel_saat_ini: Optional[str] = None
    rombel: Optional[str] = None
    # Ujian
    no_skhun: Optional[str] = None
    no_peserta_ujian: Optional[str] = None
    no_seri_ijazah: Optional[str] = None
    # Meta
    keterangan: Optional[str] = None
    # Registrasi
    nipd: Optional[int] = None
    nomor_induk_pd: Optional[int] = None
    tanggal_masuk_sekolah: Optional[date] = None
    sekolah_asal: Optional[str] = None
    a_pernah_paud: Optional[int] = None
    a_pernah_tk: Optional[int] = None
    id_hobby: Optional[int] = None
    id_cita: Optional[int] = None
    jenis_keluar_id: Optional[int] = None
    tanggal_keluar: Optional[datetime] = None
    konfirmasi_mutasi: Optional[int] = None
    ket_keluar: Optional[str] = None
    anggota_rombel_id: Optional[UUID] = None
    tingkat_pendidikan_id: Optional[int] = None
    jenis_pendaftaran_id: Optional[int] = None
    jenis_pendaftaran_id_str: str = ""
    jurusan_sp_id: Optional[str] = None
    sekolah_id: Optional[UUID] = None
    registrasi_id: Optional[UUID] = None
    vld_count: Optional[int] = None
    # Str
    id_bank_str: Optional[str] = None
    kewarganegaraan_str: Optional[str] = None
    # Metadata
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[int] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[UUID] = None
    _dapodik: Optional["Dapodik"] = None

    def __str__(self):
        return self.nama
