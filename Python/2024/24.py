from lib import *
from itertools import combinations
import copy

puzzle_input = read_input(2024, 24).strip()
puzzle_input = puzzle_input.split("\n")

states_input = puzzle_input[:puzzle_input.index("")]

gates_input = puzzle_input[puzzle_input.index("")+1:]

states = {}


def set_states():
    global states
    states = {}
    for i in states_input:
        wire, state = i.split(": ")
        states[wire] = int(state)


def compute(wire):
    global states
    p1, op, p2, out = wire
    a = states[p1]
    b = states[p2]

    result = 0
    if op == "XOR":
        result = a ^ b
    elif op == "OR":
        result = a | b
    elif op == "AND":
        result = a & b
    states[out] = result


def parse_gates(gates_input):
    gates = []
    for gate in gates_input:
        f = gate.split(" ")
        p1 = f[0]
        op = f[1]
        p2 = f[2]
        output = f[-1]
        gates.append((p1, op, p2, output))
    return gates


def calculate_states(gates):
    global states
    c = 0
    length = len(gates)
    while gates:
        current = gates.pop(0)
        if len(gates) == length:
            c+=1
        else:
            c = 0
        if c == 1000:
            return False
        length = len(gates)
        p1, op, p2, out = current

        if p1 in states.keys() and p2 in states.keys():
            compute(current)
        else:
            gates.append(current)
    return True



def get_max():
    max = 0
    for i in range(0, 1000):
        a = "z"+str(i)
        if a in states.keys():
            max = i
    return max


set_states()
parsed_gates = parse_gates(gates_input)
calculate_states(parsed_gates)


def result(states):
    bits = []
    for i in range(get_max(), -1, -1):
        if i < 10:
            bits.append(states["z0"+str(i)])
        else:
            bits.append(states["z"+str(i)])
    bits = list(map(str, bits))
    ans = "".join(bits)
    return int(ans, 2)


print(result(states))
# part 2

x = []
y = []

for k, v in states.items():
    if "x" in k:
        x.append(v)
    if "y" in k:
        y.append(v)

x = list(map(str, x))
y = list(map(str, y))
x = "".join(x)[::-1]
y = "".join(y)[::-1]
sum = int(x, 2)+int(y, 2)  # get sum which should be the right output


normal_gates = parse_gates(gates_input)
