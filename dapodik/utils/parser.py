def parse_rows_cast(datas: dict, Class_):
    outs = []
    rows: dict = datas.get('rows', {})
    if len(rows) == 0:
        return outs
    for key in rows:
        data: dict = rows.get(key)
        outs.append(Class_(**data))
    return outs
