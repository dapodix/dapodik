import attr
from typing import Optional
from dapodik import DapodikObject, TingkatPendidikan, MataPelajaran, Kurikulum
from dapodik.utils.decorator import set_meta


@set_meta(
    "mata_pelajaran_kurikulum_id",
    kurikulum=Kurikulum,
    mata_pelajaran=MataPelajaran,
    tingkat_pendidikan=TingkatPendidikan,
)
@attr.dataclass
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
