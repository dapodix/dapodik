from dataclasses import dataclass
from typing import Optional
from dapodik import (DapodikObject, PesertaDidik, Sekolah, JenisPendaftaran,
                     JenisKeluar)
from dapodik.utils.decorator import set_meta


@set_meta('registrasi_id')
@dataclass(eq=False)
class RegistrasiPesertaDidik(DapodikObject):
    peserta_didik_id: str
    sekolah_id: str
    tanggal_masuk_sekolah: str
    nipd: str = ""
    registrasi_id: Optional[str] = "Admin.model.RegistrasiPesertaDidik-1"
    jurusan_sp_id: str = ""
    jenis_pendaftaran_id: int = 1
    jenis_keluar_id: str = ""
    tanggal_keluar: Optional[str] = None
    keterangan: str = ""
    no_skhun: str = ""
    id_hobby: int = -1
    id_cita: int = -1
    no_seri_ijazah: str = ""
    no_peserta_ujian: str = ""
    sekolah_asal: str = ""
    jurusan_sp_id_str: str = ""
    peserta_didik_id_str: str = ""
    sekolah_id_str: str = ""
    jenis_pendaftaran_id_str: str = ""
    id_hobby_str: str = ""
    id_cita_str: str = ""
    jenis_keluar_id_str: str = ""
    a_pernah_paud: int = 0
    a_pernah_tk: int = 0

    @PesertaDidik.prop
    def peserta_didik(self) -> PesertaDidik:
        return self.peserta_didik_id  # type: ignore

    @Sekolah.prop
    def sekolah(self) -> Sekolah:
        return self.sekolah_id  # type: ignore

    @property
    def registrasi(self):
        return self

    @property
    def jurusan_sp(self):
        # TODO API
        return self.jurusan_sp_id

    @JenisPendaftaran.prop
    def jenis_pendaftaran(self) -> JenisPendaftaran:
        return self.jenis_pendaftaran_id  # type: ignore

    @JenisKeluar.prop
    def jenis_keluar(self) -> JenisKeluar:
        return self.jenis_keluar_id  # type: ignore
