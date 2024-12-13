from lib import *

input = read_input(2024, 9).strip()
input = input.split("\n")

input = list(input[0])
fs = [None] * len(input) * 10
filesys = [None] * len(input)

index = 0
filesys_index = 0
ID = 0
block_size = {}


for i in range(len(input)):
    input[i] = int(input[i])
    if i % 2 == 0:
        # file
        if ID not in block_size.keys():
            block_size[ID] = [input[i]]
        else:
            block_size[ID].append(input[i])

        filesys[filesys_index] = (ID, input[i])
        for k in range(input[i]):
            fs[index] = ID
            # filesystem += str(ID)
            index += 1
        filesys_index += 1
        ID += 1
    else:
        # free
        filesys[filesys_index] = (-1, input[i])
        for k in range(input[i]):
            # filesystem += '.'
            fs[index] = -1
            index += 1
        filesys_index += 1

sum = 0
for i, e in enumerate(fs):
    if e is None:
        break
    if e == -1:
        last_element = fs.pop()
        while last_element == -1 or last_element is None:
            last_element = fs.pop()
        sum += last_element * i
    else:
        sum += i * e
print(sum)


# part 2
# (value, amount)
counter = 0
for i in range(len(filesys)):
    block = filesys[i]
    value = block[0]
    size = block[1]
    if value == -1:
        # space
        for j in range(len(filesys)-1, i, -1):
            whole_file = filesys[j]
            if whole_file[0] == -1:
                continue
            if j <= i:
                break
            if size > whole_file[1]:
                filesys[i] = whole_file
                filesys[j] = (-1, whole_file[1])
                filesys.insert(i+1, (-1, size-whole_file[1]))
                break
            elif size == whole_file[1]:
                filesys[i] = whole_file
                filesys[j] = block
                break
c = 0
sum = 0
for i in filesys:
    for j in range(i[1]):
        if i[0] == -1:
            c += 1
            continue
        sum += i[0] * c
        c += 1
print(sum)
