# 2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.

Student_num =int(input("Enter number of students : "))

for i in range(1,Student_num+1):
    total_marks=0
    total_percentage=0
    print(f"\n Enter Marks of 5 subjects for {i}  student ")

    for j in range(1,6):
        marks=int(input(f'Enter marks of subject {j} : '))
        total_marks+=marks
    percentage= round((total_marks/500)*100,3)
    print(f'Percentage of student {i} is : {percentage}% \n')
    
    total_percentage+=percentage

avg_percentage = total_percentage/Student_num
print(f'The average percentage of {Student_num} student is :{avg_percentage}%')

