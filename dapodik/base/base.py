from __future__ import annotations
from logging import Logger
from requests import Session
from typing import Dict, Type
from dapodik.config import BASE_URL
from .dapodik_object import DapodikObject


class BaseDapodik:
    session: Session = Session()
    domain: str = BASE_URL
    sekolah_id: str = ""
    logger: Logger = Logger(__name__)
    id_map: Dict[str, Type[DapodikObject]] = {}
