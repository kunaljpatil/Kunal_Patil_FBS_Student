#Write a program to calculate area of rectangle based on length and breadth.

# take length and breadth as input from user
length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

# perform operation to find area
area = length * breadth
print("Area of rectangle is:", area,"\n")
print("type of area is:", type(area),"\n")

#display area
print(f'Area of rectangle is :{area}') # f string is use for formatted string at one place