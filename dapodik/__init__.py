__version__ = '0.1.0'
from requests import Session
from dapodik.auth import Auth
from dapodik.config import BASE_URL
from dapodik.peserta_didik import BasePesertaDidik
from dapodik.sekolah import BaseSekolah


class Dapodik(Auth, BaseSekolah, BasePesertaDidik):
    def __init__(self, url: str = BASE_URL, verify: bool = False):
        self._url = url
        super(Dapodik, self).__init__()
        self.verify = verify
        self.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
        })
