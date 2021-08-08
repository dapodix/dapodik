#!/usr/bin/env python

from .version import __version__, __dapodik_version__  # NOQA
from .version import __semester__, __tahun_ajaran__  # NOQA

from .response import DapodikResponse
from .result import DapodikResult

from .auth import BaseAuth
from .rest import BaseRest
from .validasi import BaseValidasi
from .peserta_didik import BasePesertaDidik
from .gtk import BaseGtk
from .sarpras import BaseSarpras
from .rombongan_belajar import BaseRombonganBelajar
from .sekolah import BaseSekolah

from .dapodik import Dapodik

__all__ = [
    "BaseAuth",
    "BaseGtk",
    "BasePesertaDidik",
    "BaseRest",
    "BaseRombonganBelajar",
    "BaseSarpras",
    "BaseSekolah",
    "BaseValidasi",
    "Dapodik",
    "DapodikResponse",
    "DapodikResult",
]
