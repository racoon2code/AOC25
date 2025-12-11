import re
from typing import List, Tuple
from scipy.optimize import linprog


def parse_line(line: str) -> Tuple[List[List[int]], List[int]]:
    line = line.strip()
    button_parts = re.findall(r"\(([^)]*)\)", line)
    buttons: List[List[int]] = []
    for part in button_parts:
        part = part.strip()
        if part == "":
            buttons.append([])
        else:
            buttons.append(list(map(int, part.split(","))))
    m = re.search(r"\{([^}]*)\}", line)
    jolts = list(map(int, m.group(1).split(",")))
    return buttons, jolts


def solve_machine(buttons: List[List[int]], target: List[int]) -> int:
    n = len(target)
    m = len(buttons)
    if m == 0:
        if any(v != 0 for v in target):
            raise ValueError("No solution")
    A_eq: List[List[int]] = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(1 if i in buttons[j] else 0)
        A_eq.append(row)
    c = [1.0] * m
    bounds = [(0, None)] * m
    res = linprog(
        c,
        A_eq=A_eq,
        b_eq=target,
        bounds=bounds,
        integrality=[1] * m,
        method="highs",
    )
    if not res.success:
        raise ValueError("No solution")
    return int(round(res.fun))


def solve(input_data: str) -> int:
    total = 0
    with open(input_data, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buttons, target = parse_line(line)
            total += solve_machine(buttons, target)
    return total


if __name__ == "__main__":
    print(solve("input.txt"))
