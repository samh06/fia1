from UI import UI
import os
from sys import platform
    
def main():
    if platform != "win32":
        print("This program only runs on windows operatins sstems")
        exit()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    Interface = UI
    Interface.__init__(Interface, dir_path)
    Interface.mainMenu(Interface)

if __name__ == "__main__":
    main()