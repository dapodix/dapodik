from bs4 import BeautifulSoup
from typing import List

from dapodik.base import BaseDapodik
from . import Pengguna
from .exception import PasswordSalah, PenggunaTidakTerdaftar


class BaseAuth(BaseDapodik):
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
        redirect = res.headers.get("Location", res.url)
        if redirect.endswith("#PenggunaTidakTerdaftar"):
            raise PenggunaTidakTerdaftar(
                "Username yang Anda masukkan tidak terdaftar! Mohon gunakan username lain."
            )
        elif redirect.endswith("#PasswordSalah"):
            raise PasswordSalah("Password yang Anda masukkan salah!")
        soup = BeautifulSoup(res.text, "html.parser")
        return Pengguna.from_soup(soup, self.server)

    def login_pengguna(self, pengguna: Pengguna) -> bool:
        """Login dengan Pengguna

        Args:
            pengguna (Pengguna): Pengguna dari .login()

        Returns:
            bool: Berhasil / tidaknya login
        """
        return self._get(pengguna.login_url).ok

    def logout(self) -> bool:
        """Logout dari dapodik

        Returns:
            bool: logout berhasil / tidak
        """
        return self._get("destauth").ok
