# Q10. Remove all occurrences of a given element in the list.


lst = [3, 7, 3, 2, 3, 9]
n = int(input("Enter element to remove: "))

new = []

for x in lst:
    if x != n:
        new = new + [x]

print("List after removal =", new)
