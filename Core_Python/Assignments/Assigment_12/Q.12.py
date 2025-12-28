# Q12. Count Number of Lowercase Characters in a String

s = input("Enter string: ")
count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count = count + 1

print("Lowercase characters =", count)
