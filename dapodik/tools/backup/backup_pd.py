from dataclasses import asdict
from datetime import datetime
from openpyxl import Workbook
from dapodik.base import Results
from dapodik.peserta_didik import PesertaDidik
from .base import BaseBackup
from .utils import cast_name, cast_row

STR_DATETIME_FORMAT = ''
COLUMNS = {
    'nama': 'A',
    'jenis_kelamin': 'B',
    'tempat_lahir': 'C',
    'tanggal_lahir': 'D',
    'agama_id': 'E',
    'nisn': 'F',
    'nik': 'G',
    'no_kk': 'H',
    'alamat_jalan': 'I',
    'rt': 'J',
    'rw': 'K',
    'nama_dusun': 'L',
    'desa_kelurahan': 'M',
    'kode_wilayah': 'N',
    'kewarganegaraan': 'O',
    'kode_pos': 'P',
    'lintang': 'Q',
    'bujur': 'R',
    'anak_keberapa': 'S',
    'reg_akta_lahir': 'T',
    'kebutuhan_khusus_id': 'U',
    'jenis_tinggal_id': 'V',
    'alat_transportasi_id': 'W',
    'no_kks': 'X',
    'penerima_kps': 'Y',
    'no_kps': 'Z',
    'penerima_kip': 'AA',
    'no_kip': 'AB',
    'nm_kip': 'AC',
    'layak_pip': 'AD',
    'id_layak_pip': 'AE',
    'id_bank': 'AF',
    'rekening_bank': 'AG',
    'nama_kcp': 'AH',
    'rekening_atas_nama': 'AI',
    'status_data': 'AJ',
    'nomor_telepon_rumah': 'AK',
    'nomor_telepon_seluler': 'AL',
    'email': 'AM',
    'nama_ibu_kandung': 'AN',
    'tahun_lahir_ibu': 'AO',
    'nik_ibu': 'AP',
    'jenjang_pendidikan_ibu': 'AQ',
    'pekerjaan_id_ibu': 'AR',
    'penghasilan_id_ibu': 'AS',
    'kebutuhan_khusus_id_ibu': 'AT',
    'nama_ayah': 'AU',
    'tahun_lahir_ayah': 'AV',
    'nik_ayah': 'AW',
    'jenjang_pendidikan_ayah': 'AX',
    'pekerjaan_id_ayah': 'AZ',
    'penghasilan_id_ayah': 'BA',
    'kebutuhan_khusus_id_ayah': 'BB',
    'nama_wali': 'BC',
    'tahun_lahir_wali': 'BD',
    'nik_wali': 'BE',
    'jenjang_pendidikan_wali': 'BF',
    'pekerjaan_id_wali': 'BG',
    'penghasilan_id_wali': 'BH',
    'kebutuhan_khusus_id_selector': 'BI',
    'peserta_didik_id': 'BJ',
    'pdb_id': 'BK',
    'sekolah_id': 'BL',
    'vld_count': 'BM',
    # Str?
    'agama_id_str': 'CA',
    'kebutuhan_khusus_id_str': 'CB',
    'jenis_tinggal_id_str': 'CC',
    'alat_transportasi_id_str': 'CD',
    'kebutuhan_khusus_id_selector_ibu': 'CE',
    'jenjang_pendidikan_ibu_str': 'CF',
    'pekerjaan_id_ibu_str': 'CG',
    'penghasilan_id_ibu_str': 'CH',
    'kebutuhan_khusus_id_ibu_str': 'CI',
    'jenjang_pendidikan_ayah_str': 'CJ',
    'pekerjaan_id_ayah_str': 'CK',
    'penghasilan_id_ayah_str': 'CL',
    'kebutuhan_khusus_id_ayah_str': 'CM',
    'kebutuhan_khusus_id_selector_ayah': 'CN',
    'jenjang_pendidikan_wali_str': 'CO',
    'pekerjaan_id_wali_str': 'CP',
    'penghasilan_id_wali_str': 'CQ',
    'id_layak_pip_str': 'CR',
    'id_bank_str': 'CS',
    'kode_wilayah_str': 'CT',
    'kewarganegaraan_str': 'CU',
}


class BackupPd(BaseBackup):
    def backup_peserta_didik(self, filename: str = None, results: Results = None):
        results = results or self.dapodik.PesertaDidik()
        if not results:
            self.logger.warn('Tidak ada peserta didik untuk dibackup...')
            return False
        filename = filename or f'Peserta-Didik_{datetime.now()}'
        wb = Workbook()
        ws = wb.active
        cast_name(ws, COLUMNS)
        for index, peserta_didik in enumerate(results):
            peserta_didik: PesertaDidik = peserta_didik
            cast_row(ws, peserta_didik, COLUMNS, index + 2)
            self.logger.info('Menyimpan data', str(peserta_didik))
        wb.save(filename)
