def parse_rows_cast(datas: dict, Class_, id: bool = False):
    outs = []
    rows: dict = datas.get('rows', {})
    id_ = datas.get('id')
    if len(rows) == 0:
        return outs
    for data in rows:
        #data: dict = rows.get(key)
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
