from lib import *

input = read_input(2024, 8).strip()
input = input.split("\n")


w = len(input[0])
h = len(input)
antennas = {}

for i in range(h):
    input[i] = list(input[i])
for i in range(h):
    for k in range(w):
        if input[i][k] != '.':
            if input[i][k] in antennas:
                antennas[input[i][k]].append((k, i))
            else:
                antennas[input[i][k]] = [(k, i)]


def in_map(x, y):
    return y >= 0 and y < h and x >= 0 and x < w


# calculate antinodes
antinode = 0


def calculate_antinode(mode, vis):
    for antenna in antennas:
        positions = antennas[antenna]
        for i in range(len(positions)):
            start = positions[i]
            for k in range(i+1, len(positions)):
                to = positions[k]

                x1, y1 = start
                x2, y2 = to

                vx = x2 - x1
                vy = y2 - y1

                if mode == 0:
                    x2 += vx
                    y2 += vy

                    x1 -= vx
                    y1 -= vy
                    if in_map(x2, y2):
                        if (input[y2][x2] == '.' or input[y2][x2] == '#'):
                            input[y2][x2] = '#'
                        vis.add((x2, y2))
                    if in_map(x1, y1):
                        if (input[y1][x1] == '.' or input[y1][x1] == '#'):
                            input[y1][x1] = '#'
                        vis.add((x1, y1))
                else:
                    while in_map(x2, y2):
                        vis.add((x2, y2))
                        if (input[y2][x2] == '.' or input[y2][x2] == '#'):
                            input[y2][x2] = '#'
                        x2 += vx
                        y2 += vy
                    while in_map(x1, y1):
                        if (input[y1][x1] == '.' or input[y1][x1] == '#'):
                            input[y1][x1] = '#'
                        vis.add((x1, y1))
                        x1 -= vx
                        y1 -= vy
    return vis


print(len(calculate_antinode(0, set())))
print(len(calculate_antinode(1, set())))
