from lib import *

puzzle_input = read_input(2024, 21).strip()
puzzle_input = puzzle_input.split("\n")


keypad = {
    "A": (0, 0),
    "0": (-1, 0),
    "1": (-2, -1),
    "2": (-1, -1),
    "3": (0, -1),
    "4": (-2, -2),
    "5": (-1, -2),
    "6": (0, -2),
    "7": (-2, -3),
    "8": (-1, -3),
    "9": (0, -3)
}

dirpad = {
    "A": (0, 0),
    "^": (-1, 0),
    "v": (-1, -1),
    "<": (-2, -1),
    ">": (0, -1)
}


"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
directional:
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""


def pad(code):
    sequence = ""
    start = (0, 0)
    for digit in code:
        target = keypad[digit]
        x, y = target
        sx, sy = start

        # walk x till not possible then walk up or dow etc
        while (sx, sy) != target:
            while sx != x:
                if x < sx:
                    sequence += "<"
                    sx -= 1
                elif x > sx:
                    sequence += ">"
                    sx += 1
            while y != sy:
                if y < sy:
                    sy -= 1
                    sequence += "^"
                elif y > sy:
                    sy += 1
                    sequence += "v"
        sequence += "A"
        start = target
    return sequence


def directional_ctrl(code):
    sequence = ""
    start = (0, 0)
    for digit in code:
        target = dirpad[digit]
        x, y = target
        sx, sy = start
        while (sx, sy) != target:
            while x != sx:
                if ((sx, sy) not in dirpad.values()):
                    print("out of bounds")
                if x < sx and (sx, sy) == dirpad["^"]:
                    break
                if x < sx:
                    sequence += "<"
                    sx -= 1
                elif x > sx:
                    sequence += ">"
                    sx += 1
            while y != sy:
                if y < sy:
                    sy -= 1
                    sequence += "v"
                elif y > sy:
                    sy += 1
                    sequence += "^"
        sequence += "A"
        start = target
    return sequence


sum_compl = 0
for code in puzzle_input:
    numcode = pad(code)
    a = directional_ctrl(numcode)
    b = directional_ctrl(a)
    print(len(b), int(code[:-1]), code)
    sum_compl += len(b) * int(code[:-1])
print(sum_compl)
