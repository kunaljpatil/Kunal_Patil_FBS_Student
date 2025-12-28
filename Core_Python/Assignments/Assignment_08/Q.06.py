# Q4. Sum of all odd numbers between 1 to n.

n = int(input("Enter a number: "))

for i in range(1, n):
    if(n % 2 == 0 and n % 3 == 0):
        print("The given value is divisible by 2 and 3: ", n)
        break
else:
    print("The Given Value is not divisibile by 2 and 3", n)
