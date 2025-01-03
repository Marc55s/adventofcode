from lib import *

puzzle_input = read_input(2024, 17)
puzzle_input = puzzle_input.split("\n")

A = int(puzzle_input[0].split(": ")[1])
B = int(puzzle_input[1].split(": ")[1])
C = int(puzzle_input[2].split(": ")[1])
program = list(map(int, (puzzle_input[4].split(": ")[1].split(","))))

# evaluate program


def adv(A, c):
    return A // 2 ** c


def bxl(B, c):
    return B ^ c


def bst(c):
    return c % 8


def bxc(B, C):
    return B ^ C


def run_program(A, B, C, program):
    instruction_p = 0
    output = []
    # print("running with",A, B, C, program)
    while instruction_p < len(program)-1:
        combo_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: None}

        opcode = program[instruction_p]
        operand = program[instruction_p+1]
        combo = combo_map[operand]

        # print(f"ptr={instruction_p}, code={opcode}, operand={operand}, combo={combo}",A,B,C)
        if opcode == 0:
            A = adv(A, combo)
        elif opcode == 1:
            B = bxl(B, operand)
        elif opcode == 2:
            B = bst(combo)
        elif opcode == 3:
            if int(A) != 0:
                # print("jump to", operand)
                instruction_p = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            # print(bst(combo))
            output.append(bst(combo))
        elif opcode == 6:
            B = adv(A, combo)
        elif opcode == 7:
            C = adv(A, combo)
        instruction_p += 2
    return output

print(",".join(map(str,run_program(A,B,C,program))))

output = []
new_A = 0
istart = 0
j = 1
while len(program) >= j >= 0:
    new_A <<= 3
    for i in range(istart,8):
        if program[-j:] == run_program(new_A + i,B,C,program):
            break
    else:
        j -= 1
        new_A >>= 3
        istart = new_A % 8 +1
        new_A >>= 3
        continue
    j += 1
    new_A += i
    istart = 0
print(new_A)

