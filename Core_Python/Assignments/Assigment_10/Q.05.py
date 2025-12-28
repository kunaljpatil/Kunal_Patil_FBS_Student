# Q5. Accept a number from user and check if it is present in the list. Also count frequency.

lst = [3, 5, 3, 9, 1, 3]
n = int(input("Enter number: "))

count = 0
for x in lst:
    if x == n:
        count = count + 1

if count > 0:
    print(n, "is present", count, "times")
else:
    print(n, "is not present")
