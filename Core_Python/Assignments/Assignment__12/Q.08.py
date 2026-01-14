# Q8. Remove Characters at Odd Index Values

s = input("Enter string: ")
new = ""

for i in range(len(s)):
    if i % 2 == 0:
        new = new + s[i]

print("New string =", new)
