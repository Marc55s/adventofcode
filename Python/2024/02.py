from lib import *
from collections import Counter

input = read_input(2024, 2).strip()
input = input.split("\n")


def check(levels):
    nums = levels
    inc = True
    dec = True
    diff_range = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False

        diff = abs(nums[i]-nums[i+1])
        if diff > 3 or diff < 1:
            diff_range = False
            break
    return diff_range and (dec ^ inc)


ans = 0

for i in input:
    numsx = (i.split(" "))
    nums = [int(x) for x in numsx]
    if check(nums):
        ans = ans + 1
    else:
        for k in range(len(nums)):
            smaller = nums.copy()
            del smaller[k]
            if check(smaller):
                ans = ans + 1
                break
print(ans)
