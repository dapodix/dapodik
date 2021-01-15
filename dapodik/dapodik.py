from requests import Session

from dapodik.base import BaseDapodik
from dapodik.auth import BaseAuth


class Dapodik(BaseDapodik):
    def __init__(
        self,
        server="http://localhost:5774/",
        session=Session(),
        login: bool = True,
        pengguna: int = 1,
    ):
        super().__init__(server=server, session=session)
        self.auth = BaseAuth(self)
