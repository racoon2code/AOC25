import math
from collections import defaultdict


def distance(p1: list[int], p2: list[int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def read_positions(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding="utf-8") as f:
        positions = [list(map(int, line.strip().split(","))) for line in f if line.strip()]
    return positions


class DSU:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return 
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

    def component_sizes(self) -> list[int]:
        comp = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            comp[root] += 1
        return list(comp.values())


def solve(filename: str, num_connections: int) -> int:

    positions = read_positions(filename)
    n = len(positions)

    pairs: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(positions[i], positions[j])
            pairs.append((d, i, j))

    pairs.sort(key=lambda x: x[0])

    dsu = DSU(n)

    for k in range(min(num_connections, len(pairs))):
        _, i, j = pairs[k]
        dsu.union(i, j)

    sizes = dsu.component_sizes()
    sizes.sort(reverse=True)


    a, b, c = sizes[0], sizes[1], sizes[2]
    return a * b * c


if __name__ == "__main__":

    print("Beispiel (10 Verbindungen):", solve("input.txt", 10))

    print("Aufgabe (1000 Verbindungen):", solve("input.txt", 1000))
