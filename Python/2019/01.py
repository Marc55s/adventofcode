from lib import *

input = read_input(2019,1,1).strip()
input = input.split("\n");

x = lambda x : (x//3)-2

def until_zero(arg):
    sum = 0
    start = arg
    while x(start) > 0:
        start = x(start)
        sum += start
    return sum 

print(sum([(int(i)//3) -2 for i in input]))

print(sum([until_zero(int(i)) for i in input]))

