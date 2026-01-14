# Q1. Replace all occurrences of ‘a’ with $ in a string

s = input("Enter string: ")
new = ""

for ch in s:
    if ch == 'a':
        new = new + '$'
    else:
        new = new + ch

print("New String =", new)
