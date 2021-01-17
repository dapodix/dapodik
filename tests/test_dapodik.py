from dapodik import __version__, __dapodik_version__, __semester__


def test_version():
    assert __version__ == "0.7.0"
    assert __dapodik_version__ == "2021.c"
    assert __semester__ == "20202"
