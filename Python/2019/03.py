from lib import *

data = read_input(2019,3,0).strip()
data = data.split("\n");

x = 0
y = 0
index = 0

# set of points
points_one =  set()
points_two =  set()
intersections = set()

line_one = []
line_two = []
dist_one = []
dist_two = []


def in_between(dist, dir):
    global x,y,index
    for v in range(1,dist+1):
        x += dir[0]
        y += dir[1]
        if index == 0:
            points_one.add((x ,y))
            line_one.append((x,y))
        elif index == 1:
            points_two.add((x ,y))
            line_two.append((x,y))


# run instructions
line = [s.split(",") for s in data]
for idx,splitted in enumerate(line):
    x = 0
    y = 0
    index = idx
    for i in splitted:
        dir = i[0]
        dist = int(i[1::])
        if dir == "U":
            in_between(dist, (0,1))
        elif dir == "D":
            in_between(dist, (0,-1))
        elif dir == "L":
            in_between(dist, (-1,0))
        elif dir == "R":
            in_between(dist, (1,0))

# get nearest intersection
min = float('inf')
intersections = points_one.intersection(points_two)
for i in intersections:
    man_dist = abs(i[0]) + abs(i[1])
    if min > man_dist:
        min = man_dist


print(min)

#part 2
def distance(line, inter):
    d = 0
    last = (0,0)
    for i in line:
        if i == inter:
            return d + 1
        d += 1

distances = []
for i in intersections:
    d1 = distance(line_one,i)
    d2 = distance(line_two,i)
    distances.append(d1 + d2)

distances.sort()
print(distances[0])
