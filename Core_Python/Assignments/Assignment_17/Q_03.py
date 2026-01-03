# 3. Create a class MedicalStudent inherited from Student with following: 
        # i. Data members :Specialization
        # ii. MarksOfInternship
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. override Method CalculateRank
        # v. Override __str__ Method
class Student:
    def __init__(self, sid, name, age, percentage):
        self.sid = sid 
        self.name = name 
        self.age = age 
        self.percentage = percentage 
        
    def display(self):
        return (
            f'STUDENT ID: {self.sid}\n'
            f'STUDENT NAME: {self.name}\n'
            f'STUDENT AGE: {self.age}\n'
            f'PERCENTAGE: {self.percentage}'
            )
        
    def accept(self):
        self.sid = int(input("Enter A Student ID: "))
        self.name = input("Enter A Student NAME: ")
        self.age = int(input("Enter A Student AGE: "))
        self.percentage = float(input("Enter A Student PERCENTAGE: "))
        return "Details Accepted Successfully"
        
        
    def calculateRank(self):
        if self.percentage >= 90:
            data = f"The Given Student {self.sid} is TOP 1% RANK" 
        elif self.percentage >= 80:
            data = f"The Given Student {self.sid} is 1%-10% RANK"
        elif self.percentage >= 70:
             data = f"The Given Student {self.sid} is 11%-20% RANK"
        elif self.percentage >= 60:
             data = f"The Given Student {self.sid} is 21%-30% RANK"
        elif self.percentage >= 50:
             data = f"The Given Student {self.sid} is 31%-40% RANK"
        elif self.percentage < 50:
             data = f"The Given Student {self.sid} is Below 40% RANK"
        return data 
        
    def __str__(self):
        return (
            f'STUDENT ID: {self.sid}\n'
            f'STUDENT NAME: {self.name}\n'
            f'STUDENT AGE: {self.age}\n'
            f'PERCENTAGE: {self.percentage}'
            )
    
# std1 = Student(101, 'Kunal', 22, 81)
# print(std1.display())
# print(std1.calculateRank())
# print(std1.accept())
# print(std1)
    
class MedStudent(Student):
    
    total_marks = 150

    def __init__(self, sid, name, age, percentage , specialization, internship_marks):
        super().__init__(sid, name, age, percentage)
        self.specialization = specialization 
        self.internship_marks = internship_marks 
        self.total_marks = MedStudent.total_marks
    
    def display(self):
        return (
            f'STUDENT ID: {self.sid}\n'
            f'STUDENT NAME: {self.name}\n'
            f'STUDENT AGE: {self.age}\n'
            f'PERCENTAGE: {self.percentage}\n'
            f'Specialization: {self.specialization}\n'
            f'INTERNSHIP MARKS: {self.internship_marks}'
            )
            
    def accept(self):
        self.sid = int(input("Enter A Student ID: "))
        self.name = input("Enter A Student NAME: ")
        self.age = int(input("Enter A Student AGE: "))
        self.percentage = float(input("Enter A Student PERCENTAGE: "))
        self.specialization = input("Enter specialization NAME: ")
        self.internship_marks = int(input("Enter INTERNSHIP MARKS: "))
        return "Details Accepted Successfully"
    
    def calculateRank(self):
        self.final_score = self.percentage + self.internship_marks 
        
        if self.final_score >= 135:
            data = f"The Given Student {self.sid} is TOP 1% RANK" 
        elif self.final_score >= 120:
            data = f"The Given Student {self.sid} is 1%-10% RANK"
        elif self.final_score >= 105:
             data = f"The Given Student {self.sid} is 11%-20% RANK"
        elif self.final_score >= 90:
             data = f"The Given Student {self.sid} is 21%-30% RANK"
        elif self.final_score >= 75:
             data = f"The Given Student {self.sid} is 31%-40% RANK"
        elif self.final_score >= 60:
             data = f"The Given Student {self.sid} is 40%-50% RANK"
        else:
             data = f"The Given Student {self.sid} is Below 40% RANK"

        return data
    
    def __str__(self):
        return (
            f'STUDENT ID: {self.sid}\n'
            f'STUDENT NAME: {self.name}\n'
            f'STUDENT AGE: {self.age}\n'
            f'PERCENTAGE: {self.percentage}\n'
            f'Specialization: {self.specialization}\n'
            f'INTERNSHIP MARKS: {self.internship_marks}'
            )
            
med1 = MedStudent(101, 'Kunal', 22, 81, 'aiml', 30)
print(med1.display())
print(med1.calculateRank())
print(med1.accept())
print(med1)
    