# Q4. Write a program to reverse the list (without using reverse).

lst = [1, 2, 3, 4, 5]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev_len = len(rev)
    rev = rev + [lst[i]]

print("Reversed List =", rev)
