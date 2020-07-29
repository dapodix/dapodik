from dataclasses import MISSING

def parse_rows_cast(datas: dict, Class_, id: bool = False):
    outs = []
    rows: dict = datas.get('rows', {})
    id_ = datas.get('id')
    if len(rows) == 0:
        return outs
    for data in rows:
        data_ = Class_(**data)
        if id:
            data_._id = id_
        outs.append(data_)
    return outs


def parse_rows_update(datas: dict, instance):
    data: dict = datas.get('rows', {})
    if data.get(instance._id) == instance._data_id:
        for ke in data:
            setattr(instance, ke, data[ke])
    return instance


def cast(data: dict, Class_):
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
