__version__ = '0.1.0'
from requests import Session
from dapodik.auth import Auth
from dapodik.config import BASE_URL, USER_AGENT
from dapodik.peserta_didik import BasePesertaDidik
from dapodik.rest import BaseRest
from dapodik.rombongan_belajar import BaseRombonganBelajar
from dapodik.sekolah import BaseSekolah


class Dapodik(Auth, BaseSekolah, BasePesertaDidik, BaseRombonganBelajar, BaseRest):
    session: Session = None
    domain: str = BASE_URL

    def __init__(self, url: str = BASE_URL, verify: bool = False, user_agent: str = USER_AGENT):
        self.domain = url
        self.verify = verify
        self.session: Session = Session()
        self.session.headers.update({
            'User-Agent': user_agent
        })
