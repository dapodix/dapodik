from __future__ import annotations
from bs4 import BeautifulSoup, Tag
from dataclasses import dataclass
from requests import Session
from typing import Optional, List
from dapodik.config import BASE_URL, SEMESTER_ID, DOMAIN


@dataclass
class Roleperan:
    nama: Optional[str]
    peran: Optional[str]
    lembaga: Optional[str]
    url: str

    @classmethod
    def from_tag(cls, tag: Tag) -> Roleperan:
        a: Tag = tag.find('a')
        spans: List[Tag] = a.find_all('span')
        url = DOMAIN + str(a['href'])
        return cls(
            nama=str(spans[1].text).split(':')[-1],
            peran=str(spans[2].text).split(':')[-1],
            lembaga=str(spans[0].text).split(':')[-1],
            url=url
        )

    def __str__(self):
        strs = [self.nama, self.peran, self.lembaga]
        return ' - '.join(strs)


class Auth(object):
    _url: str = BASE_URL
    _semester_id: str = SEMESTER_ID
    session: Session = None

    def login(self,
              username: str,
              password: str,
              rememberme: bool = True,
              semester_id: str = SEMESTER_ID,
              auto: bool = True):
        data = {
            'username': username,
            'password': password,
            'semester_id': semester_id
        }
        if rememberme is True or rememberme == 'on':
            data['rememberme'] = 'on'
        res0 = self.session.get(self._url)
        if not res0.ok:
            return False
        res1 = self.session.post(self._url + 'roleperan', data=data)
        # handle redirect
        soup = BeautifulSoup(res1.text, 'lxml')
        lis: List[Tag] = soup.find_all('li', class_='w3-bar')
        lis.pop(0)
        lis.pop(-1)
        roles: List[Roleperan] = [Roleperan.from_tag(tag) for tag in lis]
        role: Roleperan = roles[0]
        res3 = self.session.get(role.url)
        return res3.ok

    def logout(self):
        url = self._url + 'destauth'
        res = self.session.get(url)
        return res.ok
