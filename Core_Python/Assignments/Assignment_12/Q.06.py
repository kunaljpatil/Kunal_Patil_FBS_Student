# Q6. Replace Every Blank Space with Hyphen

s = input("Enter string: ")
new = ""

for ch in s:
    if ch == ' ':
        new = new + '-'
    else:
        new = new + ch

print("New string =", new)
