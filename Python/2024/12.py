from lib import *
from copy import deepcopy

input = read_input(2024, 12).strip()
input = input.split("\n")
w = len(input[0])
h = len(input)


def in_map(x, y):
    return x >= 0 and x < w and y >= 0 and y < h


for i in range(h):
    input[i] = list(input[i])


def bfs(x, y, next, letter, vis):
    if not in_map(x, y):
        return 0
    if (x, y) in vis:
        return 0
    if input[y][x] != letter:
        return 0
    vis.add((x, y))
    temp = 4
    if in_map(x, y - 1) and input[y - 1][x] == letter:
        temp -= 1
    if in_map(x, y + 1) and input[y + 1][x] == letter:
        temp -= 1
    if in_map(x + 1, y) and input[y][x + 1] == letter:
        temp -= 1
    if in_map(x - 1, y) and input[y][x - 1] == letter:
        temp -= 1
    next.append(temp)
    # umfang für jetzige position
    bfs(x + 1, y,  next, letter, vis)
    bfs(x - 1, y,  next, letter, vis)
    bfs(x, y + 1,  next, letter, vis)
    bfs(x, y - 1,  next, letter, vis)


visited = set()
result = 0
for i in range(h):
    for j in range(w):
        if (j, i) in visited:
            continue
        a = 0
        p = 0
        vis = set()
        peri_list = []
        bfs(j, i, peri_list, input[i][j], vis)
        # print(f"{input[i][j]} area={len(vis)} peri={sum(peri_list)}")
        result += sum(peri_list) * len(vis)

        for x in vis:
            visited.add(x)
        # Call bfs
print(result)