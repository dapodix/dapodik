from requests import Session

from dapodik import __semester__
from dapodik.base import BaseDapodik, HEADERS, Config, Defaults
from dapodik.utils.decorator import lazy

from . import BaseAuth
from . import BaseRest
from . import BaseSekolah
from . import BasePesertaDidik
from . import BaseRombonganBelajar
from . import BaseValidasi


class Dapodik(BaseDapodik):
    def __init__(
        self,
        username: str,
        password: str,
        semester_id: str = __semester__,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
        pengguna: int = 0,
        rememberme: bool = True,
        get_sekolah_id: bool = True,
        defaults: Defaults = None,
    ):
        config = Config(
            username=username,
            password=password,
            server=server,
            semester_id=semester_id,
            session=session,
            defaults=defaults,
        )
        super(Dapodik, self).__init__(config)
        self.session.headers.update(HEADERS)
        self.daftar_pengguna = self.auth.login(
            username, password, rememberme, semester_id, pengguna
        )
        if self.daftar_pengguna:
            self.logger.info(f"Berhasil login {username}")
        if get_sekolah_id:
            sekolah = self.sekolah.sekolah()
            self.config.sekolah_id = sekolah.sekolah_id

    @property  # type: ignore
    @lazy
    def auth(self) -> BaseAuth:
        return BaseAuth(self.config)

    @property  # type: ignore
    @lazy
    def peserta_didik(self) -> BasePesertaDidik:
        return BasePesertaDidik(self.config)

    @property  # type: ignore
    @lazy
    def rest(self) -> BaseRest:
        return BaseRest(self.config)

    @property  # type: ignore
    @lazy
    def rombongan_belajar(self) -> BaseRombonganBelajar:
        return BaseRombonganBelajar(self.config)

    @property  # type: ignore
    @lazy
    def sekolah(self) -> BaseSekolah:
        return BaseSekolah(self.config)

    @property  # type: ignore
    @lazy
    def validasi(self) -> BaseValidasi:
        return BaseValidasi(self.config)

    def __del__(self):
        self.auth.logout()
