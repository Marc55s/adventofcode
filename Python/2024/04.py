from lib import *

input = read_input(2024, 4).strip()
input = input.split("\n")

w = len(input[0])
h = len(input)
map = [[0 for x in range(w)] for y in range(h)]
for index, i in enumerate(input):
    for index2, k in enumerate(i):
        map[index][index2] = k


def in_range(x, y):
    return x >= 0 and x < w and y >= 0 and y < h


letters = ["M", "A", "S"]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (-1, 1), (1, -1), (-1, -1), (1, 1)]


def p1(x,  y):
    sum = 0
    for dir in directions:
        nx, ny = dir
        valid = True
        new_x = x + nx
        new_y = y + ny

        for letter in letters:
            if not in_range(new_x, new_y):
                valid = False
                break
            if (map[new_y][new_x] != letter):
                valid = False
                break
            new_x += nx
            new_y += ny
        if valid:
            sum += 1
    return sum


def p2(x, y):
    mas = []
    if in_range(x+1, y+1) and in_range(x-1, y+1) and in_range(x+1, y-1) and in_range(x-1, y-1):
        mas.append(map[y+1][x+1])  # Bottom-right
        mas.append(map[y-1][x+1])  # Top-right
        mas.append(map[y+1][x-1])  # Bottom-left
        mas.append(map[y-1][x-1])  # Top-left
    else:
        return False

    return mas.count("M") == 2 and mas.count("S") == 2 and mas[0] != mas[3]


ans = 0
ans2 = 0
for i in range(h):
    for k in range(w):
        pos = (map[i][k])
        if pos == "X":
            ans += p1(k, i)
        if pos == "A":
            if p2(k, i):
                ans2 += 1
print(ans)
print(ans2)
