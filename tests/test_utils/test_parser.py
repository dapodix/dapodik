from datetime import date, datetime
from dapodik.utils.parser import str_to_date, str_to_datetime


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
