#!/usr/bin/env python

import logging
from requests import Session
from typing import Dict, Optional

from dapodik import (
    DapodikObject,
    Results,
    Rest,
    BASE_URL,
    USER_AGENT,
    Auth,
    BaseCustomrest,
    BasePesertaDidik,
    BasePtk,
    BaseRest,
    BaseRombonganBelajar,
    BaseSarpras,
    BaseSekolah,
)


class Dapodik(Auth, BaseCustomrest, BaseRest, BasePesertaDidik, BasePtk,
              BaseRombonganBelajar, BaseSarpras, BaseSekolah):
    session: Session = None
    domain: str = BASE_URL
    cache: Dict[DapodikObject, Results] = {}
    rests: Dict[DapodikObject, Rest] = {}
    id_map: Dict[str, DapodikObject] = {}

    def __init__(self,
                 username: str,
                 password: str,
                 url: str = None,
                 verify: bool = False,
                 user_agent: str = USER_AGENT):
        assert bool(username)
        assert bool(password)
        self.domain = url or BASE_URL
        self.verify = verify
        self.logger = logging.getLogger(self.__class__.__name__)
        self.session: Session = Session()
        self.session.headers.update({'User-Agent': user_agent})
        if self.login(username, password):
            self.register_rest()
            self.register_sekolah()
            self.register_sarpras()
            self.register_ptk()
            self.register_peserta_didik()
            self.register_rombongan_belajar()

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
