from dapodik.enums import JenisKelamin


def test_jenis_kelamin():
    assert JenisKelamin("L") == JenisKelamin.LAKI_LAKI
    assert JenisKelamin("P") == JenisKelamin.PEREMPUAN
    assert str(JenisKelamin("L")).lower() == "laki-laki"
    assert str(JenisKelamin("P")).lower() == "perempuan"
