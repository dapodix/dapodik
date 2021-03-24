from enum import Enum


class JenisKelamin(Enum):
    LAKI_LAKI = "L"
    PEREMPUAN = "P"

    def __str__(self) -> str:
        if self.value == self.LAKI_LAKI:
            return "Laki-laki"
        elif self.value == self.PEREMPUAN:
            return "Perempuan"
        return "Tidak terdefinisi"
