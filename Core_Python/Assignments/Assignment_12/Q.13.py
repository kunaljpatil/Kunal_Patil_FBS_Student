# Q13. Count Number of Digits and Letters in a String

s = input("Enter string: ")

letters = 0
digits = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        digits = digits + 1
    else:
        letters = letters + 1

print("Digits =", digits)
print("Letters =", letters)
