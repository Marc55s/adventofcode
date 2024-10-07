from lib import *

data = read_input(2019, 5).strip()
data = data.split(",")

data = [int(i) for i in data]

def handle_operation(ID, op, instr, i, c=0, b=0, a=0) -> (int,bool):
    #print(f"op {op} (c,b,a)=({c},{b},{a}) instr[i]= {instr[i]} i={i} instr[i+1] ={instr[i+1]} instr[i+2] ={instr[i+2]}")
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
        instr[instr[i+1]] = ID
        return (2, False)
    elif op == 4:
        x = instr[i+1] if c == 1 else instr[instr[i+1]]
        print("out", x)
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


def determine(ID, instr) -> int:
    i = 0
    while i < len(instr):
        instr_len = len(str(instr[i]))
        #print(f"while: i={i} instr[i]={instr[i]}")
        skip, jump = exec_instr(ID, instr, instr_len, i)

        if skip == -1:
            break
        if skip is not None:
            i = i + skip
            if jump is True:
                i = skip
        else:
            print("nothing to do")

print(determine(1, data.copy()))
print(determine(5, data.copy()))
