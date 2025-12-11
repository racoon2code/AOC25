def read_graph(filename: str) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(":")
            node = left.strip()
            targets = right.strip().split() if right.strip() else []
            graph[node] = targets
    return graph


def count_paths(node: str, graph: dict[str, list[str]], dac: str, fft: str, have_dac: bool, have_fft: bool, memo: dict[tuple[str, bool, bool], int]) -> int:
    if node == dac:
        have_dac = True
    if node == fft:
        have_fft = True
    if node == "out":
        if have_dac and have_fft:
            return 1
        return 0
    key = (node, have_dac, have_fft)
    if key in memo:
        return memo[key]
    total = 0
    for nxt in graph.get(node, []):
        total += count_paths(nxt, graph, dac, fft, have_dac, have_fft, memo)
    memo[key] = total
    return total


def solve(input_data: str) -> int:
    graph = read_graph(input_data)
    memo: dict[tuple[str, bool, bool], int] = {}
    return count_paths("svr", graph, "dac", "fft", False, False, memo)


if __name__ == "__main__":

    print(solve("input.txt"))
