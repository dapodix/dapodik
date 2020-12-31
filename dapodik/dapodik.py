#!/usr/bin/env python

import logging
from requests import Session
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from dapodik import (
    DapodikObject,
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
    cache: Dict[Type[DapodikObject], Any] = {}
    rests: Dict[Type[DapodikObject], Any] = {}
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

    def __getitem__(self, obj: Type[DO]) -> Optional[Union[DO, List[DO]]]:
        return self.get(obj)

    def get(self, obj: Type[DO]) -> Optional[Union[DO, List[DO]]]:
        if self.cache and obj in self.cache:
            return self.cache[obj]
        elif self.rests and obj in self.rests:
            return self.rests[obj]()
        return None
