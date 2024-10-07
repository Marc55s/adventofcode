from lib import *

data = read_input(2019,2).strip()
data = data.split(",");

data[1] = 12
data[2] = 2

data = [int(i) for i in data]

def determine(addr) -> int:
    for i in range(0,len(addr),4):
        x = addr[i]
        if x == 1:
            sum = addr[addr[i+1]] + addr[addr[i+2]]
            addr[addr[i+3]] = sum
        elif x == 2:
            sum = addr[addr[i+1]] * addr[addr[i+2]]
            addr[addr[i+3]] = sum
        elif x == 99:
            break
        else:
            print("crashed", x)
            break

    return addr[0]




print(determine(data.copy()))

goal = 19690720
for i in range(99):
    for j in range(99):
        stuff = data.copy()
        stuff[1] = i
        stuff[2] = j
        if determine(stuff) == goal:
            print(100 * i+j)
            break


