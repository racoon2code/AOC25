
def calculate_rectangle(p1: list[int], p2: list[int]) -> int:
    a = p1[0] - p2[0] + 1
    b = p1[1] - p2[1] + 1
    return a * b


def read_positions(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding="utf-8") as f:
        positions = [list(map(int, line.strip().split(","))) for line in f if line.strip()]
    return positions


def solve(input_data: str) -> int:

    positions = read_positions(input_data)
    total_area = 0
    n = len(positions)

    for i in range(n):
        for j in range(i + 1, n):
            area = calculate_rectangle(positions[i], positions[j])
            
            if area > total_area:
                total_area = area

    return total_area


if __name__ == "__main__":

    print(solve("input.txt"))


