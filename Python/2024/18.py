from lib import *
import networkx as nx

input = read_input(2024, 18).strip()
input = input.split("\n")

size = 71

memory = [["." for x in range(size)] for y in range(size)]


def display(w):
    for i in range(len(w)):
        for j in range(len(w[0])):
            print(w[i][j], end="")
        print()


def in_map(x, y):
    return 0 <= x < size and 0 <= y < size


c = 0
BYTE_LIMIT = 1024
for pos in input:
    x, y = pos.split(",")
    x = int(x)
    y = int(y)
    memory[y][x] = "#"
    c += 1
    if c < BYTE_LIMIT:
        continue
    try:
        G = nx.Graph()
        for x in range(size):
            for y in range(size):
                if memory[y][x] == ".":
                    G.add_node((x, y))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx_pos, ny = x + dx, y + dy
                        if 0 <= nx_pos < size and 0 <= ny < size and memory[ny][nx_pos] == ".":
                            G.add_edge((x, y), (nx_pos, ny))
        path = (nx.shortest_path_length(
            G, source=(0, 0), target=(size-1, size-1)))
        if c == BYTE_LIMIT:
            print(path)
    except Exception:
        print(f"The coordinates {pos} of the {c} byte blocks the path")
        break
