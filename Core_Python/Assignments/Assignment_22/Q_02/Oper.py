class Emp:
    
    FILE = "emp.txt"

    # a. Add a record
    def add_rec(self):
        eid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")

        with open(Emp.FILE, "a") as fp:
            fp.write(f"{eid},{name},{salary}\n")

        print("Record Added Successfully")

    # e. Display all records
    def show_all(self):
        try:
            with open(Emp.FILE, "r") as fp:
                print("\n--- Employee Records ---")
                print(fp.read())
        except FileNotFoundError:
            print("No records found")

    # b. Search record using ID
    def search(self):
        eid = input("Enter Employee ID to Search: ")
        found = False

        with open(Emp.FILE, "r") as fp:
            for line in fp:
                record = line.strip().split(",")
                if record[0] == eid:
                    print("Record Found:", line)
                    found = True
                    break

        if not found:
            print("Record Not Found")

    # c. Delete record using ID
    def delete(self):
        eid = input("Enter Employee ID to Delete: ")
        records = []
        found = False

        with open(Emp.FILE, "r") as fp:
            records = fp.readlines()

        with open(Emp.FILE, "w") as fp:
            for line in records:
                if line.split(",")[0] != eid:
                    fp.write(line)
                else:
                    found = True

        if found:
            print("Record Deleted Successfully")
        else:
            print("Record Not Found")

    # d. Edit record using ID
    def edit(self):
        eid = input("Enter Employee ID to Edit: ")
        records = []
        found = False

        with open(Emp.FILE, "r") as fp:
            records = fp.readlines()

        with open(Emp.FILE, "w") as fp:
            for line in records:
                record = line.strip().split(",")
                if record[0] == eid:
                    name = input("Enter New Name: ")
                    salary = input("Enter New Salary: ")
                    fp.write(f"{eid},{name},{salary}\n")
                    found = True
                else:
                    fp.write(line)

        if found:
            print("Record Updated Successfully")
        else:
            print("Record Not Found")

    # Menu
    def menu(self):
        while True:
            print("""
1. Add Record
2. Search Record
3. Delete Record
4. Edit Record
5. Display All
6. Exit
""")
            ch = input("Enter Choice: ")

            if ch == "1":
                self.add_rec()
            elif ch == "2":
                self.search()
            elif ch == "3":
                self.delete()
            elif ch == "4":
                self.edit()
            elif ch == "5":
                self.show_all()
            elif ch == "6":
                print("Program Ended")
                break
            else:
                print("Invalid Choice")


e = Emp()
e.menu()
