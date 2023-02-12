from UI import UI
import os
from sys import platform, version_info
MIN_PYTHON = (3, 10)

def main():
    # * Platform and Python Version checks.
    if platform != "win32":
        exit("This program only runs on windows operatins sstems")
    if version_info < MIN_PYTHON:
        exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    Interface = UI
    Interface.__init__(Interface, dir_path)
    Interface.mainMenu(Interface)

if __name__ == "__main__":
    main()