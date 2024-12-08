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


def take_step(g, dir):
    x = g[0] + dir[0]
    y = g[1] + dir[1]
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

obstructions = 0


for obstacle in visited:
    vis = set()
    dir = (0, -1)
    player = (guard[0], guard[1])

    map = [x[:] for x in input]
    x, y = obstacle
    map[y][x] = '#'

    # isloop
    while in_map(player[0], player[1]):
        next_player = take_step(player, dir)

        if not in_map(player[0], player[1]):
            break

        if (next_player, dir) in vis:
            obstructions += 1
            break

        if not in_map(next_player[0], next_player[1]):
            break

        if map[next_player[1]][next_player[0]] == '#':
            dir = turn_right(dir)
        else:
            player = next_player
            vis.add((next_player, dir))


print("ready")
print(obstructions)
