import os
import sys

def GetInputFromStudent():
    global lname, lage, lemail, lcourseid
    lname = input("please enter name, then enter")
    lage = input("please enter age, then enter")
    lemail = input("please enter email, then enter")
    lcourseid = input("please enter couse id, then enter")


def StoreStudentData():
    global student_list
    # print(lname,lage,lemail,lcourseid)
    student_list = []
    D = {'name': lname, 'age': lage, 'email': lemail, 'course': lcourseid}
    # D = dict(lname={'age':lage,'email':lemail,'curse':lcourseid})
    student_list.append(D)

class StudentMaster:
    def __init__(self, lname, lage, lemail, lcourse):
        self.name = lname
        self.age = lage
        self.email = lemail
        self.course = lcourse

def StoreStudentDataIntoDict():
    global student_dict
    student_dict = {}
    studentMaster1 = StudentMaster(lname,lage,lemail,lcourseid)
    student_dict[lname]=studentMaster1
    #print(student_dict[lname].name)


def PrintData():
    for x in student_list:
        print("name is ", student_list[0]['name'])
        print("age is ", student_list[0]['age'])
        print("email is ", student_list[0]['email'])
        print("course is ", student_list[0]['course'])

def StoreDataToFile():
    global final_dict
    final_dict= {}
    os.chdir("C:/deba/deba5/training/python/pythonTrainingProject")
    mycurdir = os.getcwd()
    if mycurdir != "C:\deba\deba5\\training\python\pythonTrainingProject":
        print("not a correct directory, doing nothing")
    else:
        print("correct directory, doing nothing")
    try:
        print(student_dict.keys())
        fo = open("das.txt", "w+")
        # print(type(fo))
        # print(fo.mode)
        for r in student_dict.keys():
            #final_dict[r]={"age":str(student_dict[r].name,"email":str(student_dict[r].email,"course":str(student_dict[r].course}
            myvar = "{ \"" + r + "\" : { \"age\" : \"" + student_dict[r].age + "\", \"email\" : \"" + student_dict[r].email + "\", \"course\" : \"" + student_dict[r].course + "\" }}"
            print(myvar)
            fo.write(myvar)
        fo.close()
    except FileNotFoundError as e:
        print("unable to open file ", sys.exc_info()[0], sys.exc_info()[1])
    except PermissionError as e:
        print("permission error", sys.exc_info()[0], sys.exc_info()[1])
    except IsADirectoryError:
        print("Error related to directory", sys.exc_info()[0], sys.exc_info()[1])



if __name__ == '__main__':
    GetInputFromStudent()
    #StoreStudentData()
    StoreStudentDataIntoDict()
    #PrintData()
    StoreDataToFile()