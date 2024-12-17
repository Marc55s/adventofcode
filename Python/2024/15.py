from lib import *

puzzle_input = read_input(2024, 15).strip()
puzzle_input = puzzle_input.split("\n")

split_idx = puzzle_input.index("")

warehouse = puzzle_input[0:split_idx]
warehouse = [list(x) for x in warehouse]

bigger_warehouse = puzzle_input[0:split_idx]
temp = []
for row in bigger_warehouse:
    row = row.replace("#","##",-1)
    row = row.replace(".","..",-1)
    row = row.replace("O","[]",-1)
    row = row.replace("@","@.",-1)
    temp.append(list(row))
bigger_warehouse = temp

moves = puzzle_input[split_idx + 1:]
moves = "".join(moves)

flip_brackets = {"]": "[", "[": "]"}

robot = [(i.index("@"), idx) for idx, i in enumerate(warehouse) if "@" in i][0]

print(robot)

def display(w):
    for i in range(len(w)):
        for j in range(len(w[0])):
            print(w[i][j], end="")
        print()

def is_free(pos,w):
    x, y = pos
    return w[y][x] == "."


def is_wall(pos,w):
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
    if is_free(robot,warehouse):
        x,y = robot
        warehouse[y][x] = "."
        robot = step(robot, dir)
        x,y = robot
        warehouse[y][x] = "@"
    else:
        search = robot
        pushable = True
        while not is_free(search,warehouse):
            if is_wall(search,warehouse):
                pushable = False
                break
            search = step(search, dir)
        if pushable:
            x, y = search
            warehouse[y][x] = "O"
            x,y = robot
            warehouse[y][x] = "."
            robot = step(robot,dir)
            x,y = robot
            warehouse[y][x] = "@"
    # print("Move",dir)
    # display()

def get_sum_of_GPS_coords(map):
    sum_gps_coords = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                sum_gps_coords += 100 * i + j
    return sum_gps_coords
print(get_sum_of_GPS_coords(warehouse))

print("-"*200)
# Part 2
print("start part 2")
robot = [(i.index("@"),idx) for idx, i in enumerate(bigger_warehouse) if "@" in i][0]
display(bigger_warehouse)

for dir in moves:
    print("Move",dir)
    display(bigger_warehouse)
    next = step(robot,dir)
    if is_free(next,bigger_warehouse):
        x,y = robot
        bigger_warehouse[y][x] = "."
        robot = next
        x,y = robot
        bigger_warehouse[y][x] = "@"
        continue
    if dir == "<" or dir == ">":
        # row
        start = robot
        search = robot
        pushable = True
        while not is_free(search,bigger_warehouse):
            if is_wall(search,bigger_warehouse):
                pushable = False
                break
            search = step(search, dir)

        if pushable:
            x, y = search
            start = step(start,dir)
            BX, BY = step(start,dir)
            next_bracket = bigger_warehouse[BY][BX]
            bigger_warehouse[y][x] = flip_brackets[next_bracket] # set free spot to flipped bracket

            x,y = robot
            bigger_warehouse[y][x] = "."
            robot = step(robot,dir)
            x,y = robot

            bigger_warehouse[y][x] = "@"
            flipper = robot
            while not is_free(flipper,bigger_warehouse):
                flipper = step(flipper, dir)
                if is_free(flipper,bigger_warehouse):
                    break
                BX, BY = flipper
                bigger_warehouse[BY][BX] = flip_brackets[bigger_warehouse[BY][BX]] # flip every bracket
    else:
        x,y = next
        """
        While stuff:
            current = dequeue.next
            look above for all currents
        """
        if next == "[":

        elif next == "]":

        pass
