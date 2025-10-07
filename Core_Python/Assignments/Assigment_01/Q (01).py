# find percentage of marks of students

# take marks as input from user 
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))   
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

# perform operation to find percentage
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
print("Percentage of student is:", percentage,"\n")
print("type of percentage is:", type(percentage),"\n")

#display percentage 

print(f'Percentage of student is :{percentage}%',"\n") # f string is use for formatted string at one place

# Here we can see that the percentage is in float format because division operation always gives float value
# if we want to convert it into integer we can use int() function
percentage_int = int(percentage)
print("Percentage of student in integer is:", percentage_int)
print("type of percentage is:", type(percentage_int),"\n")