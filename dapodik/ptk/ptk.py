from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import (
    DapodikObject,
    Agama,
    Bank,
    JenisKeluar,
    Pengguna,
    StatusKeaktifanPegawai,
    StatusKepegawaian,
    PangkatGolongan,
    Sekolah,
    SumberGaji,
)
from dapodik.utils.decorator import set_meta


@set_meta('ptk_id')
@dataclass(eq=False)
class Ptk(DapodikObject):
    ptk_terdaftar_id: str
    ptk_id: str
    sekolah_id: str
    jenis_keluar_id: Optional[str]
    tahun_ajaran_id: str
    nomor_surat_tugas: str
    tanggal_surat_tugas: str
    ptk_induk: str
    tmt_tugas: str
    aktif_bulan_0int: str
    aktif_bulan_02: str
    aktif_bulan_03: str
    aktif_bulan_04: str
    aktif_bulan_05: str
    aktif_bulan_06: str
    aktif_bulan_07: str
    aktif_bulan_08: str
    aktif_bulan_09: str
    aktif_bulan_int0: str
    aktif_bulan_intint: str
    aktif_bulan_12: str
    tgl_ptk_keluar: Optional[str]
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    jenis_keluar_id_str: str
    nama: str
    nip: Optional[str]
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    nik: str
    no_kk: Optional[str]
    niy_nigk: Optional[str]
    nuptk: str
    nuks: Optional[str]
    status_kepegawaian_id: int
    jenis_ptk_id: str
    pengawas_bidang_studi_id: int
    agama_id: int
    alamat_jalan: str
    rt: str
    rw: str
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: Optional[str]
    lintang: Optional[str]
    bujur: Optional[str]
    no_telepon_rumah: Optional[str]
    no_hp: str
    email: str
    status_keaktifan_id: str
    sk_cpns: Optional[str]
    tgl_cpns: Optional[str]
    sk_pengangkatan: str
    tmt_pengangkatan: str
    lembaga_pengangkat_id: str
    pangkat_golongan_id: str
    keahlian_laboratorium_id: 99
    sumber_gaji_id: str
    nama_ibu_kandung: str
    status_perkawinan: str
    nama_suami_istri: str
    nip_suami_istri: Optional[str]
    pekerjaan_suami_istri: int
    tmt_pns: Optional[str]
    sudah_lisensi_kepala_sekolah: str
    jumlah_sekolah_binaan: int
    pernah_diklat_kepengawasan: str
    nm_wp: str
    status_data: int
    karpeg: Optional[str]
    karpas: Optional[str]
    mampu_handle_kk: int
    keahlian_braille: str
    keahlian_bhs_isyarat: str
    npwp: str
    kewarganegaraan: str
    id_bank: Optional[str]
    rekening_bank: Optional[str]
    rekening_atas_nama: Optional[str]
    blob_id: Optional[str]
    pengguna_id: str
    username: str
    password: str
    jabatan_lembaga: Optional[str]
    verifikasi_email: bool
    jenis_ptk_id_str: str
    vld_count: int

    @Sekolah.property
    def sekolah(self) -> Sekolah:
        return self.sekolah_id

    @property
    def ptk_terdaftar(self):
        return self.ptk_terdaftar_id

    @JenisKeluar.property
    def jenis_keluar(self) -> JenisKeluar:
        return self.jenis_keluar_id

    @property
    def tahun_ajaran(self):
        # TODO API
        return self.tahun_ajaran_id

    @property
    def updater(self):
        return self.updater_id

    @StatusKepegawaian.property
    def status_kepegawaian(self) -> StatusKepegawaian:
        return self.status_kepegawaian_id

    @property
    def jenis_ptk(self):
        # TODO API
        return self.jenis_ptk_id

    @property
    def pengawas_bidang_studi(self):
        # TODO API
        return self.pengawas_bidang_studi_id

    @Agama.property
    def agama(self) -> Agama:
        return self.agama_id

    @StatusKeaktifanPegawai.property
    def status_keaktifan(self) -> StatusKeaktifanPegawai:
        return self.status_keaktifan_id

    @property
    def lembaga_pengangkat(self):
        # TODO API
        return self.lembaga_pengangkat_id

    @PangkatGolongan.property
    def pangkat_golongan(self) -> PangkatGolongan:
        return self.pangkat_golongan_id

    @property
    def keahlian_laboratorium(self):
        # TODO API
        return self.keahlian_laboratorium_id

    @SumberGaji.property
    def sumber_gaji(self) -> SumberGaji:
        return self.sumber_gaji_id

    @property
    def blob(self):
        # TODO API
        return self.blob_id

    @Pengguna.property
    def pengguna(self) -> Pengguna:
        return self.pengguna_id

    @Bank.property
    def bank(self) -> Bank:
        return self.bank
