# Q3. Write a program to find the second largest element in the list.

lst = [12, 5, 18, 7, 18, 3]

largest = lst[0]
second = -99999   # very small value

for x in lst:
    if x > largest:
        second = largest
        largest = x
    elif x != largest and x > second:
        second = x

print("Second Largest =", second)

