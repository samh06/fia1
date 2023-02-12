import os 
import shutil
from msvcrt import getch

class UI:
    def __init__(self, dir):
        f = open('banner', 'r')
        self.banner = f.read()
        try:
            shutil.copytree(os.path.join(dir, "Data", "template"), os.path.join(dir, "Data", "Sam"))
        except FileExistsError:
            print("Directory Exists")
            
    def mainMenu(self):
        options = ["next", "back"]
        selection = 0
        self.printOptions(self, options, selection)
        while True:
            key = ord(getch())
            # * Enter key
            match key:
                case 13:
                    break
                case 72:
                    print("up")
                    selection -= 1
                    self.printOptions(self, options, selection)
                case 80:
                    print("down")
                    selection += 1
                    self.printOptions(self, options, selection)
            
    def printOptions(self, options, selection):
        os.system("cls")
        print('\x1b[1;130;44m', self.banner, '\x1b[0m')
        for option in range(len(options)):
            if selection == option:
                print('\x1b[6;30;42m' + "<•>", options[option], '\x1b[0m')
            else:
                print("<○>", options[option])
        
            