import os

from StudentClass import StudentMaster

DELIMETER = ","
fileName = "db.txt"

if os.path.isfile(fileName):
    file = open(fileName, "r+")
else:
    file = open(fileName, "w+")


class Database:

    @staticmethod
    def insert():
        lname = input("please enter name, then enter")
        lage = input("please enter age, then enter")
        lemail = input("please enter email, then enter")
        lcourseid = input("please enter course id, then enter")
        lstatus = input("please enter Admission status [A/D] :, then enter")
        studentdata = StudentMaster(lname, lage, lemail, lcourseid, lstatus)
        record = studentdata.name + DELIMETER + studentdata.age + DELIMETER + studentdata.email + DELIMETER + studentdata.course + DELIMETER + studentdata.status
        i = -1
        for i, line in enumerate(file):
            pass
        print("line no: ", i)
        if file.mode == "r+":
            if i == -1:
                file.seek(0, 0)
            else:
                file.seek(0, 2)
                file.write("\n")
            file.write(record)
        elif file.mode == "w+":
            file.writelines(record)
            file.write("\n")
        file.seek(0, 0)

    @staticmethod
    def select():
        file.seek(0, 0)
        count = 0
        for line in file:
            count += 1
            print("Record{}: {}".format(count, line.strip()))

    @staticmethod
    def close():
        if file.mode == "r+":
            file.close()
        elif file.mode == "w+":
            file.close()

    @staticmethod
    def search(attr, criteria):
        file.seek(0, 0)
        lines = file.readlines()
        if attr == "name":
            count = 0
            for row in lines:
                count += 1
                if repr(row).startswith(criteria, 1):
                    print("Record no {} : {}".format(count, row))
