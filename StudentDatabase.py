import os
import sys
sys.path.append('C:/deba/deba5/training/python/github/python')
from StudentClass import StudentMaster
DELIMETER = ","

def GetInputFromStudent():
    lname = input("please enter name, then enter")
    lage = input("please enter age, then enter")
    lemail = input("please enter email, then enter")
    lcourseid = input("please enter couse id, then enter")
    lstatus = input("please enter Admission status [A/D] :, then enter")
    return StudentMaster(lname, lage, lemail, lcourseid, lstatus)

def CreateDataFile():
    if os.path.isfile("C:\deba\deba5\\training\python\github\python\das.txt"):
        return open("das.txt", "r+")
    else:
        return open("das.txt", "w+")

def StoreData(file, data):
    record = data.name + DELIMETER + data.age + DELIMETER + data.email + DELIMETER + data.course + DELIMETER + data.status
    # file.writelines(record)
    if file.mode == "r+":
        file.seek(0, 2)
        file.write("\n")
        file.write(record)
    elif file.mode == "w+":
        file.writelines(record)
    file.close()

def DisplayData(file):
    count = 0
    for line in file:
        count += 1
        print("Record{}: {}".format(count, line.strip()))
    file.close()

def SearchData(file, attr, criteria):
    count = 0
    lines = file.readlines()
    if attr == "name":
        count = 0
        for row in lines:
            count += 1
            if repr(row).startswith(criteria, 1):
                print("Record no {} : {}".format(count, row))
    file.close()