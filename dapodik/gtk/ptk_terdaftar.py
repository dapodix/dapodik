import attr
from datetime import date, datetime
from typing import Optional
from uuid import UUID

from dapodik.gtk.enums import PtkAktif


@attr.dataclass(slots=True)
class PtkTerdaftar:
    ptk_terdaftar_id: UUID
    ptk_id: UUID
    sekolah_id: UUID
    jenis_keluar_id: Optional[int]
    tahun_ajaran_id: str
    nomor_surat_tugas: str
    tanggal_surat_tugas: date
    ptk_induk: int
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
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: int = 0
    last_sync: Optional[datetime] = None
    updater_id: Optional[UUID] = None
    ptk_id_str: Optional[str] = None
    sekolah_id_str: Optional[str] = None
    tahun_ajaran_id_str: Optional[str] = None
