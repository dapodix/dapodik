from enum import Enum


class PtkInduk(Enum):
    INDUK = "1"
    NON_INDUK = "0"

    def __bool__(self):
        return self.value == "1"


class PtkAktif(Enum):
    AKTIF = "1"
    NON_AKTIF = "0"

    def __bool__(self):
        return self.value == "1"
