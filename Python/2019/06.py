from lib import *

data = read_input(2019, 6).strip()
data = data.split("\n")


"""
BFS count the direct orbits:
for each node:
    if not in visited: # visited should be a set
            direct_orbits += neighbours
    depth++

"""


G = nx.Graph()
edges = []


for line in data:
    a, b = line.split(")")
    edges.append((a, b))

direct_orbits = 0

G.add_edges_from(edges)

"""
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
"""

indirect_orbits = 0


def dfs(node, visited, total_orbits, depth=0):
    visited.add(node)
    total_orbits[0] = total_orbits[0] + depth
    for n in G.neighbors(node):
        if n not in visited:
            dfs(n, visited, total_orbits, depth + 1)


total_orbits = [0]
v = set()
dfs("COM", v, total_orbits)

print(total_orbits[0])

z = nx.shortest_path_length(G, "YOU", "SAN")
print(z-2)
