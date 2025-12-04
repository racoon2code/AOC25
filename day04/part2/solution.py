def parse_grid(lines):
    return [list(line.strip()) for line in lines if line.strip()]

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def find_accessible_positions(grid):
    rows = len(grid)
    cols = len(grid[0])
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1

            if neighbors < 4:
                to_remove.append((r, c))

    return to_remove

def simulate_removal(grid):
    total_removed = 0

    while True:
        to_remove = find_accessible_positions(grid)
        if not to_remove:
            break  

        for r, c in to_remove:
            grid[r][c] = '.'  
        total_removed += len(to_remove)

    return total_removed


with open("input.txt", "r", encoding="utf-8") as f:
    grid = parse_grid(f)

result = simulate_removal(grid)
print(result)
