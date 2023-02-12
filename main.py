from UI import UI
import os
from sys import platform, version_info

def main():
    # * Python Version checks.
    if version_info < (3, 10):
        exit("Python %s.%s or later is required.\n" % (3, 10))
    
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