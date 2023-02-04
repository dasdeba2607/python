import sys

sys.path.append('C:/deba/deba5/training/python/github/python')
from Studentmenu import StoreMenu, DisplayMenu
from StudentDatabase import GetInputFromStudent, CreateDataFile, StoreData, DisplayData, SearchData

def ReadChoice(choice):
    while True:
        if choice == "1":
            file = CreateDataFile()
            studentdata = GetInputFromStudent()
            StoreData(file, studentdata)
        elif choice == "2":
            print("Displaying data")
            file = CreateDataFile()
            DisplayData(file)
        elif choice == "3":
            print("Please enter search string for name")
            criteria = input("enter string : ")
            file = CreateDataFile()
            SearchData(file, "name", criteria)
        elif choice == "4":
            sys.exit(0)
        choice = DisplayMenu()


if __name__ == '__main__':
    StoreMenu()
    choice = DisplayMenu()
    ReadChoice(choice)