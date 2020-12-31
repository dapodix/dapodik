import attr
from typing import Any, List, Optional
from dapodik import (
    DapodikObject,
    PesertaDidikBaru,
    Sekolah,
    Agama,
    KebutuhanKhusus,
    JenisTinggal,
    AlatTransportasi,
)
from dapodik.utils.decorator import set_meta


@set_meta(
    "peserta_didik_id",
    sekolah=Sekolah,
    pdb=PesertaDidikBaru,
    agama=Agama,
    kebutuhan_khusus=KebutuhanKhusus,
    jenis_tinggal=JenisTinggal,
    alat_transportasi=AlatTransportasi,
)
@attr.dataclass
class PesertaDidik(DapodikObject):
    nama: str
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    nama_ibu_kandung: str
    sekolah_id: str
    pdb_id: str
    tahun_lahir_ayah: int
    tahun_lahir_ibu: int
    agama_id: int
    alamat_jalan: str
    rt: int
    rw: int
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_wilayah_str: str
    kode_pos: str
    lintang: int = 0
    bujur: int = 0
    nisn: str = ""
    nik: str = ""
    tahun_lahir_wali: int = 1980
    vld_count: int = 0
    kewarganegaraan: str = "ID"
    peserta_didik_id: str = "Admin.model.PesertaDidik-1"
    kewarganegaraan_str: str = ""
    no_kk: str = ""
    reg_akta_lahir: str = ""
    agama_id_str: str = ""
    kebutuhan_khusus_id: int = 0
    kebutuhan_khusus_id_str: str = ""
    jenis_tinggal_id: int = 1
    alat_transportasi_id: int = 1
    jenis_tinggal_id_str: str = ""
    alat_transportasi_id_str: str = ""
    no_kks: str = ""
    anak_keberapa: int = 1
    penerima_kps: int = 0
    no_kps: str = ""
    penerima_kip: int = 0
    no_kip: str = ""
    nm_kip: str = ""
    layak_pip: int = 0
    id_layak_pip: Optional[int] = None
    id_layak_pip_str: str = ""
    id_bank: str = ""
    id_bank_str: str = ""
    rekening_bank: str = ""
    nama_kcp: str = ""
    rekening_atas_nama: str = ""
    status_data: int = 0
    nama_ayah: str = ""
    nik_ayah: str = ""
    jenjang_pendidikan_ayah: int = 0
    jenjang_pendidikan_ayah_str: str = ""
    pekerjaan_id_ayah: int = 0
    pekerjaan_id_ayah_str: str = ""
    penghasilan_id_ayah: int = 0
    penghasilan_id_ayah_str: str = ""
    kebutuhan_khusus_id_ayah: int = 0
    kebutuhan_khusus_id_ayah_str: str = ""
    nik_ibu: str = ""
    jenjang_pendidikan_ibu: int = 0
    jenjang_pendidikan_ibu_str: str = ""
    pekerjaan_id_ibu: int = 1
    pekerjaan_id_ibu_str: str = ""
    penghasilan_id_ibu: int = 99
    penghasilan_id_ibu_str: str = ""
    kebutuhan_khusus_id_ibu: int = 0
    kebutuhan_khusus_id_ibu_str: str = ""
    nama_wali: str = ""
    nik_wali: str = ""
    jenjang_pendidikan_wali: int = 0
    jenjang_pendidikan_wali_str: str = ""
    pekerjaan_id_wali: int = 0
    pekerjaan_id_wali_str: str = ""
    penghasilan_id_wali: int = 0
    penghasilan_id_wali_str: str = ""
    nomor_telepon_rumah: str = ""
    nomor_telepon_seluler: str = ""
    email: str = ""
    kebutuhan_khusus_id_selector: List[Any] = attr.Factory(list)
    kebutuhan_khusus_id_selector_ayah: List[Any] = attr.Factory(list)
    kebutuhan_khusus_id_selector_ibu: List[Any] = attr.Factory(list)

    @property
    def params(self):
        return {
            "sekolah_id": self.dapodik.sekolah_id,
        }
