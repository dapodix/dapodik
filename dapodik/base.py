from __future__ import annotations
import json
import logging
from dataclasses import asdict, dataclass, is_dataclass
from requests import Session
from logging import Logger
from typing import Union, TYPE_CHECKING, List, Optional
from dacite import from_dict, Config
from dapodik.utils import cast
from dapodik.config import BASE_URL
from dapodik.rest import ChildDelete
from dapodik.utils import parse_rows_cast, parse_rows_update
# untuk type hint IDE
if TYPE_CHECKING:
    from dapodik import Dapodik


class BaseDapodik:
    session: Session = None
    domain: str = BASE_URL
    sekolah_id: str = None
    logger: Logger = None


class BaseData:
    """Basis dari sebuah data aplikasi dapodik
    """
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


@dataclass
class Results:
    id: str
    start: int
    limit: int
    rows: List[BaseData]
    results: int = 0

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return self.results

    def __getitem__(self, index):
        return self.rows[index]


@dataclass
class Response:
    """Hasil dari server jika melakukan perubahan data
    """
    success: bool
    message: str
    rows: Optional[BaseData]

    def __bool__(self) -> bool:
        return self.success

    def __iter__(self):
        return iter(self.rows)


class Rest(BaseDapodik):
    def __init__(self, dapodik: Dapodik, Class_: BaseData, url: str, default: dict = None, params: dict = None, edit=True, single=False):
        self.session: Session = dapodik.session
        self.domain: str = dapodik.domain
        self.sekolah_id: str = dapodik.sekolah_id
        self._default: dict = default if default else {}
        self._params: dict = params if params else {}
        self._edit: bool = edit
        self._single: bool = single
        self.__url: str = url
        self.__class: BaseData = Class_
        self.logger = logging.getLogger(self.__class.__name__)

    def __call__(self, params={}):
        return self.get(params=params)

    @property
    def _full_url(self):
        return self.domain+self.__url

    def get(self, params: dict = None) -> Union[Results, None]:
        outs = None
        try:
            res = self.session.get(
                self._full_url, params=params if params else self._params)
            if res.ok and 'id' in res.text:
                datas: dict = res.json()
                self._id = datas.get('id')
                outs = from_dict(
                    data_class=Results,
                    data=datas,
                    config=Config(
                        type_hooks={
                            BaseData: lambda class_data: from_dict(
                                self.__class, class_data)
                        }
                    )
                )
        except Exception as e:
            self.logger.exception(e)
        finally:
            # if len(outs) > 0:
            #     for obj in outs:
            #         setattr(obj, '_session', self.session)
            #     if self._single:
            #         outs = outs[0]
            return outs

    def new(self, data_: Union[dict, object], default: dict = None, params: dict = None):
        if not self._edit:
            raise NotImplementedError(
                f'Tidak bisa membuat  {self.__class} baru', self.__class)
        if type(data_) == dict:
            data_: dict = asdict(cast(data_, self.__class))
        elif isinstance(data_, self.__class) and is_dataclass(data_):
            data_: dict = asdict(data_)
        else:
            raise ValueError(
                f'data seharusnya bertipe dict atau {self.__class}'
            )
        default = default if default else self._default
        params = params if params else self._params
        default.update(data_)
        res = self.session.post(self._full_url, json=default, params=params)
        if not res.ok:
            return
        datas = res.text.replace("\'", "\"")
        datas: dict = json.loads(datas)
        if not datas.get('success'):
            return
        data: dict = datas.get('rows')
        data_.update(data)
        return cast(data_, self.__class)
