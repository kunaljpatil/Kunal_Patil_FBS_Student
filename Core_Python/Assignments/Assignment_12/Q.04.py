# Q4. Form a New String by Exchanging First and Last Character

s = input("Enter string: ")

new = s[-1] + s[1:-1] + s[0]

print("New string =", new)
