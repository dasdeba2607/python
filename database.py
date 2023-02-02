
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