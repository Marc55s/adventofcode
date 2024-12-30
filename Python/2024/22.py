from lib import *

puzzle_input = read_input(2024, 22).strip()
puzzle_input = puzzle_input.split("\n")


def mix(sn, value):
    return sn ^ value


def prune(num):
    return num % 16777216


def evolve(sn):
    calc = sn * 64
    sn = prune(mix(sn, calc))
    calc = int(sn / 32)
    sn = prune(mix(sn, calc))
    calc = sn * 2048
    sn = prune(mix(sn, calc))
    return sn


sum = 0

for secret_number in puzzle_input:
    result = 0
    start = secret_number
    secret_number = int(secret_number)
    for i in range(2000):
        secret_number = evolve(secret_number)
        result = secret_number
    sum += result

print(sum)


# part 2
"""
secret number calculation last digit is the price
3 (from 123)
0 (from 15887950) -3
6 (from 16495136)  6
four consecutive changes are important

-2,1,-1,3 magic most rewarding sequence
the get the number (not change) of the last change and add to banana_count
"""

dic = {}

for secret_number in puzzle_input:
    secret_number = int(secret_number)
    prices = []
    changes = []
    start = secret_number

    prices.append(str(secret_number)[-1])
    for i in range(2000):
        secret_number = int(secret_number)
        secret_number = evolve(secret_number)
        prices.append(str(secret_number)[-1])

    first = prices.pop(0)
    for price in prices:
        change = int(price) - int(first)
        changes.append(change)
        first = price

    vis = set()
    for i in range(0, len(changes)-3):
        sub = changes[i:i+4]
        sub = tuple(sub)
        if sub in vis:
            continue
        vis.add(sub)
        if sub not in dic.keys():
            dic[sub] = int(prices[i+3])
        else:
            dic[sub] += int(prices[i+3])


print(max(dic.values()))
