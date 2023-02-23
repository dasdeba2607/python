import sys

import Menu
import Database

def readchoice():
    while True:
        if Menu.Menu.choice == "1":  # Menu.Menu means Menu class of Menu file, else we can use from Menu import Menu where we import only Menu, not whole file and we can refer menu.display(). Please see the previous version
            Database.Database.insert()
        elif Menu.Menu.choice == "2":
            print("Displaying data")
            Database.Database.select()
        elif Menu.Menu.choice == "3":
            print("Please enter search string for name")
            criteria = input("enter string : ")
            attr = "name"
            Database.Database.search(attr, criteria)
        elif Menu.Menu.choice == "4":
            Database.Database.close()
            sys.exit(0)
        Menu.Menu.display()

if __name__ == '__main__':
    Menu.Menu.insert()
    Menu.Menu.display()
    # print(Menu.Menu.choice)
    readchoice()
