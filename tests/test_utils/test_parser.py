from datetime import date, datetime
from dapodik.utils.parser import (
    str_to_date,
    str_to_datetime,
    date_to_str,
    datetime_to_str,
)


def test_str_to_date():
    val = "1999-12-20"
    res = str_to_date(val)
    assert isinstance(res, date)
    assert res.year == 1999
    assert res.month == 12
    assert res.day == 20


def test_str_to_datetime():
    val = "2001-02-20 22:59:30"
    res = str_to_datetime(val)
    assert isinstance(res, datetime)
    assert res.year == 2001
    assert res.month == 2
    assert res.day == 20
    assert res.hour == 22
    assert res.minute == 59
    assert res.second == 30


def lten(val: int) -> str:
    if val < 10:
        return "0" + str(val)
    return str(val)


def test_date_to_str():
    now = datetime.now().date()
    now_str = date_to_str(now)
    assert now_str == f"{now.year}-{lten(now.month)}-{lten(now.day)}"


def test_datetime_to_str():
    now = datetime.now()
    now_str = datetime_to_str(now)
    now_str_ = f"{now.year}-{lten(now.month)}-{lten(now.day)} "
    now_str_ += f"{lten(now.hour)}:{lten(now.minute)}:{lten(now.second)}"
    assert now_str == now_str_
