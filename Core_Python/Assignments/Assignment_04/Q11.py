# WAP to check if given number is Strong Number (any number)

n = int(input("Enter any number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10          # take last digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i        # factorial of that digit
    sum = sum + fact           # add factorial to sum
    temp = temp // 10          # remove last digit

if sum == n:
    print("It's a Strong Number")
else:
    print("It's not a Strong Number")
  