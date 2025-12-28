# Q5. Count Number of Vowels in a String

s = input("Enter string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total vowels =", count)
