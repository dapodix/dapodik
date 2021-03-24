from enum import Enum


class JenisKelamin(Enum):
    LAKI_LAKI = "L"
    PEREMPUAN = "P"

    def __str__(self) -> str:
        if self.value == "L":
            return "Laki-laki"
        elif self.value == "P":
            return "Perempuan"
        return "Tidak terdefinisi"
