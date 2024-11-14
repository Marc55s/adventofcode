from lib import *
import itertools

data = read_input(2019, 7 ,1).strip()
data = data.split(",")

data = [int(i) for i in data]

output = 0


def handle_operation(ID, op, instr, i, c=0, b=0, a=0) -> (int, bool):
    # print(f"op {op} (c,b,a)=({c},{b},{a}) instr[i]= {instr[i]} i={i} instr[i+1] ={instr[i+1]} instr[i+2] ={instr[i+2]}")

    global output
    if op == 1:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        instr[instr[i+3]] = x + y
        return (4, False)
    elif op == 2:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        instr[instr[i+3]] = x * y
        return (4, False)
    elif op == 3:
        if len(ID) == 0:
            z = output
        else:
            z = ID.pop(0)
        # print("in", z)
        instr[instr[i+1]] = z
        return (2, False)
    elif op == 4:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        print("out", x)
        output = x
        return (2, False)
    elif op == 5:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        if x != 0:
            return (y, True)
        else:
            return (3, False)
    elif op == 6:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        if x == 0:
            return (y, True)
        else:
            return (3, False)
    elif op == 7:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        if x < y:
            if a == 1:
                instr[i+3] = 1
            else:
                instr[instr[i+3]] = 1
        else:
            if a == 1:
                instr[i+3] = 0
            else:
                instr[instr[i+3]] = 0
        return (4, False)
    elif op == 8:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        y = instr[i+2] if b == 1 else instr[instr[i+2]]
        if x == y:
            if a == 1:
                instr[i+3] = 1
            else:
                instr[instr[i+3]] = 1
        else:
            if a == 1:
                instr[i+3] = 0
            else:
                instr[instr[i+3]] = 0
        return (4, False)
    elif op == 99:
        return (-1, False)
    else:
        print("crashed", op)
        exit()
        return (-1, False)


def exec_instr(ID, instr, instr_len, i) -> (int, bool):
    if instr_len == 1:
        op = int(str(instr[i])[0])
        return handle_operation(ID, op, instr, i)
    elif instr_len == 2:
        op = instr[i]
        return handle_operation(ID, op, instr, i, 0, 0, 0)
    elif instr_len == 3:
        mode_c = int(str(instr[i])[0])
        op = int(str(instr[i])[2])
        return handle_operation(ID, op, instr, i, mode_c, 0, 0)
    elif instr_len == 4:
        mode_b = int(str(instr[i])[0])
        mode_c = int(str(instr[i])[1])
        op = int(str(instr[i])[3])
        return handle_operation(ID, op, instr, i, mode_c, mode_b, 0)
    elif instr_len == 5:
        mode_a = int(str(instr[i])[0])
        mode_b = int(str(instr[i])[1])
        mode_c = int(str(instr[i])[2])
        op = int(str(instr[i])[4])
        return handle_operation(ID, op, instr, i, mode_c, mode_b, mode_a)


def determine(ID, instr) -> (int, bool):
    i = 0
    skip = 0
    while i < len(instr):
        instr_len = len(str(instr[i]))
        # print(f"while: i={i} instr[i]={instr[i]}")
        skip, jump = exec_instr(ID, instr, instr_len, i)

        if skip == -1:
            return output, False
        if skip is not None:
            i = i + skip
            if jump is True:
                i = skip
        else:
            print("nothing to do")
    return output, True


def calc(phase):
    start_value = 0
    out = [phase.pop(0), start_value]
    A = determine(out, data.copy())
    for i in phase:
        out = [i, A[0]]
        A = determine(out, data.copy())
    return A[0]


phase_settings = [0, 1, 2, 3, 4]


def highest_signal(phase_settings):
    combinations = list(itertools.permutations(phase_settings))
    max = 0
    for comb in combinations:
        val = calc(list(comb))
        if val > max:
            max = val
    return max


print(highest_signal(phase_settings))
print("-------------------------")

# Part 2


def calc_2(input):
    E = input
    out = [input]
    for i in range(5):
        A = determine(out, data.copy())
        out = [A[0]]
        if not A[1] and i < 4:
            return E, False
            break
    return A


def c(phase):
    start_value = 0
    out = [phase.pop(0), start_value]
    A = determine(out, data.copy())
    for i in phase:
        out = [i, A[0]]
        A = determine(out, data.copy())
    return A


phase_settings = [5, 6, 7, 8, 9]
combinations = list(itertools.permutations(phase_settings))

vals = []

for comb in combinations:
    comb = list(comb)


def cycle_phase(comb):
    e = c(comb)
    while True:
        print(e)
        e = calc_2(e[0])
        if not e[1]:
            vals.append(e[0])
            break


cycle_phase([9, 8, 7, 6, 5])
print(vals)
