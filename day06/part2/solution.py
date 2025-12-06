import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def parse_worksheet_part2(input_string: str) -> list[tuple[list[int], str]]:

    lines = [line.rstrip("\n") for line in input_string.splitlines() if line.strip()]
    if not lines:
        return []


    width = max(len(line) for line in lines)
    grid = [list(line.ljust(width)) for line in lines]

    height = len(grid)
    last_row = height - 1 

    problems: list[tuple[list[int], str]] = []

    col = 0
    while col < width:

        if all(grid[row][col] == " " for row in range(height)):
            col += 1
            continue

        start = col
        while col < width and not all(grid[row][col] == " " for row in range(height)):
            col += 1
        end = col 

        op_symbol = None
        for c in range(start, end):
            ch = grid[last_row][c]
            if ch in OPS:
                op_symbol = ch
                break

        if op_symbol is None:
            raise ValueError(f"Kein Operator in Spalten {start}..{end-1} gefunden")

        ceph_nums: list[int] = []
        for c in range(end - 1, start - 1, -1):
            digits: list[str] = []
            for r in range(last_row):  
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                ceph_nums.append(int("".join(digits)))

        problems.append((ceph_nums, op_symbol))

    return problems


def solve_part2(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    problems = parse_worksheet_part2(content)

    grand_total = 0
    for ceph_nums, op_symbol in problems:
        op = OPS[op_symbol]
        total = ceph_nums[0]
        for n in ceph_nums[1:]:
            total = op(total, n)
        grand_total += total

    return grand_total


if __name__ == "__main__":
    print(solve_part2("input.txt"))
