import fileinput
from collections import Counter

grid = []
for line in fileinput.input():
    grid.append([c for c in line.strip()])
rows = len(grid)
cols = len(grid[0])
dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def adj(grid, r, c):
    cnt = Counter()
    for dr in dirs:
        if 0 <= r+dr[0] < rows and 0 <= c+dr[1] < cols:
            cnt[grid[r+dr[0]][c+dr[1]]] += 1
    return cnt


for step in range(0, 10):
    ngrid = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    for r in range(rows):
        for c in range(rows):
            val = grid[r][c]
            counts = adj(grid, r, c)
            if val == '.' and counts["|"] >= 3:
                ngrid[r][c] = '|'
            elif val == '|' and counts["#"] >= 3:
                ngrid[r][c] = '#'
            elif val == '#' and counts['#'] >= 1 and counts['|'] >= 1:
                ngrid[r][c] = '#'
    grid = ngrid
    for row in grid:
        print("".join(row))
    print("")
