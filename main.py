from UI import UI
import os
from sys import platform, version_info

# * Minimum Python version
MIN_PYTHON = (3, 10)

def main():
    # * Platform and Python Version checks.
    if platform != "win32":
        exit("This program only runs on windows operatins sstems")
    if version_info < MIN_PYTHON:
        exit("Python %s.%s or later is required.\n" % MIN_PYTHON)
    
    # * Get directory to pass to UI for copying files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # * Create interface and initialise it
    Interface = UI
    Interface.__init__(Interface, dir_path)
    Interface.mainMenu(Interface)

# * Make sure main.py is the one being run
if __name__ == "__main__":
    main()
else:
    print("Run main.py on its own.")