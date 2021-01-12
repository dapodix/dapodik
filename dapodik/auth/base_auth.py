from __future__ import annotations
from logging import Logger
from bs4 import BeautifulSoup, Tag
from requests import Session
from typing import List
from dapodik import Rest, Pengguna
from dapodik.config import BASE_URL, SEMESTER_ID
from .role_peran import Roleperan


class BaseAuth(object):
    _url: str = BASE_URL
    _semester_id: str = SEMESTER_ID
    session: Session = Session()
    logger: Logger = Logger(__name__)

    def register_auth(self) -> bool:
        try:
            self.Pengguna = Rest(self, Pengguna, "rest/Pengguna")
            self.logger.debug("Berhasil memulai auth")
            return True
        except Exception as E:
            self.logger.exception(E)
            return False

    def login(
        self,
        username: str,
        password: str,
        rememberme: bool = True,
        semester_id: str = SEMESTER_ID,
        auto: bool = True,
    ):
        data = {"username": username, "password": password, "semester_id": semester_id}
        if rememberme is True or rememberme == "on":
            data["rememberme"] = "on"
        res0 = self.session.get(self._url)
        if not res0.ok:
            return False
        res1 = self.session.post(self._url + "roleperan", data=data)
        # handle redirect
        soup = BeautifulSoup(res1.text, "html.parser")
        lis: List[Tag] = soup.find_all("li", class_="w3-bar")
        lis.pop(0)
        lis.pop(-1)
        roles: List[Roleperan] = [Roleperan.from_tag(tag) for tag in lis]
        role: Roleperan = roles[0]
        res3 = self.session.get(role.url)
        return res3.ok

    def logout(self):
        url = self._url + "destauth"
        res = self.session.get(url)
        return res.ok
