__version__ = '0.1.0'
from requests import Session
from typing import Dict, Optional
from dapodik.auth import Auth
from dapodik.base import DapodikObject, Results, Rest
from dapodik.config import BASE_URL, USER_AGENT
from dapodik.peserta_didik import BasePesertaDidik
from dapodik.rest import BaseRest
from dapodik.rombongan_belajar import BaseRombonganBelajar
from dapodik.sarpras import BaseSarpras
from dapodik.sekolah import BaseSekolah


class Dapodik(Auth, BaseSekolah, BasePesertaDidik, BaseRombonganBelajar,
              BaseSarpras, BaseRest):
    session: Session = None
    domain: str = BASE_URL
    cache: Dict[DapodikObject, Results] = {}
    rests: Dict[DapodikObject, Rest] = {}

    def __init__(self,
                 url: str = None,
                 verify: bool = False,
                 user_agent: str = USER_AGENT):
        self.domain = url or BASE_URL
        self.verify = verify
        self.session: Session = Session()
        self.session.headers.update({'User-Agent': user_agent})

    def __getitem__(self, key: DapodikObject) -> Optional[Results]:
        res = self.cache.get(key)
        if self.cache and res:
            if res:
                return res
        if key not in self.rests:
            return
        rest: Rest = self.rests.get(key)
        if not rest:
            return
        res = rest.get()
        if not res:
            return
        self.cache[key] = res
        return res
