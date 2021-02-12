from dapodik.base import dataclass


@dataclass
class Validasi:
    validasi_id: int
    table: str
    tipe: int
    keterangan: str

    def __str__(self) -> str:
        return self.keterangan

    @staticmethod
    def location() -> str:
        return ""


class ValidasiSekolah(Validasi):
    @staticmethod
    def location() -> str:
        return "sekolah"


class ValidasiPrasarana(Validasi):
    @staticmethod
    def location() -> str:
        return "prasarana"


class ValidasiPesertaDidik(Validasi):
    @staticmethod
    def location() -> str:
        return "peserta_didik"


class ValidasiPtk(Validasi):
    @staticmethod
    def location() -> str:
        return "ptk"


class ValidasiRombonganBelajar(Validasi):
    @staticmethod
    def location() -> str:
        return "rombongan_belajar"


class ValidasiPembelajaran(Validasi):
    @staticmethod
    def location() -> str:
        return "pembelajaran"


class ValidasiNilai(Validasi):
    @staticmethod
    def location() -> str:
        return "nilai"


class ValidasiReferensi(Validasi):
    @staticmethod
    def location() -> str:
        return "referensi"
