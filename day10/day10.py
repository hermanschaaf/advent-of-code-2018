import re
from collections import namedtuple, Counter


class Point(object):
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


points = []
re_line = re.compile(r'position=<\s*(\-?\d+),\s*(\-?\d+)> velocity=<\s*(\-?\d+),\s*(\-?\d+)>')
for line in open('input.txt', 'r').readlines():
    m = re_line.match(line)
    m = list(map(int, [m[1], m[2], m[3], m[4]]))
    p = Point(m[0], m[1], m[2], m[3])
    points.append(p)


def get_grid():
    min_x = min(p.x for p in points)
    min_y = min(p.y for p in points)
    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)

    grid = [['.' for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]
    for p in points:
        grid[p.y - min_y][p.x - min_x] = '#'
    return grid


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")
    print("")


def get_width():
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    return max_x - min_x


u = 0
prev_width = get_width()
while True:
    for i, p in enumerate(points):
        p.x += p.vx
        p.y += p.vy

    width = get_width()
    if width > prev_width:
        for i, p in enumerate(points):
            p.x -= p.vx
            p.y -= p.vy
        g = get_grid()
        print_grid(g)
        print(u)
        break

    prev_width = width
    u += 1
