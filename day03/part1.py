import re


class Grid(object):
    def __init__(self, size=1000):
        self.grid = [[0 for i in range(size)] for u in range(size)]

    def add(self, left, top, width, height):
        for row in range(top, top+height):
            for col in range(left, left+width):
                self.grid[row][col] += 1

    def overlap(self):
        t = 0
        for row in self.grid:
            for val in row:
                if val >= 2:
                    t += 1
        return t


grid = Grid()
claims = []
r = re.compile(r"""#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)""")
for line in open("input", "r").readlines():
    f = r.findall(line.strip())
    claim = map(int, f[0])
    i, left, top, width, height = claim
    claims.append((left, top, width, height))
    grid.add(left, top, width, height)
print(grid.overlap())
