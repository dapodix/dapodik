from dapodik import (
    BaseDapodik,
    Rest,
    Semester,
    Sekolah,
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
            self.AkreditasiSp = Rest(self, AkreditasiSp, 'rest/AkreditasiSp')
            self.BlockGrant = Rest(self, BlockGrant, 'rest/BlockGrant')
            self.Kepanitiaan = Rest(self, Kepanitiaan, 'rest/Kepanitiaan')
            self.ProgramInklusi = Rest(self, ProgramInklusi,
                                       'rest/ProgramInklusi')
            self.Sanitasi = Rest(self, Sanitasi, 'rest/Sanitasi')
            self.Sekolah = Rest(self, Sekolah, 'rest/Sekolah')
            self.SekolahLongitudinal = Rest(self, SekolahLongitudinal,
                                            'rest/SekolahLongitudinal')
            self.SekolahPaud = Rest(self, SekolahPaud, 'rest/SekolahPaud')
            self.Semester = Rest(self, Semester, 'rest/Semester')
            self.Yayasan = Rest(self, Yayasan, 'rest/Yayasan')
            self.logger.debug('Berhasil memulai sekolah')
            return True
        except Exception as E:
            self.logger.exception(E)
            return False
