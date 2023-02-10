fileName = "menu.txt"


class Menu:

    @staticmethod
    def insert():
        file = open(fileName, "w+")
        record = "Admission\n" + "Adm Report\n" + "Enquiry by email id\n" + "Exit"
        file.writelines(record)
        file.close()

    @staticmethod
    def display():
        file = open(fileName, "r+")
        record_list = []
        for line in file:
            record_list.append(line.strip())
        count = 0
        for r in record_list:
            print("{}. {}".format(count + 1, record_list[count]))
            count += 1
        choice = input("Enter choice :")
        file.close()
        return choice
