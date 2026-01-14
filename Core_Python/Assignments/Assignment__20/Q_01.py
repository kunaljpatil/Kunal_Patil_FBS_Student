# Write a program to
# 1. Create object of student class (Outside SY & TY package) having roll number, name, SYMakrs and TYMarks. Add the marksof SY and TY Computer subjects and calculate grade ("A" for >=70, "B" for >=60, "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result of the student in proper format.

class Student:
    def __init__(self, roll_no, name, SYmarks, TYmarks):
        self.roll_no = roll_no
        self.name = name
        self.SYmarks = SYmarks
        self.TYmarks = TYmarks
        
    def grade(self):
        grades = self.SYmarks.total() + self.TYmarks.total()
        if (grades >= 70):
            return f"You Got A Grade!!"
        elif (grades >= 60):
            return f"You Got B Grade!!"
        elif (grades >= 50):
            return f"You Got C Grade!!"
        elif (grades >= 70):
            return "You Are Pass Class !!"   
        else:
            return "You Are Fail!!!"
    
    def display(self):
        print(f"Student Roll No: {self.roll_no}")
        print(f"Student Name: {self.name}")
        print(f"SY Marks (C+M+E): {self.SYmarks.total()}")
        print(f"TY Marks (T+P): {self.TYmarks.total()}")
        print(f"Total Marks: {self.SYmarks.total() + self.TYmarks.total()}")
        print(f"Grade: {self.grade()}\n")
        
        
        
#2 Create a package “SY” which has class SYMARKS (Computer Total MathsTotal, ElectronicsTotal).
class SYmarks:
    def __init__(self, computertotal, mathstotal, electronicstotal):
        # super().__init__(roll_no, name, SYmarks, TYmarks)
        self.computertotal = computertotal
        self.mathstotal = mathstotal
        self.electronicstotal = electronicstotal
        
    def total(self):
        return self.computertotal + self.mathstotal + self.electronicstotal
        
        
#3 Create another package “TY” which has a class TYMarks (Theory, Practical).
class TYmarks:
    def __init__(self, Theory, Practical):
        # super().__init__(roll_no, name, SYmarks, TYmarks)
        self.Theory = Theory
        self.Practical = Practical 
    
    def total(self):
        return self.Theory + self.Practical 
        
        
s = SYmarks(90, 70, 88)
t = TYmarks(80, 99)
student1 = Student(101, "Kunal", s, t)
student1.display()

