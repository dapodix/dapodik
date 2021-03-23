#!/usr/bin/env python

from .version import __version__, __dapodik_version__  # NOQA
from .version import __semester__, __tahun_ajaran__  # NOQA

from .auth import BaseAuth
from .validasi import BaseValidasi

from .dapodik import Dapodik

__all__ = [
    "BaseAuth",
    "BaseValidasi",
    "Dapodik",
]
