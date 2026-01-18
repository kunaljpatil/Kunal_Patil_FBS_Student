# Q11. Replace Every Blank Space with Hyphen (duplicate of Q6)



s = input("Enter string: ")
new = ""

for ch in s:
    if ch == ' ':
        new = new + '-'
    else:
        new = new + ch

print("New string =", new)
