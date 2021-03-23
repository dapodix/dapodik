import attr


@attr.dataclass
class Validasi:
    validasi_id: int
    table: str
    tipe: int
    keterangan: str

    def __str__(self) -> str:
        return self.keterangan


class ValidasiSekolah(Validasi):
    pass


class ValidasiPrasarana(Validasi):
    pass


class ValidasiPesertaDidik(Validasi):
    pass


class ValidasiPtk(Validasi):
    pass


class ValidasiRombonganBelajar(Validasi):
    pass


class ValidasiPembelajaran(Validasi):
    pass


class ValidasiNilai(Validasi):
    pass


class ValidasiReferensi(Validasi):
    pass
