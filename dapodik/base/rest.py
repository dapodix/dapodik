from __future__ import annotations
from requests import Session
from .dapodik_object import DapodikObject
from .results import Results
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from dapodik import Dapodik


class Rest:
    def __init__(self, dapodik: Dapodik, klass: DapodikObject, url: str):
        self.session: Session = dapodik.session
        self.dapodik: Dapodik = dapodik
        assert isinstance(klass, DapodikObject)
        self.klass = klass
        self.url = dapodik.domain + url

    def get(self, params: dict = None) -> Optional[Results]:
        res = self.session.get(self.url, params=params)
        if not res.ok:
            return
        data = res.json()
        result: Results = Results.from_data(self.klass, data, self.dapodik)
        self.dapodik.rests[self.klass] = result
        return result

    def __call__(self, *args, **kwargs):
        return self.get(*args, **kwargs)
