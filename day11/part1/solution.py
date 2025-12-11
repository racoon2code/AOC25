def read_graph(filename: str) -> dict[str, list[str]]:
    graph = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, targets = line.split(":")
            name = name.strip()
            if targets.strip():
                graph[name] = targets.strip().split()
            else:
                graph[name] = []
    return graph


def count_paths(node: str, graph: dict[str, list[str]], memo: dict[str, int]) -> int:
    if node == "out":
        return 1
    if node in memo:
        return memo[node]
    total = 0
    for nxt in graph.get(node, []):
        total += count_paths(nxt, graph, memo)
    memo[node] = total
    return total


def solve(input_data: str) -> int:
    graph = read_graph(input_data)
    memo: dict[str, int] = {}
    return count_paths("you", graph, memo)


if __name__ == "__main__":
    print(solve("input.txt"))
