import logging
import json
from dataclasses import asdict, dataclass, _MISSING_TYPE
from requests import Session
from logging import Logger
from typing import Union
from dapodik.utils import cast
from dapodik.config import BASE_URL
from dapodik.rest import ChildDelete
from dapodik.utils import parse_rows_cast, parse_rows_update


class Base:
    _url: str = BASE_URL
    _logger: Logger = None


class Rest(Base):
    _id: str = None
    __url: str = None

    def __init__(self, session: Session, Class_, url: str, params: dict = None, get=True, post=True, put=True, delete=True):
        self._session: Session = session
        self.__url: str = url
        self.params: dict = params
        self._get: bool = get
        self._post: bool = post
        self._put: bool = put
        self._delete: bool = delete
        self.__class = Class_
        self._logger = logging.getLogger(self.__class.__name__)

    def __call__(self):
        return self.get()

    @property
    def _full_url(self):
        return self._url+self.__url

    def get(self):
        outs = []
        try:
            res = self._session.get(
                self._full_url, params=self.params if self.params and len(self.params) > 0 else {})
            if res.ok:
                datas: dict = res.json()
                self._id = datas.get('id')
                outs = parse_rows_cast(datas, self.__class, True)
        except Exception as e:
            self._logger.exception(e)
        finally:
            if len(outs) > 0:
                for obj in outs:
                    setattr(obj, '_session', self._session)
            return outs

    def new(self, data_: Union[dict, object], default: dict = None, params: dict = None):
        if type(data_) == dict:
            data_: dict = asdict(cast(data_, self.__class))
        elif isinstance(data_, self.__class):
            data_: dict = asdict(data_)
        else:
            raise ValueError(
                f'data seharusnya bertipe dict atau {self.__class}'
            )
        default = default if default else {}
        params = params if params else {}
        default.update(data_)
        res = self._session.post(self._full_url, json=default, params=params)
        if not res.ok:
            return
        datas = res.text.replace("\'", "\"")
        datas: dict = json.loads(datas)
        if not datas.get('success'):
            return
        data: dict = datas.get('rows')
        data_.update(data)
        return cast(data_, self.__class)


class BaseData:
    _id: str = None
    _session: Session = None
    _url: str = BASE_URL
    __url: str = None

    @property
    def _data_id(self):
        return getattr(self, self._id)

    @property
    def _full_url(self):
        url = self._url
        url += self.__url if self.__url else ''
        url += f'/{self._data_id}' if self._id and self._data_id else ''
        return url

    def update(self, sync=True) -> bool:
        data = asdict(self)
        res = self._session.put(self._full_url, data=data)
        datas: dict = res.json()
        if not res.ok or not datas.get('success', False):
            return False
        if sync and 'rows' in datas:
            parse_rows_update(datas, self)
        return True

    def delete(self) -> bool:
        data = {
            self._id: self._data_id
        }
        params = {
            'sekolah_id': getattr(self, 'sekolah_id'),
        }
        res = self._session.delete(self._full_url, data=data, params=params)
        return res.ok and "'success' : true" in res.text

    def child_delete(self) -> [ChildDelete]:
        url = self._url
        url += 'rest/child_delete/'
        url += self._id
        params = {
            'id': self._data_id
        }
        res = self._session.get(url, params=params)
        return parse_rows_cast(res.json(), ChildDelete)
