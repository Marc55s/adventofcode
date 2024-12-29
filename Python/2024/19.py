from lib import *

puzzle_input = read_input(2024, 19).strip()
puzzle_input = puzzle_input.split("\n")

split_idx = puzzle_input.index("")
patterns = puzzle_input[0:split_idx]
patterns = patterns[0].split(", ")
designs = puzzle_input[split_idx+1:]


dic = {}
found = False


def dp(design):
    # Done
    if design == "":
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            cutted = design[len(pattern):]
            if dp(cutted):
                return True

    return False


ans = 0
for d in designs:
    if dp(d):
        ans += 1
print(ans)


def dp2(design):
    # recall
    if design in memo:
        return memo[design]

    # Done
    if design == "":
        return 1

    count = 0
    # calculate all ways
    for pattern in patterns:
        if design.startswith(pattern):
            cutted = design[len(pattern):]
            count += dp2(cutted)

    # memoize and return result
    memo[design] = count
    return count


memo = {}
total_ways = 0

for design in designs:
    total_ways += dp2(design)

print(total_ways)
