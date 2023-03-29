#!/usr/bin/env python
import sys
from . import __version__, __dapodik_version__, __semester__, __tahun_ajaran__


def print_ver():
    print("python dapodik versi v{}".format(__version__))
    print("Client / SDK python untuk dapodik versi {}".format(__dapodik_version__))
    print("Semester {}".format(__semester__))
    print("Tahun ajaran {}".format(__tahun_ajaran__))
    print("Python {}".format(sys.version.replace("\n", " ")))


def main():
    sys.exit(print_ver())


if __name__ == "__main__":
    main()
