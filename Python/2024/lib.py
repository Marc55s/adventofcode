from pathlib import Path

def read_input(year, day, example = 0) -> str:
    if example == 0:
        f = Path(__file__).parent / f"../{year}/puzzles/{day}"
    else:
        f = Path(__file__).parent / f"../../examples/{year}/{day}/{example}"
    f = f.resolve()
    return f.read_text()

