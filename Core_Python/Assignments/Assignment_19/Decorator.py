# Develop a memoization decorator that caches the results of function calls and returns the cached result when the same inputs occur again. This can greatly improve the performance of recursive or computationally intensive functions.

def memo(fun):
    cache = {}
    def wrapper(n):
        print('----------------------------')
        if(n in cache):
            print("Output Available Of", n)
            return cache[n]
        output = fun(n)
        cache[n] = output
        print("Ouput Not Available Of", n)
        return output
        
    return wrapper

@memo
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


# Test
print(fact(5))  # Output Not Available, 120
print(fact(5))  # Output Available, 120
print(fact(6))  # Output Not Available, 720
print(fact(6))        
