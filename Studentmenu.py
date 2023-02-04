def OpenMenuFile(mode):
    return open("menu.txt", mode)


def StoreMenu():
    file = OpenMenuFile("w+")
    record = "Admission\n" + "Adm Report\n" + "Enquiry by email id\n" + "Exit"
    file.writelines(record)
    file.close()


def MenuReadFile(file):
    record_list = []
    for line in file:
        record_list.append(line.strip())
    # print(record_list)
    return record_list


def MenuPrintRecord(record_list):
    count = 0
    for r in record_list:
        print("{}. {}".format(count + 1, record_list[count]))
        count += 1


def DisplayMenu():
    menufile = OpenMenuFile("r")
    record_list = MenuReadFile(menufile)
    MenuPrintRecord(record_list)
    choice = input("Enter choice :")
    menufile.close()
    return choice