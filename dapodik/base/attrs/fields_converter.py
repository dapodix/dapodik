from datetime import datetime, date
from typing import Optional
from uuid import UUID

from dapodik.utils.parser import str_to_datetime, str_to_date


def fields_converter(cls, fields):
    results = []
    for field in fields:
        if field.converter is not None:
            results.append(field)
            continue
        if field.type in {int, "int"}:
            converter = int
        elif field.type in {UUID, "UUID"}:
            converter = UUID
        elif field.type in {datetime, "datetime"}:
            converter = str_to_datetime
        elif field.type in {date, "date"}:
            converter = str_to_date
        elif field.type == Optional[field.type]:

            def converter(d=None):
                return d

        else:
            converter = None
        results.append(field.evolve(converter=converter))
    return results
