#!/usr/bin/env python

import logging
from requests import Session
from typing import Dict, Optional, Type, TypeVar

from dapodik import (
    DapodikObject,
    Results,
    Rest,
    BASE_URL,
    USER_AGENT,
    BaseAuth,
    BaseCustomrest,
    BaseJadwal,
    BasePesertaDidik,
    BasePtk,
    BaseRest,
    BaseRombonganBelajar,
    BaseSarpras,
    BaseSekolah,
)

DO = TypeVar("DO", bound=DapodikObject)


class Dapodik(
    BaseAuth,
    BaseCustomrest,
    BaseRest,
    BasePesertaDidik,
    BasePtk,
    BaseRombonganBelajar,
    BaseSarpras,
    BaseJadwal,
    BaseSekolah,
):
    session: Session = Session()
    domain: str = BASE_URL
    cache: Dict[Type[DapodikObject], Results] = {}
    rests: Dict[Type[DapodikObject], Rest] = {}
    id_map: Dict[str, Type[DapodikObject]] = {}

    def __init__(
        self,
        username: str,
        password: str,
        url: str = None,
        verify: bool = False,
        user_agent: str = USER_AGENT,
    ):
        assert bool(username)
        assert bool(password)
        self.domain = url or BASE_URL
        self.verify = verify
        self.logger = logging.getLogger(self.__class__.__name__)
        self.session: Session = Session()
        self.session.headers.update({"User-Agent": user_agent})
        if self.login(username, password):
            self.logger.info("Berhasil login dengan email {}".format(username))
            self.register_auth()
            self.register_customrest()
            self.register_rest()
            self.register_sekolah()
            self.register_sarpras()
            self.register_ptk()
            self.register_peserta_didik()
            self.register_rombongan_belajar()
            self.register_jadwal()

    def __getitem__(self, obj: Type[DO]) -> Optional[Results[DO]]:
        return self.get(obj)

    def get(self, obj: Type[DO]) -> Optional[Results[DO]]:
        res = self.cache.get(obj)
        if self.cache and res:
            if res:
                return res
        if obj in self.rests:
            rest: Optional[Rest] = self.rests.get(obj)
            if rest:
                res = rest.get()
                if res:
                    self.cache[obj] = res
                    return res
        return None
