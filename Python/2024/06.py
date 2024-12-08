from lib import *
from collections import Counter

input = read_input(2024, 6).strip()
input = input.split("\n")

w = len(input[0])
h = len(input)

global guard

for i in range(h):
    input[i] = list(input[i])
    for k in range(w):
        if input[i][k] == '^':
            guard = (k, i)



def in_map(x, y):
    return x >= 0 and x < w and y >= 0 and y < h


def print_map(m):
    for i in range(h):
        for k in range(w):
            print(m[i][k], end="")
        print()


dir = (0, -1)
right_directions = {(0, -1): (1, 0), (1, 0): (0, 1),
                    (0, 1): (-1, 0), (-1, 0): (0, -1)}


def take_step(guard, dir):
    x = guard[0] + dir[0]
    y = guard[1] + dir[1]
    return (x, y)


def turn_right(dir):
    return right_directions[dir]


visited = set()
ans = 0


def walk(guard, dir):
    dx, dy = take_step(guard, dir)
    while True:
        if not in_map(dx, dy):
            return
        if input[dy][dx] == '#':
            dir = turn_right(dir)
        else:
            guard = take_step(guard, dir)
        visited.add(guard)
        dx, dy = guard[0] + dir[0], guard[1]+dir[1]


walk(guard, dir)


print(len(visited))
