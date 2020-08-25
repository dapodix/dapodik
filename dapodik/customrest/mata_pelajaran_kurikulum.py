from dataclasses import dataclass
from typing import Optional
from dapodik import DapodikObject, TingkatPendidikan, MataPelajaran, Kurikulum
from dapodik.utils.decorator import set_meta


@set_meta('mata_pelajaran_kurikulum_id')
@dataclass(eq=False)
class MataPelajaranKurikulum(DapodikObject):
    mata_pelajaran_kurikulum_id: str
    kurikulum_id: int
    mata_pelajaran_id: int
    tingkat_pendidikan_id: str
    jumlah_jam: str
    jumlah_jam_maksimum: str
    wajib: str
    a_peminatan: str
    nama: str
    jam_mengajar_per_minggu: Optional[int]

    @property
    def mata_pelajaran_kurikulum(self):
        return self.mata_pelajaran_kurikulum_id

    @Kurikulum.prop
    def kurikulum(self) -> Kurikulum:
        return self.kurikulum_id  # type: ignore

    @MataPelajaran.prop
    def mata_pelajaran(self):
        return self.mata_pelajaran_id  # type: ignore

    @TingkatPendidikan.prop
    def tingkat_pendidikan(self) -> TingkatPendidikan:
        return self.tingkat_pendidikan_id  # type: ignore
