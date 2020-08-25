from dataclasses import dataclass
from dapodik import DapodikObject, Sekolah, JenisPendaftaran
from dapodik.utils.decorator import set_meta


@set_meta('pdb_id')
@dataclass(eq=False)
class PesertaDidikBaru(DapodikObject):
    sekolah_id: str
    nama_pd: str
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    nama_ibu_kandung: str
    nisn: str = ""
    nik: str = ""
    tahun_ajaran_id: int = 2020
    jenis_pendaftaran_id: int = 1
    sudah_diproses: int = 0
    berhasil_diproses: int = 0
    peserta_didik_id: str = ""
    pdb_id: str = "Admin.model.PesertaDidikBaru-1"
    sekolah_id_str: str = ""
    tahun_ajaran_id_str: str = ""
    jenis_pendaftaran_id_str: str = ""
    peserta_didik_id_str: str = ""

    @Sekolah.prop
    def sekolah(self) -> Sekolah:
        return self.sekolah_id  # type: ignore

    @property
    def tahun_ajaran(self):
        # TODO API
        return self.tahun_ajaran_id

    @JenisPendaftaran.prop
    def jenis_pendaftaran(self) -> JenisPendaftaran:
        return self.jenis_pendaftaran_id  # type: ignore

    @property
    def peserta_didik(self):
        return self.peserta_didik_id
