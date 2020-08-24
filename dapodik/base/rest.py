from __future__ import annotations
from logging import getLogger
from requests import Session
from .dapodik_object import DapodikObject
from .results import Results
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from dapodik import Dapodik


class Rest:
    def __init__(self, dapodik: Dapodik, klass: DapodikObject, url: str):
        self.logger = getLogger(self.__class__.__name__)
        self.session: Session = dapodik.session
        self.dapodik: Dapodik = dapodik
        klass._url = url
        klass.dapodik = dapodik
        self.klass = klass
        self.url = dapodik.domain + url
        self.dapodik.rests[klass] = self
        self.dapodik.id_map[self.klass._id] = self.klass
        self.logger.debug('Berhasil membuat Rest untuk {}'.format(
            klass.__class__.__name__))

    def get(self, params: dict = None) -> Optional[Results]:
        params = params or self.klass.get_params()
        res = self.session.get(self.url, params=params)
        if not res.ok:
            return
        data = res.json()
        result: Results = Results.from_data(self.klass, data, self.dapodik)
        self.dapodik.rests[self.klass] = result
        return result

    def create(self, do: DapodikObject):
        pass

    def update(self, do: DapodikObject):
        pass

    def delete(self, do: DapodikObject):
        pass

    def __call__(self, *args, **kwargs) -> Optional[Results]:
        return self.get(*args, **kwargs)
