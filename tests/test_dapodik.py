from dapodik import __version__, __dapodik_version__


def test_version():
    assert __version__ == '0.3.0'
    assert __dapodik_version__ == '2021.a'
