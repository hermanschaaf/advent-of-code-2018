from collections import namedtuple

fp = open('input.txt', 'r')


class Cart(object):
    def __init__(self, row, col, direction, count):
        self.row = row
        self.col = col
        self.dir = direction
        self.count = count


P = namedtuple("P", "row col")
left, right, up, down = ["<", ">", "^", "v"]
dirs = {left: P(0, -1), right: P(0, 1), up: P(-1, 0), down: P(1, 0)}
grid = []
carts = []
for row, line in enumerate(fp):
    l = [ch for ch in line.strip("\n")]
    c = []
    for col, ch in enumerate(line):
        if ch in (left, right, up, down):
            c.append(Cart(row, col, ch, 0))
    for i, ci in enumerate(c):
        if ci.dir in (left, right):
            l[ci.col] = "-"
        elif ci.dir in (up, down):
            l[ci.col] = "|"

    grid.append(l)
    carts += c


def print_carts():
    for row, line in enumerate(grid):
        line = line[:]
        for cart in carts:
            if cart.row == row:
                line[cart.col] = cart.dir
        print("".join(line))


def turn_left(d):
    if d == left:
        return down
    if d == right:
        return up
    if d == up:
        return left
    if d == down:
        return right


def turn_right(d):
    return turn_left(turn_left(turn_left(d)))


while True:
    seen = set()
    # print_carts()
    for c in carts:
        if grid[c.row][c.col] == "/":
            if c.dir == left:
                c.dir = down
            elif c.dir == right:
                c.dir = up
            elif c.dir == up:
                c.dir = right
            elif c.dir == down:
                c.dir = left
        elif grid[c.row][c.col] == "\\":
            if c.dir == left:
                c.dir = up
            elif c.dir == right:
                c.dir = down
            elif c.dir == up:
                c.dir = left
            elif c.dir == down:
                c.dir = right
        if grid[c.row][c.col] == "+":
            if c.count % 3 == 0:
                c.dir = turn_left(c.dir)
            elif c.count % 3 == 2:
                c.dir = turn_right(c.dir)
            c.count += 1
        d = dirs[c.dir]
        nxt = P(c.row + d.row, c.col + d.col)
        c.row = nxt.row
        c.col = nxt.col

        if nxt not in seen:
            seen.add(nxt)
        else:
            print("{},{}".format(nxt[1], nxt[0]))
            exit(0)
