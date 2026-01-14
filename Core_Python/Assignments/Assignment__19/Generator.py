# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
g = fib(20)  

print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 


print("-------------------------")
# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

# Numeric palindrome check
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return original == rev

# Infinite palindrome generator
def palindrome_generator():
    n = 0
    while True:               
        if is_palindrome(n):
            yield n
        n += 1

pd = palindrome_generator()

for _ in range(15):
    print(next(pd))
    
    
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4
print(next(pd))  # 4


print("-------------------------")  
print()
# Write a generator function that mimics the behavior of the built-in range() function. The generator should take start, stop, and step arguments and yield numbers within the specified range.

def my_range(start, stop, step=1):
    """Generator function that mimics Python's built-in range()"""
    
    # Handle positive step
    if step > 0:
        while start < stop:
            yield start
            start += step
    # Handle negative step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError("step argument must not be zero")
    
# Test the my_range generator
for num in my_range(0, 10, 2):                      
    print(num)  