import attr
from datetime import date, datetime
from typing import Any, Optional
from uuid import UUID

from dapodik.enums import JenisKelamin
from dapodik.gtk.enums import PtkAktif, PtkInduk


@attr.dataclass(slots=True)
class Ptk:
    ptk_terdaftar_id: UUID
    ptk_id: UUID
    sekolah_id: UUID
    jenis_keluar_id: Optional[int]
    tahun_ajaran_id: str
    nomor_surat_tugas: str
    tanggal_surat_tugas: date
    ptk_induk: PtkInduk
    tmt_tugas: date
    aktif_bulan_01: PtkAktif
    aktif_bulan_02: PtkAktif
    aktif_bulan_03: PtkAktif
    aktif_bulan_04: PtkAktif
    aktif_bulan_05: PtkAktif
    aktif_bulan_06: PtkAktif
    aktif_bulan_07: PtkAktif
    aktif_bulan_08: PtkAktif
    aktif_bulan_09: PtkAktif
    aktif_bulan_10: PtkAktif
    aktif_bulan_11: PtkAktif
    aktif_bulan_12: PtkAktif
    tgl_ptk_keluar: Optional[date]
    jenis_keluar_id_str: Optional[str]
    nama: str
    nip: Optional[str]
    jenis_kelamin: JenisKelamin
    tempat_lahir: str
    tanggal_lahir: date
    nik: Optional[str]
    no_kk: Optional[str]
    niy_nigk: Optional[str]
    nuptk: Optional[str]
    nuks: Optional[str]
    status_kepegawaian_id: int
    jenis_ptk_id: int
    pengawas_bidang_studi_id: Optional[int]
    agama_id: int
    alamat_jalan: Optional[str]
    rt: str
    rw: str
    nama_dusun: Optional[str]
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: Optional[str]
    lintang: Optional[str]
    bujur: Optional[str]
    no_telepon_rumah: Optional[str]
    no_hp: Optional[str]
    email: Optional[str]
    status_keaktifan_id: int
    sk_cpns: Optional[str]
    tgl_cpns: Optional[date]
    sk_pengangkatan: str
    tmt_pengangkatan: date
    lembaga_pengangkat_id: int
    pangkat_golongan_id: int
    keahlian_laboratorium_id: int
    sumber_gaji_id: int
    nama_ibu_kandung: str
    status_perkawinan: int
    nama_suami_istri: Optional[str]
    nip_suami_istri: Optional[str]
    pekerjaan_suami_istri: int
    tmt_pns: Optional[date]
    sudah_lisensi_kepala_sekolah: int
    jumlah_sekolah_binaan: Optional[int]
    pernah_diklat_kepengawasan: int
    nm_wp: Optional[str]
    status_data: Optional[int]
    karpeg: Optional[Any]
    karpas: Optional[Any]
    mampu_handle_kk: int
    keahlian_braille: int
    keahlian_bhs_isyarat: int
    npwp: Optional[str]
    kewarganegaraan: str
    id_bank: Optional[int]
    rekening_bank: Optional[str]
    rekening_atas_nama: Optional[str]
    pengguna_id: Optional[UUID] = None
    username: Optional[str] = None
    password: Optional[str] = None
    jabatan_lembaga: Optional[str] = None
    verifikasi_email: Optional[bool] = None
    jenis_ptk_id_str: Optional[str] = None
    blob_id: Optional[str] = None
    vld_count: int = 0
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[int] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[UUID] = None
