# Write a program to enter P, T, R and calculate Compound Interest.

# take principal, time and rate as input from user
P = int(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = int(input("Enter Time in years: "))

# perform operation to find compound interest
CI = P * ( (1 + R / 100) ** T ) - P
print("Compound Interest is:", CI,"\n")
print("type of Compound Interest is:", type(CI),"\n")

#display compound interest
print(f'Compound Interest is :{CI}') # f string is use for formatted string at one place 