from lib import *

input = read_input(2024, 7).strip()
input = input.split("\n")

ans = 0

def validate_eq(nums, index, op, calculation, tocheck):

    if tocheck == calculation and index == len(nums):
        return True
    if index == len(nums):
        return False

    if op == '+':
        calculation += nums[index]
    elif op == '*':
        calculation *= nums[index]
    elif op == '||':
        calculation = int(str(calculation) + str(nums[index]))

    return validate_eq(nums, index+1, '+', calculation, tocheck) or validate_eq(nums, index+1, '*', calculation, tocheck) or validate_eq(nums, index+1, '||', calculation, tocheck)


for i in input:
    check, nums = i.split(": ")
    check = int(check)
    nums = nums.split(" ")
    nums = [int(x) for x in nums]
    start = nums.pop(0)

    valid = validate_eq(nums, 0, '+', start,check) or validate_eq(nums, 0, '*', start, check) or validate_eq(nums, 0, '||', start, check)
    if valid:
        ans += check

print(ans)
