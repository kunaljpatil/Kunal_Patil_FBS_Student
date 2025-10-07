# Write a program to enter P, T, R and calculate simple Interest.

# take principal, time and rate as input from user
P = int(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))   
T = int(input("Enter Time in years: "))     
 

# perform operation to find simple interest
SI = (P * R * T) / 100
print("Simple Interest is:", SI,"\n")
print("type of Simple Interest is:", type(SI),"\n")

#display simple interest
print(f'Simple Interest is :{SI}') # f string is use for formatted string at one place
