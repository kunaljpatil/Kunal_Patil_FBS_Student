# Q2. Remove the nth Index Character from a Non-Empty String

s = input("Enter string: ")
n = int(input("Enter index: "))

new = ""

for i in range(len(s)):
    if i != n:
        new = new + s[i]

print("After removing character:", new)
