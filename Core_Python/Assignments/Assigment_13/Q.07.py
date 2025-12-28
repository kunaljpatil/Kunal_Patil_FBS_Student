
# Q7. Remove the Given Key from a Dictionary


d = {1: "one", 2: "two", 3: "three"}
key = int(input("Enter key to remove: "))

new = {}

for k in d:
    if k != key:
        new[k] = d[k]

print("Dictionary after removal =", new)
