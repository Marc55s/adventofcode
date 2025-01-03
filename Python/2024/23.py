from lib import *
import networkx as nx

puzzle_input = read_input(2024, 23)
puzzle_input = puzzle_input.split("\n")

con = {}
G = nx.Graph()
for connection in puzzle_input:
    con1, con2 = connection.split("-")
    G.add_node(con1)
    G.add_node(con2)
    G.add_edge(con1,con2)
    G.add_edge(con2,con1)

    if con1 in con:
        con[con1].append(con2)
    else:
        con[con1] = [con2]
    if con2 in con:
        con[con2].append(con1)
    else:
        con[con2] = [con1]
sum = 0
inter = []
for k, v in con.items():
    for i in v:
        for z in con[i]:
            if z in v:
                inter.append(tuple(list(set(sorted([k,i,z])))))
inter = list(set(inter))

m = [0]
k = ""
for a,b,c in inter:
    if "t" in a[0] or "t" in b[0] or "t" in c[0]:
        sum += 1
print(sum)

m = [0]
for c in nx.find_cliques(G):
    if len(c) > len(m):
        m = c
print(",".join(sorted(m)))
