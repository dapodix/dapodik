from requests import Session
from dapodik.base import BaseDapodik, Rest
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


class BaseSekolah:
    session: Session = None

    @property
    def Akreditasi(self):
        return Rest(
            self.session, Akreditasi, 'rest/Akreditasi'
        )

    @property
    def BlockGrant(self):
        return Rest(
            self.session, BlockGrant, 'rest/BlockGrant'
        )

    @property
    def Kepanitiaan(self):
        return Rest(
            self.session, Kepanitiaan, 'rest/Kepanitiaan'
        )

    @property
    def ProgramInklusi(self):
        return Rest(
            self.session, ProgramInklusi, 'rest/ProgramInklusi'
        )

    @property
    def Sanitasi(self):
        return Rest(
            self.session, Sanitasi, 'rest/Sanitasi'
        )

    @property
    def Sekolah(self):
        return Rest(
            self.session, Sekolah, 'rest/Sekolah'
        )

    @property
    def SekolahLongitudinal(self):
        return Rest(
            self.session, SekolahLongitudinal, 'rest/SekolahLongitudinal'
        )

    @property
    def SekolahPaud(self):
        return Rest(
            self.session, SekolahPaud, 'rest/SekolahPaud'
        )

    @property
    def Yayasan(self):
        return Rest(
            self.session, Yayasan, 'rest/Yayasan'
        )
