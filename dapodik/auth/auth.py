from bs4 import BeautifulSoup
from typing import List

from dapodik.base import BaseDapodik
from . import Pengguna
from .exception import PasswordSalah, PenggunaTidakTerdaftar


class BaseAuth(BaseDapodik):
    def __init__(self, *args, **kwargs):
        super(BaseAuth, self).__init__(*args, **kwargs)

    def login(
        self,
        username: str,
        password: str,
        semester_id: str = "20202",
    ) -> List[Pengguna]:
        """Login ke dapodik dan mendapatkan daftar Pengguna

        Args:
            username (str): Email dapodik
            password (str): Password dapodik
            semester_id (str, optional): Id semester. Defaults to "20202".

        Raises:
            PenggunaTidakTerdaftar: Username yang Anda masukkan tidak terdaftar!
            PasswordSalah: Password yang Anda masukkan salah!

        Returns:
            List[Pengguna]: list dari Pengguna
        """
        data = {"username": username, "password": password, "semester_id": semester_id}
        res = self._post("roleperan", data, allow_redirects=False)
        if res.url.endswith("#PenggunaTidakTerdaftar"):
            raise PenggunaTidakTerdaftar(
                "Username yang Anda masukkan tidak terdaftar! Mohon gunakan username lain."
            )
        elif res.url.endswith("#PasswordSalah"):
            raise PasswordSalah("Password yang Anda masukkan salah!")
        res = self._get(res.headers["Location"])
        soup = BeautifulSoup(res.text, "html.parser")
        return Pengguna.from_soup(soup, self.__server)

    def login_pengguna(self, pengguna: Pengguna) -> bool:
        """Login dengan Pengguna

        Args:
            pengguna (Pengguna): Pengguna dari .login()

        Returns:
            bool: Berhasil / tidaknya login
        """
        return self._get(pengguna.url).ok
