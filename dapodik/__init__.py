#!/usr/bin/env python

from .version import __version__, __dapodik_version__, __semester__  # NOQA

from .auth import BaseAuth
from .rest import BaseRest
from .sekolah import BaseSekolah
from .peserta_didik import BasePesertaDidik
from .validasi import BaseValidasi

from .dapodik import Dapodik

__all__ = [
    "BaseAuth",
    "BaseRest",
    "BaseSekolah",
    "BaseValidasi",
    "BasePesertaDidik",
    "Dapodik",
]
