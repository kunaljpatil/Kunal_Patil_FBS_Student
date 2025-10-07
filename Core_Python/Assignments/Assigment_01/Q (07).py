# Program to Find the Roots of a Quadratic Equation

# take coefficients a, b and c as input from user
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)
sqrt_val = d**0.5 # or use import math and then math.sqrt(d)
# find two solutions
sol1 = (-b + sqrt_val) / (2 * a)
sol2 = (-b - sqrt_val) / (2 * a)
print("The solutions are {0} and {1}".format(sol1, sol2))