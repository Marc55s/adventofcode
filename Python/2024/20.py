from lib import *

puzzle_input = read_input(2024, 20).strip()
puzzle_input = puzzle_input.split("\n")

track = [list(x) for x in puzzle_input]

start = 0
for y_i in range(len(puzzle_input)):
    for x_i in range(len(puzzle_input[0])):
        if track[y_i][x_i] == "S":
            start = (x_i, y_i)


def in_map(x, y):
    return 0 <= x < len(track[0]) and 0 <= y < len(track)


def cheat(vis, pos, time, part):
    x, y = pos
    saved_time = []
    if part == 1:
        for dx, dy in [(2, 0), (-2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if in_map(nx, ny) and track[ny][nx] != "#" and (nx, ny) not in vis:
                saved_time.append(time[(nx, ny)] - time[(x, y)] - 2)  # subtracting the time while cheating
    else:
        for y_skip in range(-21, 21):
            for x_skip in range(-21, 21):
                if abs(y_skip) + abs(x_skip) > 20:
                    continue
                nx, ny = x + x_skip, y + y_skip
                if in_map(nx, ny) and track[ny][nx] != "#" and (nx, ny) not in vis:
                    saved_time.append(time[(nx, ny)] - time[(x, y)] - (
                                abs(y_skip) + abs(x_skip)))  # subtracting the time while cheating
    return saved_time


def race(start, vis, path, position_to_time):
    picoseconds = 0
    q = [start]
    vis.add(start)
    while q:
        current = q.pop(0)
        path.append(current)
        x, y = current
        position_to_time[(x, y)] = picoseconds
        if track[y][x] == "E":
            break
        picoseconds += 1
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if in_map(nx, ny) and track[ny][nx] != "#" and (nx, ny) not in vis:
                vis.add((nx, ny))
                q.append((nx, ny))
    return picoseconds


path = []
position_to_time = {}
race(start, set(), path, position_to_time)


def amount_of_cheats(race_path, part=1):
    cheated_sec_to_amount = {}
    for i, pos in enumerate(race_path):
        saved_time = cheat(set(list(race_path)[:i]), pos, position_to_time, part)
        if i % 100 == 0 or i == len(race_path) - 1:
            progress = 100 * (i + 1) // len(race_path)
            print("\rCalculating cheats {}%".format(progress), end="")
        for t in saved_time:
            if t in cheated_sec_to_amount:
                cheated_sec_to_amount[t] += 1
            else:
                cheated_sec_to_amount[t] = 1
    return cheated_sec_to_amount


def get_total(part=1):
    total_cheats = 0
    cheated_seconds_map = amount_of_cheats(path, part)
    sorted_cheats = sorted(cheated_seconds_map.keys())
    for x in sorted_cheats:
        # print(f"There are {cheated_seconds_map[x]} cheats that save {x} picoseconds")
        if x >= 100:
            total_cheats += cheated_seconds_map[x]
    print()
    return total_cheats


print("Total cheats(p1) =", get_total())
print("Total cheats(p2) =", get_total(2))