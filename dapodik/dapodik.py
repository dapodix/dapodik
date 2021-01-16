from requests import Session

from dapodik import __semester__
from dapodik.base import BaseDapodik, HEADERS, Config
from dapodik.utils.decorator import lazy

from . import BaseAuth
from . import BaseValidasi


class Dapodik(BaseDapodik):
    def __init__(
        self,
        username: str,
        password: str,
        semester_id: str = __semester__,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
        login: bool = True,
        pengguna: int = 0,
    ):
        config = Config(username, password, server, semester_id)
        super(Dapodik, self).__init__(config)
        self.__username = username
        self.__password = password
        self.session.headers.update(HEADERS)
        if login:
            daftar_pengguna = self.auth.login(username, password, semester_id)
            self.auth.login_pengguna(daftar_pengguna[pengguna])

    @property  # type: ignore
    @lazy
    def auth(self) -> BaseAuth:
        return BaseAuth(self.config)

    @property  # type: ignore
    @lazy
    def validasi(self) -> BaseValidasi:
        return BaseValidasi(self.config)

    def __del__(self):
        self.auth.logout()
