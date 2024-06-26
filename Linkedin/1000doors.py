doors = [False] * 101
for i in range(1,101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

print(', '.join(str(i) for i in range(1,101) if doors[i] == True))

