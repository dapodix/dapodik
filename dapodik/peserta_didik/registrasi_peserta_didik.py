from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class RegistrasiPesertaDidik:
    peserta_didik_id: str = freeze()
    sekolah_id: str = freeze()
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
