# Q5. Sort a List According to Length of Elements

lst = ["apple", "hi", "banana", "car"]

for i in range(len(lst)):
    for j in range(len(lst)-1):
        if len(lst[j]) > len(lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted by Length =", lst)
