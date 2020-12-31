#!/usr/bin/env python
import sys
from . import __version__, __dapodik_version__


def print_ver():
    print("dapodik versi v{}".format(__version__))
    print("Client / API python untuk dapodik versi {}".format(__dapodik_version__))
    print("Python {}".format(sys.version.replace("\n", " ")))


def main():
    print_ver()


if __name__ == "__main__":
    main()
