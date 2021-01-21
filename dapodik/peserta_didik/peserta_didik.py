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
    no_kk: str = ""
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
    kode_pos: Optional[int] = None
    lintang: str = "0"
    bujur: str = "0"
    jenis_tinggal_id: int = 1
    alat_transportasi_id: int = 1
    nik_ayah: str
    nik_ibu: str
    anak_keberapa: int = 1
    nik_wali: Optional[str]
    nomor_telepon_rumah: Optional[str]
    nomor_telepon_seluler: Optional[str]
    email: Optional[str] = ""
    penerima_kps: int = 0
    no_kps: Optional[str] = None
    layak_pip: int = 0
    penerima_kip: int = 0
    no_kip: Optional[str] = None
    nm_kip: Optional[str] = None
    no_kks: Optional[str] = None
    reg_akta_lahir: str = ""
    id_layak_pip: Optional[int] = None
    id_bank: Optional[int] = freeze(default=None)
    rekening_bank: Optional[str] = freeze(default=None)
    nama_kcp: Optional[str] = freeze(default=None)
    rekening_atas_nama: Optional[str] = freeze(default=None)
    status_data: Optional[int] = freeze(default=None)
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
    registrasi_id: UUID = freeze()
    jurusan_sp_id: Optional[str] = freeze()
    sekolah_id: UUID = freeze()
    jenis_pendaftaran_id: int
    nipd: int
    tanggal_masuk_sekolah: date
    jenis_keluar_id: Optional[int]
    tanggal_keluar: Optional[datetime]
    keterangan: str = freeze()
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
    rombel_saat_ini: str = freeze(default=None)
    rombel: str = freeze(default=None)
    id_bank_str: Optional[str] = freeze(default=None)
    kewarganegaraan_str: str = ""
    nomor_induk_pd: int
    yatim_piatu: bool = False
    konfirmasi_mutasi: int = freeze(default=0)
    vld_count: Optional[int] = freeze(default=0)
    # Metadata
    create_date: Optional[datetime] = freeze(default=None)
    last_update: Optional[datetime] = freeze(default=None)
    soft_delete: Optional[int] = freeze(default=None)
    last_sync: Optional[datetime] = freeze(default=None)
    updater_id: Optional[UUID] = freeze(default=None)

    def __str__(self):
        return self.nama
