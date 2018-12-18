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


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print("")


def run_step(grid):
    ngrid = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            counts = adj(grid, r, c)
            if val == '.' and counts["|"] >= 3:
                ngrid[r][c] = '|'
            elif val == '|' and counts["#"] >= 3:
                ngrid[r][c] = '#'
            elif val == '#' and counts['#'] >= 1 and counts['|'] >= 1:
                ngrid[r][c] = '#'
            elif val == '#':
                ngrid[r][c] = '.'
    return ngrid


def score(grid):
    wood = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == '|')
    lumber = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == '#')
    return wood * lumber


def hash(grid):
    return "".join("".join(row) for row in grid)


# Part 1
target = 1000000000
lastseen = dict()
cycle = None
step = 1
while True:
    grid = run_step(grid)

    h = hash(grid)
    if h not in lastseen:
        lastseen[h] = step
    else:
        cycle = step - lastseen[h]
        steps = (target - step) // cycle
        step += steps * cycle
        lastseen[h] = step

    if step == 10:
        print("Part 1:", score(grid))
    if step == target:
        print("Part 2:", score(grid))
        break

    step += 1
