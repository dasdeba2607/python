import sys

import Menu
import Database

class menuChild(Menu.Menu):
    pass


def readchoice():
    while True:
        if menuChild.choice == "1":  # menuChild means Menu class of Menu file, else we can use from Menu import Menu where we import only Menu, not whole file and we can refer menu.display(). Please see the previous version
            Database.Database.insert()
        elif menuChild.choice == "2":
            print("Displaying data")
            Database.Database.select()
        elif menuChild.choice == "3":
            print("Please enter search string for name")
            criteria = input("enter string : ")
            attr = "name"
            Database.Database.search(attr, criteria)
        elif menuChild.choice == "4":
            Database.Database.close()
            sys.exit(0)
        menuChild.display()

if __name__ == '__main__':
    menuChild.insert()
    menuChild.display()
    # print(menuChild.choice)
    readchoice()
