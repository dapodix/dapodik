from typing import List

from dapodik import (
    BaseDapodik,
    Semester,
    Sekolah,
    JurusanSp,
    Yayasan,
    AkreditasiSp,
    BlockGrant,
    Kepanitiaan,
    ProgramInklusi,
    Sanitasi,
    SekolahLongitudinal,
    SekolahPaud,
)


class BaseSekolah(BaseDapodik):
    def register_sekolah(self) -> bool:
        try:
            self.AkreditasiSp = AkreditasiSp.maker(self, "rest/AkreditasiSp")
            self.BlockGrant = BlockGrant.maker(self, "rest/BlockGrant")
            self.Kepanitiaan = Kepanitiaan.maker(self, "rest/Kepanitiaan")
            self.JurusanSp = JurusanSp.maker(self, "rest/JurusanSp")
            self.ProgramInklusi = ProgramInklusi.maker(self, "rest/ProgramInklusi")
            self.Sanitasi = Sanitasi.maker(self, "rest/Sanitasi")
            self.Sekolah = Sekolah.maker(self, "rest/Sekolah")
            self.SekolahLongitudinal = SekolahLongitudinal.maker(
                self, "rest/SekolahLongitudinal"
            )
            self.SekolahPaud = SekolahPaud.maker(self, "rest/SekolahPaud")
            self.Semester = Semester.maker(self, "rest/Semester")
            self.Yayasan = Yayasan.maker(self, "rest/Yayasan")
            self.logger.debug("Berhasil memulai sekolah")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    @property
    def akreditasi_sp(self) -> List[AkreditasiSp]:
        return self.AkreditasiSp()  # type: ignore

    @property
    def blockgrant(self) -> List[BlockGrant]:
        return self.BlockGrant()  # type: ignore

    @property
    def kepanitiaan(self) -> List[Kepanitiaan]:
        return self.Kepanitiaan()  # type: ignore

    @property
    def jurusan_sp(self) -> List[JurusanSp]:
        return self.JurusanSp()  # type: ignore

    @property
    def program_inklusi(self) -> List[ProgramInklusi]:
        return self.ProgramInklusi()  # type: ignore

    @property
    def sanitasi(self) -> List[Sanitasi]:
        return self.Sanitasi()  # type: ignore

    @property
    def sekolah(self) -> List[Sekolah]:
        return self.Sekolah()  # type: ignore

    @property
    def sekolah_longitudinal(self) -> List[SekolahLongitudinal]:
        return self.SekolahLongitudinal()  # type: ignore

    @property
    def sekolah_paud(self) -> List[SekolahPaud]:
        return self.SekolahPaud()  # type: ignore

    @property
    def semester(self) -> List[Semester]:
        return self.Semester()  # type: ignore

    @property
    def yayasan(self) -> List[Yayasan]:
        return self.Yayasan()  # type: ignore
