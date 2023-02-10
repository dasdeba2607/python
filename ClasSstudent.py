import sys

from Menu import Menu
from Database import Database


def readchoice(mymenu, dbops, choice):
    while True:
        if choice == "1":
            dbops.insert()
        elif choice == "2":
            print("Displaying data")
            dbops.select()
        elif choice == "3":
            print("Please enter search string for name")
            criteria = input("enter string : ")
            attr = "name"
            dbops.search(attr, criteria)
        elif choice == "4":
            dbops.close()
            sys.exit(0)
        choice = mymenu.display()


if __name__ == '__main__':
    mymenu = Menu()
    dbops = Database()
    mymenu.insert()
    choice = mymenu.display()
    readchoice(mymenu, dbops, choice)
