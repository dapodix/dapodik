import attr
from datetime import date
from typing import List, Optional, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from dapodik import Dapodik
from . import PesertaDidik


@attr.dataclass(kw_only=True)
class CreatePesertaDidik:
    """Data untuk membuat peserta didik"""

    # Data Pribadi
    nama: str
    jenis_kelamin: str
    nisn: str
    nik: str
    no_kk: str
    tempat_lahir: str
    tanggal_lahir: date
    reg_akta_lahir: str = ""
    kebutuhan_khusus_id: int = 0
    agama_id: int
    alamat_jalan: str
    rt: int = 0
    rw: int = 0
    nama_dusun: str
    kode_wilayah: str
    kode_wilayah_str: str
    desa_kelurahan: str
    kode_pos: int
    lintang: int
    bujur: int
    jenis_tinggal_id: int
    alat_transportasi_id: int
    anak_keberapa: int = 1
    penerima_kps: int = 0
    penerima_kip: int = 0
    layak_pip: int = 0
    id_layak_pip: Optional[int] = None
    sekolah_id: UUID
    kewarganegaraan: str = "ID"
    no_kks: str = ""
    no_kps: str = ""
    no_kip: str = ""
    nm_kip: int = 0
    # Data Ayah Kandung
    nama_ayah: str
    nik_ayah: str
    tahun_lahir_ayah: int
    jenjang_pendidikan_ayah: int
    pekerjaan_id_ayah: int
    penghasilan_id_ayah: int
    kebutuhan_khusus_id_ayah: int = 0
    # Data Ibu Kandung
    nama_ibu_kandung: str
    nik_ibu: str
    tahun_lahir_ibu: int
    jenjang_pendidikan_ibu: int
    pekerjaan_id_ibu: int
    penghasilan_id_ibu: int
    kebutuhan_khusus_id_ibu: int = 0
    # Data Wali
    nama_wali: str = ""
    nik_wali: str = ""
    tahun_lahir_wali: int
    jenjang_pendidikan_wali: int = 0
    pekerjaan_id_wali: int = 0
    penghasilan_id_wali: int = 0
    # Kontak
    nomor_telepon_rumah: str = ""
    nomor_telepon_seluler: str = ""
    email: str = ""
    # Bank PIP
    id_bank: str = ""
    rekening_bank: str = ""
    nama_kcp: str = ""
    rekening_atas_nama: str = ""
    # Etc
    peserta_didik_id: str = "Admin.model.PesertaDidik-1"
    kewarganegaraan_str: str = ""
    agama_id_str: str = ""
    status_data: int = 0
    pdb_id: Optional[str] = None
    kebutuhan_khusus_id_str: str = ""
    jenis_tinggal_id_str: str = ""
    alat_transportasi_id_str: str = ""
    id_layak_pip_str: str = ""
    id_bank_str: str = ""
    jenjang_pendidikan_ayah_str: str = ""
    jenjang_pendidikan_ibu_str: str = ""
    jenjang_pendidikan_wali_str: str = ""
    pekerjaan_id_ayah_str: str = ""
    pekerjaan_id_ibu_str: str = ""
    pekerjaan_id_wali_str: str = ""
    penghasilan_id_ayah_str: str = ""
    penghasilan_id_ibu_str: str = ""
    penghasilan_id_wali_str: str = ""
    kebutuhan_khusus_id_ayah_str: str = ""
    kebutuhan_khusus_id_ibu_str: str = ""
    kebutuhan_khusus_id_selector: List[int] = attr.ib(factory=list)
    kebutuhan_khusus_id_selector_ayah: List[int] = attr.ib(factory=list)
    kebutuhan_khusus_id_selector_ibu: List[int] = attr.ib(factory=list)
    vld_count: int = 0

    def save(
        self,
        dapodik: "Dapodik",
        pd_module: str = "pdterdaftar",
        limit: int = 25,
        ascending: str = "nama",
    ) -> PesertaDidik:
        query = {
            "sekolah_id": self.sekolah_id,
            "pd_module": pd_module,
            "limit": limit,
            "ascending": ascending,
        }
        return dapodik._post_rest(
            path="PesertaDidik", cl=PesertaDidik, data=self, query=query
        )
