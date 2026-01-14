# Program to find quotient and remainder of two numbers.

# take two numbers as input from user
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

# perform operation to find quotient and remainder
quotient = num1 // num2
remainder = num1 % num2

print("Quotient of", num1, "and", num2, "is:", quotient)
print("Remainder of", num1, "and", num2, "is:", remainder)

print("type of quotient is:", type(quotient))
print("type of remainder is:", type(remainder))
