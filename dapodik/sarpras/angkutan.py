import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Sekolah, Ptk, JenisSarana
from dapodik.utils.decorator import set_meta


@set_meta("id_angkutan", sekolah=Sekolah, ptk=Ptk, jenis_sarana=JenisSarana)
@attr.dataclass
class Angkutan(DapodikObject):
    id_angkutan: str
    sekolah_id: str
    ptk_id: Optional[str]
    jenis_sarana_id: int
    id_hapus_buku: Optional[str]
    kepemilikan_sarpras_id: str
    kd_kl: Optional[str]
    kd_satker: Optional[str]
    kd_brg: Optional[str]
    nup: Optional[int]
    kode_eselon1: Optional[str]
    nama_eselon1: Optional[str]
    kode_sub_satker: Optional[str]
    nama_sub_satker: Optional[str]
    nama: str
    spesifikasi: Optional[str]
    tgl_hapus_buku: Optional[str]
    merk: Optional[str]
    no_polisi: Optional[str]
    no_bpkb: Optional[str]
    alamat: Optional[str]
    asal_data: Optional[str]
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: Optional[str]
    jenis_sarana_id_str: str
    sekolah_id_str: str
    vld_count: int

    @property
    def kepemilikan_sarpras(self):
        # TODO API
        return self.kepemilikan_sarpras_id
