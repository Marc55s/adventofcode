from lib import *

puzzle_input = read_input(2024, 25)
puzzle_input = puzzle_input.split("\n")

keys = []
locks = []

for i in range(0, len(puzzle_input)-8, 8):
    if "#####" in puzzle_input[i+1]:
        count = [0] * 5
        for k in range(5):
            for j in range(2, 8):
                if puzzle_input[i+j][k] == "#":
                    count[k] += 1
        locks.append(count)
        # lock

    elif "....." in puzzle_input[i+1]:
        count = [0] * 5
        for k in range(5):
            for j in range(1, 8-1):
                if puzzle_input[i+j][k] == "#":
                    count[k] += 1
        keys.append(count)
pair = 0
for lock in locks:
    for key in keys:
        # print("checking",lock,key)
        compatable = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                compatable = False
                break
        if compatable:
            pair += 1

print(pair)
