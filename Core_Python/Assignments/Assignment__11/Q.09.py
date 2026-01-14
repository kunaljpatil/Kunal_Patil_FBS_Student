# Q9. Create three lists: numbers, their squares, and cubes

nums = [1, 2, 3, 4, 5]

squares = []
cubes = []

for x in nums:
    squares = squares + [x * x]
    cubes = cubes + [x * x * x]

print("Numbers =", nums)
print("Squares =", squares)
print("Cubes =", cubes)
