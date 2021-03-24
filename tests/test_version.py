from dapodik import __version__, __dapodik_version__, __semester__, __tahun_ajaran__


def test_version():
    assert __version__ == "0.13.0"


def test_dapodik_version():
    assert __dapodik_version__ == "2021.d"


def test_tahun_ajaran():
    assert __tahun_ajaran__ == "2020"


def test_semester():
    assert __semester__ == "20202"
    assert __semester__.startswith(__tahun_ajaran__)
