from typing import Tuple, List
from shapely.geometry import Polygon


def read_positions(filename: str) -> List[Tuple[int, int]]:
    with open(filename, "r", encoding="utf-8") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]


def solve(filename: str) -> int:
    red: List[Tuple[int, int]] = read_positions(filename)
    if not red:
        return 0

    region: Polygon = Polygon(red)
    n: int = len(red)
    best: int = 0

    for i in range(n):
        x1, y1 = red[i]
        for j in range(i + 1, n):
            x2, y2 = red[j]
            if x1 == x2 or y1 == y2:
                continue
            xmin, xmax = (x1, x2) if x1 < x2 else (x2, x1)
            ymin, ymax = (y1, y2) if y1 < y2 else (y2, y1)
            rect: Polygon = Polygon(
                [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
            )
            if region.covers(rect):
                area: int = (xmax - xmin + 1) * (ymax - ymin + 1)
                if area > best:
                    best = area

    return best


if __name__ == "__main__":
    print(solve("input.txt"))
