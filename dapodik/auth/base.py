from bs4 import BeautifulSoup
from typing import List

from dapodik.base import BaseDapodik
from dapodik.exception import PasswordSalah, PenggunaTidakTerdaftar, ServerTidakMerespon
from . import Pengguna


class BaseAuth(BaseDapodik):
    def login(
        self,
        username: str,
        password: str,
        rememberme: bool = True,
        semester_id: str = "20202",
        pengguna: int = None,
    ) -> List[Pengguna]:
        """Login ke dapodik dan mendapatkan daftar Pengguna

        Args:
            username (str): Email dapodik
            password (str): Password dapodik
            semester_id (str, optional): Id semester. Defaults to "20202".

        Raises:
            ServerTidakMerespon: Server dapodik tidak merespon
            PenggunaTidakTerdaftar: Username yang Anda masukkan tidak terdaftar!
            PasswordSalah: Password yang Anda masukkan salah!

        Returns:
            List[Pengguna]: list dari Pengguna
        """
        res = self._get("")
        if not res.ok:
            raise ServerTidakMerespon(f"Server dapodik ({self.server}) tidak merespon")
        data = {"username": username, "password": password, "semester_id": semester_id}
        if rememberme:
            data["rememberme"] = "on"
        res = self._post("roleperan", data)
        redirect = res.request.url or res.url
        # Check error
        if redirect.endswith("#PenggunaTidakTerdaftar"):
            raise PenggunaTidakTerdaftar(
                "Username yang Anda masukkan tidak terdaftar! Mohon gunakan username lain."
            )
        elif redirect.endswith("#PasswordSalah"):
            raise PasswordSalah("Password yang Anda masukkan salah!")
        soup = BeautifulSoup(res.text, "html.parser")
        daftar_pengguna = Pengguna.from_soup(soup, self.server)
        if pengguna is None:
            return daftar_pengguna
        self.login_pengguna(daftar_pengguna[pengguna])
        return daftar_pengguna

    def login_pengguna(self, pengguna: Pengguna) -> bool:
        """Login dengan Pengguna

        Args:
            pengguna (Pengguna): Pengguna dari .login()

        Returns:
            bool: Berhasil / tidaknya login
        """
        res = self._get(pengguna.login_url)
        return res.ok

    def logout(self) -> bool:
        """Logout dari dapodik

        Returns:
            bool: logout berhasil / tidak
        """
        return self._get("destauth").ok
