from lib import *
from collections import Counter

input = read_input(2024, 1).strip()
input = input.split("\n")

left = []
right = []

for i in input:
    split = i.split("   ")
    left_id = int(split[0])
    right_id = int(split[1])
    left.append(left_id)
    right.append(right_id)


distances = [abs(left[x]-right[x]) for x in range(len(left))]

similiarity = Counter(right)
score = [int(x) * (similiarity[x]) for x in left]

print(sum(distances))
print(sum(score))
