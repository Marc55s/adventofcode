from Python.lib.lib import read_input

puzzle_input = read_input(2024, 19).strip()
puzzle_input = puzzle_input.split("\n")

split_idx = puzzle_input.index("")
patterns = puzzle_input[0:split_idx]
designs = puzzle_input[split_idx+1:]


def dp(design, idx):

    if design[0:idx] in patterns:
        design = design[idx+1:]

