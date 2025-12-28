# Write a Program to input two angles from user and find third angle of the triangle.

# take two angles as input from user
angle1 = int(input("Enter first angle of triangle: "))
angle2 = int(input("Enter second angle of triangle: "))

# perform operation to find third angle
angle3 = 180 - (angle1 + angle2)
print("Third angle of triangle is:", angle3,"\n") 