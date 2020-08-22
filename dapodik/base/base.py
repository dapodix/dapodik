from logging import Logger
from requests import Session
from typing import Dict
from dapodik.config import BASE_URL
from .dapodik_object import DapodikObject


class BaseDapodik:
    session: Session = None
    domain: str = BASE_URL
    sekolah_id: str = None
    logger: Logger = None
    id_map: Dict[str, DapodikObject] = {}
