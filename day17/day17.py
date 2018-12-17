import fileinput
import collections
import sys

from collections import namedtuple

sys.setrecursionlimit(20000)
Point = namedtuple("Point", ["x", "y"])

clay = collections.defaultdict(bool)
xmin, xmax = None, None
ymin, ymax = None, None

settled = set()
flowing = set()
up = Point(0, -1)
down = Point(0, 1)
left = Point(-1, 0)
right = Point(1, 0)


def print_grid():
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if (x, y) in settled:
                print("~", end="")
            elif (x, y) in flowing:
                print("|", end="")
            elif (x, y) in clay:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def load_file():
    global clay, xmin, xmax, ymin, ymax
    for line in fileinput.input():
        a, brange = line.split(',')
        if a[0] == 'x':
            x = int(a.split('=')[1])
            y1, y2 = (int(y) for y in brange.split('=')[1].split('..'))

            for y in range(y1, y2 + 1):
                clay[Point(x, y)] = True
        else:
            y = int(a.split('=')[1])
            x1, x2 = (int(x) for x in brange.split('=')[1].split('..'))

            for x in range(x1, x2 + 1):
                clay[Point(x, y)] = True

    xmin, xmax = min(clay, key=lambda p: p.x).x, max(clay, key=lambda p: p.x).x
    ymin, ymax = min(clay, key=lambda p: p.y).y, max(clay, key=lambda p: p.y).y


def simulate(pt, dr=down):
    flowing.add(pt)
    below = Point(pt.x, pt.y + 1)

    if not clay[below] and below not in flowing and 1 <= below.y <= ymax:
        simulate(below)

    if not clay[below] and below not in settled:
        return False

    p_left = Point(pt.x - 1, pt.y)
    p_right = Point(pt.x + 1, pt.y)

    left_filled = clay[p_left] or p_left not in flowing and simulate(p_left, dr=Point(-1, 0))
    right_filled = clay[p_right] or p_right not in flowing and simulate(p_right, dr=Point(1, 0))

    if dr == down and left_filled and right_filled:
        settled.add(pt)

        while p_left in flowing:
            settled.add(p_left)
            p_left = Point(p_left.x - 1, p_left.y)

        while p_right in flowing:
            settled.add(p_right)
            p_right = Point(p_right.x + 1, p_right.y)

    is_flowing = False
    if dr == left:
        is_flowing = left_filled or clay[p_left]
    elif dr == right:
        is_flowing = right_filled or clay[p_right]
    return is_flowing


load_file()
simulate(Point(500, 0))
print_grid()
print('Part 1:', sum(1 for pt in flowing | settled if ymin <= pt[1] <= ymax))
print('Part 2:', sum(1 for pt in settled if ymin <= pt[1] <= ymax))
