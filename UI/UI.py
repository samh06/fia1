import os 
import shutil
from msvcrt import getch

class UI:
    def __init__(self, dir):
        # * Get banner from file
        f = open('banner', 'r')
        self.banner = f.read()
        
        # * Temporary directory copy test
        try:
            shutil.copytree(os.path.join(dir, "Data", "template"), os.path.join(dir, "Data", "Sam"))
        except FileExistsError:
            print("Directory Exists")
            
    def mainMenu(self):
        options = ["next", "back"]
        selection = 0
        
        # * Print options
        self.printOptions(self, options, selection)
        
        while True:
            # * Capture key input
            key = ord(getch())
            
            # * Switch case for pressed keys
            match key:
                # * Enter key
                case 13:
                    break
                # * Up arrow
                case 72:
                    print("up")
                    selection -= 1
                    self.printOptions(self, options, selection)
                # * Down arrow
                case 80:
                    print("down")
                    selection += 1
                    self.printOptions(self, options, selection)
            
    def printOptions(self, options, selection):
        # * Clear the terminal
        os.system("cls")
        print('\x1b[1;130;44m', self.banner, '\x1b[0m')
        # * Print options on screen
        for option in range(len(options)):
            # * Show indicator if current selected matches option
            if selection == option:
                print('\x1b[6;30;42m' + "<•>", options[option], '\x1b[0m')
            else:
                print("<○>", options[option])
        
            