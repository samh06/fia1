import os 
import shutil
class UI:
    def __init__(dir):
        print("UI")
        
        print(os.path.join(dir, "Data", "template"))
        try:
            shutil.copytree(os.path.join(dir, "Data", "template"), os.path.join(dir, "Data", "Sam"))
        except FileExistsError:
            print("Try again?")