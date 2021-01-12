from dapodik import __version__, __dapodik_version__


def test_version():
    assert __version__ == "0.6.1"
    assert __dapodik_version__ == "2021.b"
