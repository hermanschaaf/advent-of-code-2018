from collections import namedtuple, deque, defaultdict

Point = namedtuple("Point", "id row col")

max_row, max_col = 0, 0
points = []
for i, line in enumerate(open('input.txt', 'r')):
    col, row = map(int, map(str.strip, line.strip().split(",")))
    max_row = max(max_row, row)
    max_col = max(max_col, col)
    points.append(Point(i, row, col))

grid = [[(None, -1) for c in range(max_col + 1)] for r in range(max_row + 1)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque((0, p) for p in points)
seen = defaultdict(set)
while len(q) > 0:
    steps, p = q.popleft()
    s, val = grid[p.row][p.col]
    if s is None:
        grid[p.row][p.col] = (steps, p.id)
    elif s == steps and val != p.id:
        grid[p.row][p.col] = (steps, -1)  # shared
    elif steps < s:
        assert False
    else:
        continue

    for d in dirs:
        np = Point(p.id, p.row+d[0], p.col+d[1])
        if 0 <= np.row < len(grid) and 0 <= np.col < len(grid[0]):
            if np not in seen[p.id]:
                q.append((steps + 1, np))
            seen[p.id].add(np)

counts = defaultdict(int)
edges = set()
chars = "abcdefghijklmnopqrstuvwxyz."
for r in range(len(grid)):
    for c in range(len(grid[0])):
        s, val = grid[r][c]
        counts[val] += 1
        if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
            edges.add(val)
        # print(chars[int(val)], end="")
    # print("")
print(max(count for i, count in counts.items() if i not in edges))
