fileName = "menu.txt"


class Menu:
    choice = ""

    def insert(self):
        self.file = open(fileName, "w+")
        record = "Admission\n" + "Adm Report\n" + "Enquiry by email id\n" + "Exit"
        self.file.writelines(record)
        self.file.close()

    def display(self):
        self.file = open(fileName, "r+")
        record_list = []
        for line in self.file:
            record_list.append(line.strip())
        count = 0
        for r in record_list:
            print("{}. {}".format(count + 1, record_list[count]))
            count += 1
        Menu.choice = input("Enter choice :")
        self.file.close()

    def test1(self,yy):
        print("testing")
