from lib import *
from collections import Counter

input = read_input(2024, 1).strip()

input = input.split("\n")


a = []
b = []

for i in input:
    split = i.split("   ")
    left = int(split[0])
    right = int(split[1])
    a.append(left)
    b.append(right)


z = a.copy()
w = b.copy()
z.sort()
w.sort()
distances = [abs(z[x]-w[x]) for x in range(len(a))]

similiarity = Counter(b)
score = [int(x) * (similiarity[x]) for x in a]

print(sum(distances))
print(sum(score))
