# Q8. Print 1 to 100 in Snake and Ladder Pattern

num = 1

for row in range(1, 11):
    line = []

    for col in range(10):
        line = line + [num]
        num = num + 1

    if row % 2 == 0:
        # reverse for snake pattern
        rev = []
        for i in range(9, -1, -1):
            rev = rev + [line[i]]
        line = rev

    print(line)
