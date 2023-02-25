"""
how to read comma separator lines and then place them in list of dictionary items
"""

import os

fileName = "db.txt"
file = open(fileName, "r+")
recordList = []
file.seek(0, 0)
count = 0
for line in file:
    count += 1
    recordList.append(line.strip())


mylist = []
for i in recordList:
    count=0
    mydict = {}
    for i in i.split(','):
        if count == 0:
            mydict['Name'] = i
            #print("name is "+i)
        elif count == 1:
            mydict['Age'] = i
            #print("age is "+i)
        elif count == 2:
            mydict['Email'] = i
            #print("email is "+i)
        elif count == 3:
            mydict['Course'] = i
            #print("course is "+i)
        elif count == 4:
            mydict['Status'] = i
            #print("status is "+i)
        count+=1
    mylist.append(mydict)

for i in mylist:
    for key, value in i.items():
        print("{} -> {}".format(key,value))
