import attr
from datetime import datetime, date
from typing import List, Optional, TYPE_CHECKING
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
    tahun_lahir_wali: int
    jenjang_pendidikan_wali: int
    pekerjaan_id_wali: int
    penghasilan_id_wali: int
    kewarganegaraan: str
    registrasi_id: UUID
    jurusan_sp_id: Optional[str]
    sekolah_id: UUID
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
    rombel_saat_ini: str
    rombel: str
    id_bank_str: Optional[str]
    kewarganegaraan_str: str
    nomor_induk_pd: int
    yatim_piatu: bool
    konfirmasi_mutasi: int
    vld_count: Optional[int]
    # Metadata
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[int] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[UUID] = None
    _dapodik: Optional["Dapodik"] = None

    def __str__(self):
        return self.nama

    @attr.dataclass(kw_only=True)
    class Create:
        """Data untuk membuat peserta didik
        """
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

        def save(self, dapodik: Dapodik):
            pass
