import os
import sys
DELIMETER = ","
def GetInputFromStudent():
    lname = input("please enter name, then enter")
    lage = input("please enter age, then enter")
    lemail = input("please enter email, then enter")
    lcourseid = input("please enter couse id, then enter")
    lstatus = input("please enter Admission status [A/D] :, then enter")
    return StudentMaster(lname, lage, lemail, lcourseid, lstatus)

class StudentMaster:
    def __init__(self, lname, lage, lemail, lcourse, lstatus):
        self.name = lname
        self.age = lage
        self.email = lemail
        self.course = lcourse
        self.status = lstatus

def CreateDataFile():
    if os.path.isfile("C:\deba\deba5\\training\python\github\python\das.txt"):
        return open("das.txt", "r+")
    else:
        return open("das.txt", "w+")

def OpenMenuFile(mode):
    return open("menu.txt", mode)

def StoreData(file, data):
    record=data.name + DELIMETER + data.age + DELIMETER + data.email + DELIMETER + data.course + DELIMETER + data.status
    #file.writelines(record)
    if file.mode=="r+":
        file.seek(0,2)
        file.write("\n")
        file.write(record)
    elif file.mode=="w+":
        file.writelines(record)
    file.close()

def StoreMenu(file):
    record="Admission\n" + "Adm Report\n" + "Enquiry by email id\n" + "Exit"
    file.writelines(record)
    file.close()

def ReadFile(file):
    record_list = []
    for line in file:
        record_list.append(line.strip())
    print(record_list)
    return record_list


def PrintRecord(record_list):
    count=0
    for r in record_list:
        print("{}. {}".format(count+1,record_list[count]))
        count +=1

def DisplayData(file):
    count = 0
    for line in file:
        count += 1
        print("Record{}: {}".format(count, line.strip()))
    file.close()

def SearchData(file,attr,criteria):
    count = 0
    lines = file.readlines()
    if attr == "name":
        count = 0
        for row in lines:
            count += 1
            if repr(row).startswith(criteria,1):
                print("Record no {} : {}".format(count,row))
    file.close()


def DisplayMenu():
    menufile = OpenMenuFile("r")
    record_list = ReadFile(menufile)
    PrintRecord(record_list)
    choice = input("Enter choice :")
    menufile.close()
    return choice


if __name__ == '__main__':
    file = OpenMenuFile("w+")
    StoreMenu(file)
    choice=DisplayMenu()
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
            criteria=input("enter string : ")
            file = CreateDataFile()
            SearchData(file,"name",criteria)
        elif choice == "4":
            sys.exit(0)
        choice=DisplayMenu()