import re


def parse_line(line: str) -> tuple[str, list[list[int]]]:
    line = line.strip()
    s = line.index("[")
    e = line.index("]", s)
    pattern = line[s + 1 : e]
    button_parts = re.findall(r"\(([^)]*)\)", line)
    buttons: list[list[int]] = []
    for part in button_parts:
        part = part.strip()
        if part == "":
            buttons.append([])
        else:
            buttons.append(list(map(int, part.split(","))))
    return pattern, buttons


def solve_machine(pattern: str, buttons: list[list[int]]) -> int:
    n = len(pattern)
    m = len(buttons)
    if m == 0:
        if "#" in pattern:
            raise ValueError("No solution")
        return 0
    rows: list[int] = []
    rhs: list[int] = []
    for i in range(n):
        rowmask = 0
        for j, btn in enumerate(buttons):
            if i in btn:
                rowmask |= 1 << j
        rows.append(rowmask)
        rhs.append(1 if pattern[i] == "#" else 0)
    r = len(rows)
    pivots: dict[int, int] = {}
    row = 0
    for col in range(m):
        pivot_row = None
        for i in range(row, r):
            if (rows[i] >> col) & 1:
                pivot_row = i
                break
        if pivot_row is None:
            continue
        rows[row], rows[pivot_row] = rows[pivot_row], rows[row]
        rhs[row], rhs[pivot_row] = rhs[pivot_row], rhs[row]
        pivots[col] = row
        for i in range(r):
            if i != row and (rows[i] >> col) & 1:
                rows[i] ^= rows[row]
                rhs[i] ^= rhs[row]
        row += 1
    for i in range(r):
        if rows[i] == 0 and rhs[i] == 1:
            raise ValueError("No solution")
    free_cols = [c for c in range(m) if c not in pivots]
    x0 = 0
    for c, rrow in pivots.items():
        if rhs[rrow]:
            x0 |= 1 << c
    basis: list[int] = []
    for fc in free_cols:
        sol = 0
        sol |= 1 << fc
        for c, rrow in pivots.items():
            s = rhs[rrow]
            if (rows[rrow] >> fc) & 1:
                s ^= 1
            if s:
                sol |= 1 << c
        v = sol ^ x0
        basis.append(v)
    k = len(basis)
    best = m + 1
    for mask in range(1 << k):
        x = x0
        mm = mask
        idx = 0
        while mm:
            if mm & 1:
                x ^= basis[idx]
            mm >>= 1
            idx += 1
        wt = x.bit_count()
        if wt < best:
            best = wt
    return best


def solve(input_data: str) -> int:
    total = 0
    with open(input_data, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pattern, buttons = parse_line(line)
            total += solve_machine(pattern, buttons)
    return total


if __name__ == "__main__":
    print(solve("input.txt"))
