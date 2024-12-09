from lib import *

input = read_input(2024, 9,1).strip()
input = input.split("\n")

filesystem =""

input = list(input[0])
ID = 0
fs = [None] * len(input) ** 2

index = 0
frees = []

for i in range(len(input)):
    input[i] = int(input[i])
    if i % 2 == 0:
        # file
        for k in range(input[i]):
            fs[index] = ID
            filesystem += str(ID)
            index += 1
        ID += 1
    else:
        # free
        for k in range(input[i]):
            filesystem += '.'
            fs[index] = -1
            index += 1

print("ready for checksum eval",len(fs))
# compress
for i in range(index,0,-1):
    if type(fs[i]) is int:
        if fs[i] == -1:
            continue
        else:
            for k in range(len(fs)):
                if fs[k] == -1:
                    fs[k] = fs[i]
                    fs.pop(i)
                    break
                if fs[k] is None:
                    break

sum = 0
print(len(fs))
for i in range(len(fs)):
    if fs[i] is None:
        break
    if type(fs[i]) is int:
        sum += i * int(fs[i])

print(sum)
