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


def PrintData():
    for x in student_list:
        print("name is ", student_list[0]['name'])
        print("age is ", student_list[0]['age'])
        print("email is ", student_list[0]['email'])
        print("course is ", student_list[0]['course'])


if __name__ == '__main__':
    GetInputFromStudent()
    #StoreStudentData()
    StoreStudentDataIntoDict()
    PrintData()