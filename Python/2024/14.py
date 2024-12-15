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

def in_quadrant(x, y):
    global first, sec, third, fourth
    if x == w // 2 or y == h // 2:
        return
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

def display(robots):
    temp = []
    for z in robots:
        a,b,c,d = z
        temp.append((a,b))
    for i in range(h):
        for k in range(w):
            if (k, i) in temp:
                print("#", end="")
            else:
                print(".", end="")
        print()


def build_rows(robots_positions):
    res = [["." for x in range(w)] for z in range(h)]
    for pos in robots_positions:
        x,y,vx,vy = pos
        res[y][x] = "#"
    return res


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

def check_easter_egg(bots):
    rows =  build_rows(bots)
    for row in rows:
        if "########" in "".join(row):
            return True
    return False



for seconds in range(100000):
    if seconds % 100 == 0:
        print(seconds)
    bots = update_bots(bots)
    if check_easter_egg(bots):
        display(bots)
        print("Easter egg found at:",seconds+1) # seconds start at 1
        break


for bot in bots:
    x,y,vx,vy = bot
    in_quadrant(x,y)
print(first*sec*third*fourth)
