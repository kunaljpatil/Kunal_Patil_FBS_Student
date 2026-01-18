# Q7. Create a new list containing cube of each element.

lst = [2, 3, 4, 5]
cube_list = []

for x in lst:
    cube_list = cube_list + [x*x*x]

print("Cube List =", cube_list)


