from logging import Logger
from requests import Session
from dapodik.config import BASE_URL


class BaseDapodik:
    session: Session = None
    domain: str = BASE_URL
    sekolah_id: str = None
    logger: Logger = None
