#!/usr/bin/env python

from .version import __version__, __dapodik_version__  # NOQA
from .version import __semester__, __tahun_ajaran__  # NOQA

from .auth import BaseAuth
from .rest import BaseRest
from .sekolah import BaseSekolah
from .peserta_didik import BasePesertaDidik
from .rombongan_belajar import BaseRombonganBelajar
from .validasi import BaseValidasi

from .dapodik import Dapodik

__all__ = [
    "BaseAuth",
    "BaseRest",
    "BaseSekolah",
    "BaseValidasi",
    "BasePesertaDidik",
    "BaseRombonganBelajar",
    "Dapodik",
]
