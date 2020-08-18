from dataclasses import asdict
from openpyxl.worksheet.worksheet import Worksheet
from dapodik.base import BaseData


def cast_name(
    ws: Worksheet,
    columns: dict,
    row: int = 1,
    change=lambda x: str(x).upper().replace('_', ' ')
):
    for column in columns:
        cell = f"{columns[column]}{row}"
        data: str = columns.get(columns)
        ws[cell] = change(data)


def cast_row(ws: Worksheet, data: BaseData, columns: dict, row: int):
    for column in columns:
        cell = f"{columns[column]}{row}"
        ws[cell] = getattr(data, column)
