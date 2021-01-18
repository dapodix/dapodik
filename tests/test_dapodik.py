from dapodik import __version__, __dapodik_version__, __semester__, __tahun_ajaran__


def test_version():
    assert __version__ == "0.8.1"
    assert __dapodik_version__ == "2021.c"
    assert __semester__ == "20202"
    assert __tahun_ajaran__ == "2020"
    assert __semester__.startswith(__tahun_ajaran__)
