import os
import sys

if __name__ == '__main__':
    os.chdir("C:/deba/deba5/training/python/pythonTrainingProject")
    mycurdir=os.getcwd()
    if mycurdir!= "C:\deba\deba5\\training\python\pythonTrainingProject":
        print("not a correct directory, doing nothing")
    else:
        print("correct directory, doing nothing")
    try:
        fo = open("das.txt", "w+")
        #print(type(fo))
        #print(fo.mode)
        myname="deba"
        D = {myname: {"age": "50", "email": "d@d.com", "courseid": "25"}}
        fo.write(str(D))
        fo.close()
    except FileNotFoundError as e:
        print("unable to open file ",sys.exc_info()[0],sys.exc_info()[1])
    except PermissionError as e:
        print("permission error",sys.exc_info()[0],sys.exc_info()[1])
    except IsADirectoryError:
        print("Error related to directory",sys.exc_info()[0],sys.exc_info()[1])
