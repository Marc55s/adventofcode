from time import sleep

from lib import *

w = 101
h = 103

puzzle_input = read_input(2024, 14).strip()
puzzle_input = puzzle_input.split("\n")

first = 0
sec = 0
third = 0
fourth = 0


def in_quadrant(x, y, vx, vy, seconds):
    global first, sec, third, fourth
    robots = []
    for i in range(seconds):
        x += vx
        y += vy
        if x >= w:
            x %= w
        elif x < 0:
            x = w + x

        if y >= h:
            y %= h
        elif y < 0:
            y = h + y
        robots.append((x, y))
    if x == w // 2 or y == h // 2:
        return robots

    if x > w // 2:
        if y > h // 2:
            fourth += 1
        else:
            sec += 1
    else:
        if y > h // 2:
            third += 1
        else:
            first += 1
    return robots


def display(robots):
    for i in range(h):
        for k in range(w):
            if (k, i) in robots:
                print("#", end="")
            else:
                print(".", end="")
        print()


def build_rows(robots_positions):
    res = [["." for x in range(w)] for z in range(h)]
    for pos in robots_positions:
        x, y = pos
        res[y][x] = "#"
    return res


for second in range(10000):
    if second % 100 == 0:
        print(second)
    r = []
    for i in puzzle_input:
        p, v = i.split(" ")
        p = p.split(",")
        px = p[0][2:]
        py = p[1]
        v = v.split(",")
        vx = v[0][2:]
        vy = v[1]
        px = int(px)
        py = int(py)
        vx = int(vx)
        vy = int(vy)
        result = in_quadrant(px, py, vx, vy, second)
        for z in result:
            r.append(z)
    rows = build_rows(r)
    for row in rows:
        if "#######" in row:
            print(second)
            break

print(first, sec, third, fourth)
print(first * sec * third * fourth)
bots = []
for i in puzzle_input:
    p, v = i.split(" ")
    p = p.split(",")
    px = p[0][2:]
    py = p[1]
    v = v.split(",")
    vx = v[0][2:]
    vy = v[1]
    px = int(px)
    py = int(py)
    vx = int(vx)
    vy = int(vy)
    bots.append((px, py, vx, vy))

def update_bots(bots):
    updated = []
    for bot in bots:
        x, y, vx, vy = bot
        x += vx
        y += vy
        if x >= w:
            x %= w
        elif x < 0:
            x = w + x
        if y >= h:
            y %= h
        elif y < 0:
            y = h + y
        updated.append((x,y,vx,vy))
    return updated

