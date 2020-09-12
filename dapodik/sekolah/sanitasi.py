from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, SumberAir, Sekolah, Semester
from dapodik.utils.decorator import set_meta


@set_meta('sanitasi_id',
          sekolah=Sekolah,
          semester=Semester,
          sumber_air=SumberAir)
@dataclass(eq=False)
class Sanitasi(DapodikObject):
    sekolah_id: str
    semester_id: str
    sumber_air_id: str
    sumber_air_minum_id: str
    ketersediaan_air: str
    kecukupan_air: str
    minum_siswa: str
    memproses_air: str
    siswa_bawa_air: str
    toilet_siswa_laki: str
    toilet_siswa_perempuan: str
    toilet_siswa_kk: str
    toilet_siswa_kecil: str
    jml_jamban_l_g: str
    jml_jamban_l_tg: str
    jml_jamban_p_g: str
    jml_jamban_p_tg: str
    jml_jamban_lp_g: str
    jml_jamban_lp_tg: str
    tempat_cuci_tangan: str
    tempat_cuci_tangan_rusak: str
    a_sabun_air_mengalir: str
    jamban_difabel: str
    tipe_jamban: str
    a_sedia_pembalut: str
    kegiatan_cuci_tangan: Optional[str]
    pembuangan_air_limbah: Optional[str]
    a_kuras_septitank: Optional[str]
    a_memiliki_solokan: Optional[str]
    a_tempat_sampah_kelas: str
    a_tempat_sampah_tutup_p: str
    a_cermin_jamban_p: str
    a_memiliki_tps: str
    a_tps_angkut_rutin: str
    a_anggaran_sanitasi: str
    a_melibatkan_sanitasi_siswa: str
    a_kemitraan_san_daerah: Optional[str]
    a_kemitraan_san_puskesmas: Optional[str]
    a_kemitraan_san_swasta: Optional[str]
    a_kemitraan_san_non_pem: Optional[str]
    kie_guru_cuci_tangan: Optional[str]
    kie_guru_haid: Optional[str]
    kie_guru_perawatan_toilet: Optional[str]
    kie_guru_keamanan_pangan: Optional[str]
    kie_guru_minum_air: Optional[str]
    kie_kelas_cuci_tangan: Optional[str]
    kie_kelas_haid: Optional[str]
    kie_kelas_perawatan_toilet: Optional[str]
    kie_kelas_keamanan_pangan: Optional[str]
    kie_kelas_minum_air: Optional[str]
    kie_toilet_cuci_tangan: Optional[str]
    kie_toilet_haid: Optional[str]
    kie_toilet_perawatan_toilet: Optional[str]
    kie_toilet_keamanan_pangan: Optional[str]
    kie_toilet_minum_air: Optional[str]
    kie_selasar_cuci_tangan: Optional[str]
    kie_selasar_haid: Optional[str]
    kie_selasar_perawatan_toilet: Optional[str]
    kie_selasar_keamanan_pangan: Optional[str]
    kie_selasar_minum_air: Optional[str]
    kie_uks_cuci_tangan: Optional[str]
    kie_uks_haid: Optional[str]
    kie_uks_perawatan_toilet: Optional[str]
    kie_uks_keamanan_pangan: Optional[str]
    kie_uks_minum_air: Optional[str]
    kie_kantin_cuci_tangan: Optional[str]
    kie_kantin_haid: Optional[str]
    kie_kantin_perawatan_toilet: Optional[str]
    kie_kantin_keamanan_pangan: Optional[str]
    kie_kantin_minum_air: Optional[str]
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    semester_id_str: str
    sanitasi_id: str

    @property
    def sumber_air_minum(self):
        # TODO API
        return self.sumber_air_minum_id
