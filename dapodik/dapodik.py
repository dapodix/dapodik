from requests import Session

from dapodik import __semester__
from dapodik.base import HEADERS, Config, Defaults

from . import BaseAuth
from . import BaseRest
from . import BaseSekolah
from . import BaseSarpras
from . import BasePesertaDidik
from . import BaseRombonganBelajar
from . import BaseValidasi


class Dapodik(
    BaseAuth,
    BaseRest,
    BaseSekolah,
    BaseSarpras,
    BasePesertaDidik,
    BaseRombonganBelajar,
    BaseValidasi,
):
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
        self.daftar_pengguna = self.login(
            username, password, rememberme, semester_id, pengguna
        )
        if self.daftar_pengguna:
            self.logger.info(f"Berhasil login {username}")
        if get_sekolah_id:
            sekolah = self.sekolah()
            self.config.sekolah_id = sekolah.sekolah_id
        self.__add_peserta_didik__()
        self.__add_rest__()
        self.__add_rombongan_belajar__()
        self.__add_sarpras__()
        self.__add_sekolah__()
        self.__add_validasi__()

    def __del__(self):
        self.logout()
