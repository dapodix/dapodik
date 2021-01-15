from bs4 import BeautifulSoup
from typing import List

from dapodik.base import BaseDapodik
from . import Pengguna
from .exception import PasswordSalah, PenggunaTidakTerdaftar


class BaseAuth(BaseDapodik):
    def __init__(self, *args, **kwargs):
        super(BaseAuth, self).__init__(*args, **kwargs)

    def login(
        self, username: str, password: str, semester_id: str = "20202"
    ) -> List[Pengguna]:
        data = {"username": username, "password": password, "semester_id": semester_id}
        res = self._post("roleperan", data)
        if res.url.endswith("#PenggunaTidakTerdaftar"):
            raise PenggunaTidakTerdaftar(
                "Username yang Anda masukkan tidak terdaftar! Mohon gunakan username lain."
            )
        elif res.url.endswith("#PasswordSalah"):
            raise PasswordSalah("Password yang Anda masukkan salah!")
        soup = BeautifulSoup(res.text, "html.parser")
        return Pengguna.from_soup(soup, self.__server)
