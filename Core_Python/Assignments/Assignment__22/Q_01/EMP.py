import pickle

class Emp:
    
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def save(self):
        with open("emp.dat", "ab") as fp:   # append binary
            pickle.dump(self, fp)

    @staticmethod
    def show_all():
        try:
            with open("emp.dat", "rb") as fp:
                print("----- Employee Records -----")
                while True:
                    try:
                        emp = pickle.load(fp)
                        print(f"EID: {emp.eid}, Name: {emp.ename}, Basic: {emp.basic}")
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No records found")
            
e1 = Emp(101, "Kunal", "AIML")
e2 = Emp(102, "Lalit", "AIML")
e3 = Emp(103, "Om", "AIML")
e4 = Emp(104, "Lokesh", "AIML")
e5 = Emp(105, "Vivek", "AIML")
e6 = Emp(106, "Ankit", "AIML")

e1.save()
e2.save()
e3.save()
e4.save()
e5.save()
e6.save()

Emp.show_all()

