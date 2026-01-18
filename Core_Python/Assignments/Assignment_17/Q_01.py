# 1. Create a class Student with following
    # a. data members :
        # i. StudentId
        # ii. Name
        # iii. Age
        # iv. Percentage
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. Method CalculateRank
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
    
    
std1 = Student(101, 'Kunal', 22, 81)
print(std1.display())
print(std1.calculateRank())
print(std1.accept())
print(std1)
    
    
    
    
    
    