from lib import *
import re

input = read_input(2024, 3).strip()
input = input.split("\n")

line = ""
for i in input:
    line += i
sum = 0
x = re.findall("mul[(](\\d{1,3})[,](\\d{1,3})[)]", line)
index = 0
for i in x:
    a, b = i
    sum = sum + (int(a) * int(b))

print("part 1=", sum)


sum = 0
regex = re.finditer("(mul[(](\\d{1,3})[,](\\d{1,3})[)])|(do[(][)])|(don't[(][)])", line)
state = True
for m in regex:
    m = m.group()
    if m == "don't()":
        state = False
    elif m == "do()":
        state = True
    else:
        if state:
            splitted = m.split(",")
            a = splitted[0][4::]
            b = splitted[1][:-1:]
            sum += int(a)*int(b)

print("part 2=",sum)

