# Q3. Check if a Given Key Exists in a Dictionary

d = {10: "red", 20: "green", 30: "blue"}
k = int(input("Enter key to search: "))

found = False

for key in d:
    if key == k:
        found = True
        break

if found:
    print("Key exists in dictionary")
else:
    print("Key does not exist")
