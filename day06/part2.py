from collections import namedtuple, deque, defaultdict

Point = namedtuple("Point", "id row col")

max_row, max_col = 0, 0
points = []
for i, line in enumerate(open('test.txt', 'r')):
    col, row = map(int, map(str.strip, line.strip().split(",")))
    max_row = max(max_row, row)
    max_col = max(max_col, col)
    points.append(Point(i, row, col))

grid = [[0 for c in range(max_col + 1)] for r in range(max_row + 1)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque((0, p) for p in points)
seen = defaultdict(set)
while len(q) > 0:
    steps, p = q.popleft()
    grid[p.row][p.col] += steps
    for d in dirs:
        np = Point(p.id, p.row+d[0], p.col+d[1])
        if 0 <= np.row < len(grid) and 0 <= np.col < len(grid[0]):
            if np not in seen[p.id]:
                q.append((steps + 1, np))
            seen[p.id].add(np)

count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        steps = grid[r][c]
        count += 1 if steps < 10000 else 0
        if steps < 10000:
            assert 0 < r < len(grid) - 1
            assert 0 < c < len(grid[0]) - 1
print(count)
