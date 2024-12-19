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


corners = 0

def count_sides(x,y, letter):
    edge = 0
    if (not in_map(x, y - 1) or input[y - 1][x] != letter) and (not in_map(x + 1, y) or input[y][x + 1] != letter):
        edge += 1
    if (not in_map(x, y - 1) or input[y - 1][x] != letter) and (not in_map(x - 1, y) or input[y][x - 1] != letter):
        edge += 1
    if (not in_map(x, y + 1) or input[y + 1][x] != letter) and (not in_map(x - 1, y) or  input[y][x - 1] != letter):
        edge += 1
    if (not in_map(x, y + 1) or input[y + 1][x] != letter) and (not in_map(x + 1, y) or  input[y][x + 1] != letter):
        edge += 1
    # Diagonal checks for internal corners
    if in_map(x - 1, y - 1) and input[y - 1][x - 1] != letter:  # Top-Left diagonal
        if (in_map(x, y - 1) and input[y - 1][x] == letter) and (in_map(x - 1, y) and input[y][x - 1] == letter):
            edge += 1

    if in_map(x + 1, y - 1) and input[y - 1][x + 1] != letter:  # Top-Right diagonal
        if (in_map(x, y - 1) and input[y - 1][x] == letter) and (in_map(x + 1, y) and input[y][x + 1] == letter):
            edge += 1

    if in_map(x - 1, y + 1) and input[y + 1][x - 1] != letter:  # Bottom-Left diagonal
        if (in_map(x, y + 1) and input[y + 1][x] == letter) and (in_map(x - 1, y) and input[y][x - 1] == letter):
            edge += 1

    if in_map(x + 1, y + 1) and input[y + 1][x + 1] != letter:  # Bottom-Right diagonal
        if (in_map(x, y + 1) and input[y + 1][x] == letter) and (in_map(x + 1, y) and input[y][x + 1] == letter):
            edge += 1

    return edge


def bfs(x, y, next, letter, vis):
    global corners
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

    corners += count_sides(x,y,letter)

    next.append(temp)
    # umfang für jetzige position
    bfs(x + 1, y,  next, letter, vis)
    bfs(x - 1, y,  next, letter, vis)
    bfs(x, y + 1,  next, letter, vis)
    bfs(x, y - 1,  next, letter, vis)


visited = set()
result = 0
new_result = 0
for i in range(h):
    for j in range(w):
        if (j, i) in visited:
            continue
        a = 0
        p = 0
        vis = set()
        peri_list = []
        corners = 0
        bfs(j, i, peri_list, input[i][j], vis)
        # print(f"{input[i][j]} area={len(vis)} peri={sum(peri_list)}")
        result += sum(peri_list) * len(vis)
        # print(input[i][j], len(vis), corners)
        new_result += corners * len(vis)

        for x in vis:
            visited.add(x)
        # Call bfs
print(result)
print(new_result)
