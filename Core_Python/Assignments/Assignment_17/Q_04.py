# 4. Create a class College which has collection of students. Add the following methods :
    # a. Parameteried constructor for number of students.
    # b. AddStudent
    # c. GetStudent
    # d. RemoveStudent
    # e. Override __str__ Method
    
# Student class
class Student:
    def __init__(self, sid, name, age, percentage):
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}"


# College class
class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []  # This list stores Student objects

    # Add a new student
    def addStudent(self):
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        percentage = float(input("Enter Student Percentage: "))
        new_student = Student(sid, name, age, percentage)
        self.students.append(new_student)
        return f"Student {sid} added successfully!"

    # Get student by ID
    def getStudent(self, search_id):
        for student in self.students:
            if student.sid == search_id:
                return str(student)
        return f"Student with ID {search_id} not found."

    # Remove student by ID
    def remStudent(self, search_id):
        for student in self.students:
            if student.sid == search_id:
                self.students.remove(student)
                return f"Student {search_id} removed successfully!"
        return f"Student {search_id} not found."

    # Print all students
    def __str__(self):
        if not self.students:
            return f"College {self.college_name} has no students."
        result = f"College: {self.college_name}\nStudents List:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result


# Example usage
c1 = College("ABC College")
print(c1.addStudent())           # Add a student
print(c1.addStudent())           # Add another student
print(c1.getStudent(101))        # Get student with ID 101
print(c1.remStudent(101))        # Remove student with ID 101
print(c1)                        # Print all students
