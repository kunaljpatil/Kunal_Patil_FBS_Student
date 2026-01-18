# Find all of the numbers from 1–1000 that are divisible by 8
li = [i for i in range(1, 1001) if (i % 8 == 0)]
print(li)
print()


# Find all of the numbers from 1–1000 that have a 6 in them
li1 = [i for i in range(1,1001) if '6' in str(i)] 
print(li1)


# Write A Python Program Count the number of spaces in a string (take input from user)
s = input("Enter A String: ")
sp = sum([1 for ch in s if ch == ' '])
print(sp)


# Write A Python Program Remove all of the vowels in a string (take input from user)
s = input("Enter A String: ")
vowels = 'aeiouAEIOU'
sp = ''.join ([ch for ch in s if ch not in vowels])
print(sp)


# Write A Python Program Find all of the words in a string that are less than 5 letters (take input from user)
s = input("Enter a String: ")
words = s.split(" ")
print(words)

new = [i for i in words if len(i) < 5]
print(new)

    
# Write A Python Program Find all of the words in a string that are less than 5 letters (take input from user)
dic1 = input("Enter A Values: ")
words = dic1.split()

length_words = {w: len(w) for w in words}
print(length_words)


# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.
result = [n for n in range(1, 1001) if any(n % d == 0 for d in range(1, 10))]
print(result)

