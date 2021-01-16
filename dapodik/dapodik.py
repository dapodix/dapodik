from requests import Session

from dapodik import __semester__
from dapodik.base import BaseDapodik, HEADERS
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
        super(Dapodik, self).__init__(server, session, semester_id)
        self.__username = username
        self.__password = password
        self.session.headers.update(HEADERS)
        if login:
            daftar_pengguna = self.auth.login(username, password, semester_id)
            self.auth.login_pengguna(daftar_pengguna[pengguna])

    @property  # type: ignore
    @lazy
    def auth(self) -> BaseAuth:
        return BaseAuth(self.server, self.session, self.semester_id)

    @property  # type: ignore
    @lazy
    def validasi(self) -> BaseValidasi:
        return BaseValidasi(self.server, self.session, self.semester_id)

    def __del__(self):
        self.auth.logout()
