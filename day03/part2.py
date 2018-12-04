import re


class Grid(object):
    def __init__(self, size=1000):
        self.grid = [[0 for i in range(size)] for u in range(size)]

    def add(self, id, left, top, width, height):
        for row in range(top, top+height):
            for col in range(left, left+width):
                self.grid[row][col] += 1

    def uniq(self, id, left, top, width, height):
        t = None
        for row in range(top, top+height):
            for col in range(left, left+width):
                if self.grid[row][col] > 1:
                    return False
        return True


grid = Grid()
claims = []
r = re.compile(r"""#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)""")
for line in open("input", "r").readlines():
    f = r.findall(line.strip())
    claim = list(map(int, f[0]))
    id, left, top, width, height = claim
    claims.append(claim)
    grid.add(id, left, top, width, height)
for claim in claims:
    if grid.uniq(*claim):
        print(claim[0])
        break
