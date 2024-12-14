from lib import *
from copy import deepcopy


input = read_input(2024, 13).strip()
input = input.split("\n")

sum = 0
sum2 = 0
for i in range(0,len(input),4):
    a = input[i].split(": ")[1].split(", ")
    x1 = a[0].replace("X+","")
    y1 = a[1].replace("Y+","")

    b = input[i+1].split(": ")[1].split(", ")
    x2 = b[0].replace("X+","")
    y2 = b[1].replace("Y+","")

    prize = input[i+2].split(": ")[1].split(", ")
    px = prize[0].replace("X=","")
    py = prize[1].replace("Y=","")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    px = int(px)
    py = int(py)

    # Part 2
    px += 10000000000000
    py += 10000000000000
    # end

    factor = 1 / ((x1 * y2) - (x2*y1))
    k = factor * y2 * px + factor * (-x2) * py
    l = factor * (-y1) * px + factor * x1 * py
    if  k < 0 or l < 0:
        continue
    print(k,l)
    k = round(k)
    l = round(l)
    if (k * x1 + l * x2) == px and (k * y1 + l * y2) == py:
        # valid
        k *= 3
        sum += k + l


print(sum)
