from dataclasses import MISSING
from datetime import datetime, date
from typing import Union


def parse_rows_update(datas: dict, instance):
    data: dict = datas.get('rows', {})
    if data.get(instance._id) == instance._data_id:
        for ke in data:
            setattr(instance, ke, data[ke])
    return instance


def cast(data: dict, Class_):
    """Merubah dict menjadi Class_

    Args:
        data (dict): Data dari server
        Class_ (DapodikObject): Class untuk dimasukan datanya

    Raises:
        TypeError: Jika Class tidak dataclass / tidak memiliki __anotations__
        ValueError: Jika data tidak memiliki argumen yang diperlukan Class_

    Returns:
        BaseData: Instance dari data
    """
    anot: dict = getattr(Class_, '__annotations__', {})
    if len(anot) == 0:
        raise TypeError(f'{Class_} didnt have anotations')
    ndata_ = {}
    fields = Class_.__dataclass_fields__
    for key in anot:
        if key in data and data[key]:
            ndata_[key] = data[key]
        elif key in fields:
            ndata_[key] = fields[key].default
        else:
            ndata_[key] = None
        if type(ndata_[key]) == MISSING:
            raise ValueError(f"Missing type found {key} from {ndata_}")
    return Class_(**ndata_)


def str_to_datetime(data: Union[str, datetime],
                    format: str = '%Y-%m-%d %H:%M:%S') -> datetime:
    if isinstance(data, datetime):
        return data
    elif type(data) == str:
        return datetime.strptime(data, format)
    else:
        return datetime.now()


def str_to_date(data: Union[str, date], format: str = '%Y-%m-%d') -> date:
    if isinstance(data, date):
        return data
    elif type(data) == str:
        return datetime.strptime(data, format).date()
    else:
        return datetime.now().date()
