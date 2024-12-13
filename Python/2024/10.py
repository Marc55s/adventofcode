from lib import *

input = read_input(2024, 10).strip()
input = input.split("\n")

w = len(input[0])
h = len(input)


def in_map(x, y):
    return x >= 0 and x < w and y >= 0 and y < h


def trail(x, y, old, vis, mode=0):
    # if (x, y) in vis or not in_map(x, y) or old + 1 != input[y][x]:
    if mode == 1:
        if not in_map(x, y) or old + 1 != input[y][x]:
            return 0
    else:
        if (x, y) in vis or not in_map(x, y) or old + 1 != input[y][x]:
            return 0

    vis.add((x, y))
    if input[y][x] == 9:
        return 1
    old = input[y][x]
    return trail(x+1, y, old, vis, mode) + trail(x-1, y, old, vis, mode) + trail(x, y + 1, old, vis, mode) + trail(x, y - 1, old, vis, mode)


trailheads = []
for i in range(h):
    input[i] = list(input[i])
    for k in range(w):
        input[i][k] = int(input[i][k])
        if input[i][k] == 0:
            trailheads.append((k, i))

sum = 0
ans2 = 0
for th in trailheads:
    x, y = th
    sum += trail(x, y, -1, set())
    ans2 += trail(x, y, -1, set(), 1)
print(sum)
print(ans2)
