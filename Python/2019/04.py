from lib import *

data = read_input(2019,4,0).strip()
data = data.split("-")

print(data)


def decrease(pw):
    for i in range(len(pw)-1):
        if pw[i] > pw[i+1]:
            return True

def double(pw):
    i = 0
    while i < len(pw)-1:
        if pw[i] == pw[i+1]:
            return True
        i+=1
    return False

def double_two(pw):
    i = 0
    while i < len(pw)-1:
        if pw[i] == pw[i+1]:
            if (i + 2 < len(pw) and pw[i] == pw[i + 2]):
                # Skip the whole sequence of identical digits
                while i + 1 < len(pw) and pw[i] == pw[i + 1]:
                    i += 1
            else:
                return True  # Found a valid double
        i+=1

    return False

valid = 0
valid_p2 = 0
for i in range(int(data[0]),int(data[1])):
    # is i valid?
    if " " in str(i):
        continue
    if not decrease(str(i)) and double(str(i)):
        valid += 1
    if not decrease(str(i)) and double_two(str(i)):
        valid_p2 += 1

print(valid)
print(valid_p2)
