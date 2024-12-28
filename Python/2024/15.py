from lib import *
import copy

puzzle_input = read_input(2024, 15).strip()
puzzle_input = puzzle_input.split("\n")

split_idx = puzzle_input.index("")

warehouse = puzzle_input[0:split_idx]
warehouse = [list(x) for x in warehouse]

bigger_warehouse = puzzle_input[0:split_idx]
temp = []
for row in bigger_warehouse:
    row = row.replace("#", "##", -1)
    row = row.replace(".", "..", -1)
    row = row.replace("O", "[]", -1)
    row = row.replace("@", "@.", -1)
    temp.append(list(row))
bigger_warehouse = temp

moves = puzzle_input[split_idx + 1:]
moves = "".join(moves)

flip_brackets = {"]": "[", "[": "]"}

robot = [(i.index("@"), idx) for idx, i in enumerate(warehouse) if "@" in i][0]


def display(w):
    for i in range(len(w)):
        for j in range(len(w[0])):
            print(w[i][j], end="")
        print()


def is_dot(pos, w):
    x, y = pos
    return w[y][x] == "."


def is_wall(pos, w):
    x, y = pos
    return w[y][x] == "#"


def step(pos, move):
    x, y = pos
    if move == "^":
        y -= 1
    elif move == "v":
        y += 1
    elif move == "<":
        x -= 1
    elif move == ">":
        x += 1
    return (x, y)


for dir in moves:
    search = robot
    pushable = True
    while not is_dot(search, warehouse):
        if is_wall(search, warehouse):
            pushable = False
            break
        search = step(search, dir)
    if pushable:
        x, y = search
        warehouse[y][x] = "O"
        x, y = robot
        warehouse[y][x] = "."
        robot = step(robot, dir)
        x, y = robot
        warehouse[y][x] = "@"
    # print("Move",dir)
    # display()


def get_sum_of_GPS_coords(map):
    sum_gps_coords = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O" or map[i][j] == "[":
                sum_gps_coords += 100 * i + j
    return sum_gps_coords


print(get_sum_of_GPS_coords(warehouse))

# Part 2
robot = [(i.index("@"), idx)
         for idx, i in enumerate(bigger_warehouse) if "@" in i][0]
wh = copy.deepcopy(bigger_warehouse)
display(wh)
for move in moves:
    # print("move", move)
    # display(wh)
    next_step = step(robot, move)
    # z = input()

    if is_wall(next_step, wh):
        continue
    if is_dot(next_step, wh):  # basic movement
        x, y = robot
        wh[y][x] = "."
        robot = next_step
        x, y = robot
        wh[y][x] = "@"
    else:
        if move == "<" or move == ">":
            start = next_step
            find = next_step
            switchable = True
            while not is_dot(find, wh):
                if is_wall(find, wh):
                    switchable = False
                    break
                find = step(find, move)
            if switchable:
                # flip
                x, y = find
                BX, BY = step(start, move)
                starting_bracket = wh[BY][BX]
                wh[y][x] = flip_brackets[starting_bracket]

                # move robot
                x, y = robot
                wh[y][x] = "."
                robot = step(robot, move)
                x, y = robot
                wh[y][x] = "@"

                # flip every bracket in between
                flipper = robot
                while not is_dot(flipper, wh):
                    flipper = step(flipper, move)
                    if flipper == step(find, move) or is_dot(flipper, wh) or is_wall(flipper, wh):
                        break
                    x, y = flipper
                    wh[y][x] = flip_brackets[wh[y][x]]
        else:
            # up and down movement
            x, y = next_step
            walker = []
            walker.append((x, y))
            collision_zone = []
            boxes = []
            if wh[y][x] == "]":
                walker.append((x-1, y))
            else:
                walker.append((x+1, y))

            boxes.extend(walker)

            moveable = True
            while walker:
                explore = walker.pop(0)
                x, y = explore
                if move == "^":
                    y -= 1
                else:
                    y += 1
                if 0 > y or y >= len(wh):
                    moveable = False
                    break
                if wh[y][x] == "]":
                    walker.append((x-1, y))
                    walker.append((x, y))
                    boxes.append((x-1, y))
                    boxes.append((x, y))
                elif wh[y][x] == "[":
                    walker.append((x+1, y))
                    walker.append((x, y))
                    boxes.append((x+1, y))
                    boxes.append((x, y))
                else:
                    collision_zone.append((x, y))
                    continue

            for i in collision_zone:
                x, y = i
                if wh[y][x] == "#":
                    moveable = False
                    break
            if moveable:
                vis = set()
                for i in range(len(boxes)-1, -1, -1):
                    if boxes[i] in vis:
                        continue
                    vis.add(boxes[i])
                    x, y = boxes[i]
                    if move == "^":
                        wh[y-1][x] = wh[y][x]
                    elif move == "v":
                        wh[y+1][x] = wh[y][x]
                    wh[y][x] = "."
                x, y = robot
                wh[y][x] = "."
                robot = next_step
                x, y = robot
                wh[y][x] = "@"
print(get_sum_of_GPS_coords(wh))
