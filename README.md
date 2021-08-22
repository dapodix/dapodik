# dapodik

[![dapodik - PyPi](https://img.shields.io/pypi/v/dapodik)](https://pypi.org/project/dapodik/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/dapodik)](https://pypi.org/project/dapodik/)
[![LISENSI](https://img.shields.io/github/license/dapodix/dapodik)](https://github.com/dapodix/dapodik/blob/master/LISENSI)
[![Donate Saweria](https://img.shields.io/badge/Donasi-Saweria-blue)](https://saweria.co/hexatester)
[![Tutorial](https://img.shields.io/badge/Tutorial-Penggunaan-informational)](https://github.com/dapodix/dapodik/wiki)
[![Tests](https://github.com/dapodix/dapodik/workflows/Tests/badge.svg)](https://github.com/dapodix/dapodik/actions?query=workflow%3ATests)
[![codecov](https://codecov.io/gh/dapodix/dapodik/branch/master/graph/badge.svg)](https://codecov.io/gh/dapodix/dapodik)
[![Code Style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

SDK python untuk aplikasi dapodik.

## Install

Pastikan [python 3.7+](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) terinstall,
kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X):

```bash
pip install --upgrade dapodik
```

## Penggunaan

Contoh pennggunaan

```python
from dapodik import Dapodik

email = 'email@saya.com'
password = 'password dapodik'

d = Dapodik(email, password)
sekolah = d.sekolah()
daftar_peserta_didik = d.peserta_didik(sekolah_id=sekolah.sekolah_id)
for peserta_didik in daftar_peserta_didik:
    print(peserta_didik.nama)
```

## Legal / Hukum

Kode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh [Kemdikbud](https://kemdikbud.go.id/) atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. _Gunakan dengan risiko Anda sendiri._
