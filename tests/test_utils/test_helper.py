from dapodik.utils.helper import make_query, find_in


def test_make_query():
    result = make_query(a=1, b=None)
    expected = {"a": 1}
    assert result == expected


def test_find_in():
    a = {"a": 1}
    b = {"b": 2}
    value = [a, b]
    result = find_in(value, lambda val: "b" in val)
    assert result == b
