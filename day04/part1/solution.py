
def parse_grid(lines):
    return [list(line.strip()) for line in lines if line.strip()]

def count_accessible(grid):
    rows = len(grid)
    cols = len(grid[0])
    accessible = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

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
                accessible += 1

    return accessible

with open("input.txt", "r", encoding="utf-8") as f:
   lines = f.readlines()

       

grid = parse_grid(lines)
print(count_accessible(grid))  
