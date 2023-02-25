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
    def insert(lname, lage, lemail, lcourseid, lstatus):
        studentdata = StudentMaster(lname, lage, lemail, lcourseid, lstatus)
        record = studentdata.name + DELIMETER + studentdata.age + DELIMETER + studentdata.email + DELIMETER + studentdata.course + DELIMETER + studentdata.status
        i = -1
        for i, line in enumerate(file):
            pass
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
        recordList = []
        file.seek(0, 0)
        count = 0
        for line in file:
            count += 1
            #print("Record{}: {}".format(count, line.strip()))
            recordList.append(line.strip())
        return recordList

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
