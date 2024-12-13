from lib import *
from copy import deepcopy


input = read_input(2024, 11).strip()
input = input.split("\n")
input = input[0].split(" ")
# input = list(map(int,input))
input_copy = deepcopy(input)


def blink(input):
    temp = []
    for e in (input):
        if int(e) == 0:
            temp.append(1)
        elif len(str(e)) % 2 == 0:
            e = str(e)
            left = e[0:(len(str(e))//2)]
            right = e[(len(str(e))//2):]
            temp.append(int(left))
            temp.append(int(right))
        else:
            temp.append(int(e) * 2024)
    return temp


step = 25
for i in range(step):
    input = blink(input)

print(len(input))
print("-----")


def blink2(stones):
    temp = deepcopy(stones)
    for k, v in stones.items():
        if v == 0:
            continue
        if k == 0:
            temp[0] -= v
            if 1 in temp:
                temp[1] += v
            else:
                temp[1] = v
        elif len(str(k)) % 2 == 0:
            k = str(k)
            left = k[0:(len(str(k))//2)]
            right = k[(len(str(k))//2):]
            left = int(left)
            right = int(right)

            temp[int(k)] -= v
            if left not in temp.keys():
                temp[left] = v
            else:
                temp[left] += v

            if right not in temp.keys():
                temp[right] = v
            else:
                temp[right] += v
        else:
            calc = int(k) * 2024
            temp[int(k)] -= v
            if calc not in temp.keys():
                temp[calc] = v
            else:
                temp[calc] += v
    return temp


dic = {}
for i in input_copy:
    dic[int(i)] = 1
for i in range(75):
    dic = blink2(dic)


sum = 0
for i in dic.values():
    sum += i
print(sum)
