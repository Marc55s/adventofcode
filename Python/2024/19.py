from lib import *

puzzle_input = read_input(2024, 19).strip()
puzzle_input = puzzle_input.split("\n")

split_idx = puzzle_input.index("")
patterns = puzzle_input[0:split_idx]
patterns = patterns[0].split(", ")
designs = puzzle_input[split_idx+1:]


dic = {}
found = False


def dp(design, old):
    global found
    if found:
        return
    for i in patterns:
        cutted = design.removeprefix(i)
        if cutted == "":
            found = True
            print(old)
            if old not in dic:
                dic[old] = 1
            else:
                dic[old] += 1
            return True
        if cutted != design:
            dp(cutted, old)


ans = 0
for d in designs:
    found = False
    dp(d, d)
print(len(dic))
