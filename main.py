from UI import UI
import os
    
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    UI.__init__(dir_path)

if __name__ == "__main__":
    main()