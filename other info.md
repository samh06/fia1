            key = ord(getch())
            # * Enter key
            if key == 13:
                break
            elif key == 72:
                print("up")
                selection -= 1
                self.printOptions(self, options, selection)
            elif key == 80:
                print("down")
                selection += 1
                self.printOptions(self, options, selection)
            # elif key == 75:
            #     print("left")
            #     self.printOptions(self, options, selection)
            # elif key == 77:
            #     print("right")
            #     self.printOptions(self, options, selection)
