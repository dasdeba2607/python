import sys

import MenuInheritence
import Database

class menuChild(MenuInheritence.Menu):

    def test1(self,vv): ## argument type and no of arguments need to be matched with method of parent class for overriding
        print("my value ", vv)

def readchoice(mymenu):
    while True:
        if mymenu.choice == "1":  # menuChild means Menu class of Menu file, else we can use from Menu import Menu where we import only Menu, not whole file and we can refer menu.display(). Please see the previous version
            Database.Database.insert()
        elif mymenu.choice == "2":
            print("Displaying data")
            Database.Database.select()
        elif mymenu.choice == "3":
            print("Please enter search string for name")
            criteria = input("enter string : ")
            attr = "name"
            Database.Database.search(attr, criteria)
        elif mymenu.choice == "4":
            Database.Database.close()
            sys.exit(0)
        mymenu.display()

if __name__ == '__main__':
    mymenu = menuChild()
    mymenu.insert()
    mymenu.display()
    vv = 10
    mymenu.test1(vv)
    # print(menuChild.choice)
    readchoice(mymenu)
