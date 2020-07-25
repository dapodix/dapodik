from dapodik.base import BaseDapodik
from dapodik.utils import parse_rows_cast
from .akreditasi import Akreditasi
from .blockgrant import BlockGrant
from .kepanitiaan import Kepanitiaan
from .program_inklusi import ProgramInklusi
from .sanitasi import Sanitasi
from .sekolah import Sekolah
from .sekolah_longitudinal import SekolahLongitudinal
from .sekolah_paud import SekolahPaud
from .yayasan import Yayasan


class BaseSekolah(BaseDapodik):
    def Akreditasi(self) -> [Akreditasi]:
        return self.get_parse_cast_rows('rest/Akreditasi', Akreditasi)

    def BlockGrant(self) -> [BlockGrant]:
        return self.get_parse_cast_rows('rest/BlockGrant', BlockGrant)

    def Kepanitiaan(self) -> [Kepanitiaan]:
        return self.get_parse_cast_rows('rest/Kepanitiaan', Kepanitiaan)

    def ProgramInklusi(self) -> [ProgramInklusi]:
        return self.get_parse_cast_rows('rest/ProgramInklusi', ProgramInklusi)

    def Sanitasi(self) -> [Sanitasi]:
        return self.get_parse_cast_rows('rest/Sanitasi', Sanitasi)

    def Sekolah(self) -> [Sekolah]:
        return self.get_parse_cast_rows('rest/Sekolah', Sekolah)

    def SekolahLongitudinal(self) -> [SekolahLongitudinal]:
        return self.get_parse_cast_rows('rest/SekolahLongitudinal', SekolahLongitudinal)

    def SekolahPaud(self) -> [SekolahPaud]:
        return self.get_parse_cast_rows('rest/SekolahPaud', SekolahPaud)

    def Yayasan(self) -> [Yayasan]:
        return self.get_parse_cast_rows('rest/Yayasan', Yayasan)
