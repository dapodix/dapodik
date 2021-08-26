from dapodik.message import DapodikMessage


def test_dapodik_message():
    data = "{ 'success' : false, 'message' : 'Gagal menyimpan PesertaDidik (data Penghasilan Ayah belum terisi dengan benar)' }"
    message = (
        "Gagal menyimpan PesertaDidik (data Penghasilan Ayah belum terisi dengan benar)"
    )
    res = DapodikMessage.from_fail(data)
    assert res.success is False
    assert not res
    assert res.message == message
