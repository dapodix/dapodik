from dapodik.result import DapodikResult
from dapodik.rest import Agama
from typing import List

def test_result():
    data = """{ "results" : 8, "id" : "agama_id", "start": 0, "limit": 20, "rows" : [{"agama_id":1,"nama":"Islam","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":2,"nama":"Kristen","create_date":"2013-05-13 00:00:00","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":3,"nama":"Katholik","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":4,"nama":"Hindu","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":5,"nama":"Budha","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":6,"nama":"Khonghucu","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":7,"nama":"Kepercayaan kpd Tuhan YME","create_date":"2017-01-31 01:00:00","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"},{"agama_id":99,"nama":"lainnya","create_date":"2013-05-13 06:51:30","last_update":"2021-06-19 13:23:39","expired_date":null,"last_sync":"2021-06-19 13:23:39"}] }"""
    result = DapodikResult.from_str(data, List[Agama])
    assert isinstance(result, DapodikResult)
    assert isinstance(result.rows, list)
    for agama in result.rows:
        assert isinstance(agama, Agama)
        break
