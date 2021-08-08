import cattr
from datetime import date, datetime
from uuid import UUID

from dapodik.peserta_didik import PesertaDidik
from dapodik.response import DapodikResponse
from dapodik.utils.parser import str_to_date, str_to_datetime


def test_dapodik_response():
    cattr.register_structure_hook(date, lambda d, t: str_to_date(d))
    cattr.register_structure_hook(datetime, lambda d, t: str_to_datetime(d))
    cattr.register_structure_hook(UUID, lambda d, t: UUID(d))
    data = """{ 'success' : true, 'message' : 'Berhasil mengupdate PesertaDidik', 'rows' : {"peserta_didik_id":"a5a3ccff-53e2-4228-b321-541f59324a9e","nama":"ADAM","jenis_kelamin":"L","nisn":null,"nik":"1111222233334444","no_kk":"1111222233334444","tempat_lahir":"INDONESIA","tanggal_lahir":"1945-8-17","agama_id":1,"kebutuhan_khusus_id":0,"alamat_jalan":"Indonesia","rt":"1","rw":"1","nama_dusun":"JAKARTA","desa_kelurahan":"KALIREJO","kode_wilayah":"123456","kode_pos":"10000","lintang":"0","bujur":"0","jenis_tinggal_id":"1","alat_transportasi_id":"1","nik_ayah":"1111222233334444","nik_ibu":"1111222233334444","anak_keberapa":"1","nik_wali":null,"nomor_telepon_rumah":null,"nomor_telepon_seluler":null,"email":null,"penerima_kps":"0","no_kps":null,"layak_pip":"0","penerima_kip":"0","no_kip":null,"nm_kip":"0","no_kks":null,"reg_akta_lahir":null,"id_layak_pip":null,"id_bank":null,"rekening_bank":null,"nama_kcp":null,"rekening_atas_nama":null,"status_data":0,"nama_ayah":"ADAM SENIOR","tahun_lahir_ayah":"1945","jenjang_pendidikan_ayah":"6","pekerjaan_id_ayah":6,"penghasilan_id_ayah":13,"kebutuhan_khusus_id_ayah":0,"nama_ibu_kandung":"MAMA ADAM","tahun_lahir_ibu":"1945","jenjang_pendidikan_ibu":"6","penghasilan_id_ibu":13,"pekerjaan_id_ibu":6,"kebutuhan_khusus_id_ibu":0,"nama_wali":null,"tahun_lahir_wali":null,"jenjang_pendidikan_wali":"0","pekerjaan_id_wali":0,"penghasilan_id_wali":0,"kewarganegaraan":"ID","pekerjaan_id":0,"create_date":"2021-08-08 11:26:30","last_update":"2021-08-07 20:10:41","soft_delete":"0","last_sync":"2021-08-07 19:40:41","updater_id":"69374600-ca7f-4f4b-8d50-128fb3825220"} }"""
    response = DapodikResponse.from_str(data, PesertaDidik)
    assert isinstance(response, DapodikResponse)
    assert isinstance(response.rows, PesertaDidik)
