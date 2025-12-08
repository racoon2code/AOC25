import math
from collections import defaultdict


def distance(p1: list[int], p2: list[int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def read_positions(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding="utf-8") as f:
        return [list(map(int, line.strip().split(","))) for line in f if line.strip()]


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def component_sizes(self) -> list[int]:
        comp = defaultdict(int)
        for i in range(len(self.parent)):
            comp[self.find(i)] += 1
        return list(comp.values())


def solve(positions: list[list[int]]) -> int:
    n = len(positions)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((distance(positions[i], positions[j]), i, j))
    pairs.sort(key=lambda x: x[0])
    dsu = DSU(n)
    for d, i, j in pairs:
        if dsu.union(i, j):
            if dsu.components == 1:
                x1 = positions[i][0]
                x2 = positions[j][0]
                return x1 * x2
    return -1


if __name__ == "__main__":
    positions = read_positions("input.txt")
    print("Part 2:", solve(positions))
