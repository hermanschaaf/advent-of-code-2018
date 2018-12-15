import fileinput
from collections import namedtuple, deque


class Position(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.prev = None

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Position(self.row - other.row, self.col - other.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __abs__(self):
        return abs(self.row) + abs(self.col)

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return "Position({},{})".format(self.row, self.col)


class Unit(object):
    def __init__(self, position, kind, hp, attack_power=3):
        self.position = position
        self.kind = kind
        self.hp = hp
        self.attack_power = attack_power

    def __repr__(self):
        return "{}({})".format(self.kind, self.hp)

    def is_adjacent(self, other):
        d = self.position - other.position
        return abs(d) == 1

    def attack(self, other):
        other.hp -= self.attack_power

    def is_dead(self):
        return self.hp <= 0


class Battlefield(object):
    directions = (
        Position(-1, 0),  # up
        Position(0, -1),  # left
        Position(0, 1),  # right
        Position(1, 0),  # down
    )

    def __init__(self, reader, elf_attack_power=3):
        grid = []
        units = []
        for row, line in enumerate(reader):
            grid.append([ch for ch in line.strip()])
            for col, ch in enumerate(line):
                if ch in "EG":
                    pos = Position(row=row, col=col)
                    unit = Unit(pos, kind=ch, hp=200)
                    if ch == "E":
                        unit.attack_power = elf_attack_power
                    units.append(unit)
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self._grid = grid
        self._units = units
        self._left = dict((k, len(list(u for u in units if u.kind == k))) for k in "GE")
        self._is_done = False

    def __repr__(self):
        s = []
        units = sorted(self._units, key=self._reading_order)
        for rw, row in enumerate(self._grid):
            r = "".join(row)
            r += " " + ",".join(map(str, (u for u in units if u.position.row == rw and not u.is_dead())))
            s.append(r)
        return "\n".join(s) + "\n"

    def step(self):
        self._units.sort(key=self._reading_order)
        for unit in self._units:
            if unit.is_dead():
                continue

            if self.is_done():
                return True

            if not self._is_in_range(unit):
                self._move_with_unit(unit)

            self._attack_with_unit(unit)

        return False

    def _reading_order(self, unit):
        return unit.position.row * self.num_cols + unit.position.col

    def _is_in_range(self, unit):
        for enemy in self._iter_enemies(unit):
            if unit.is_adjacent(enemy):
                return True
        return False

    def _move_with_unit(self, unit):
        best_dist, best_next_pos = None, None
        for enemy in self._iter_enemies(unit):
            for open_space in self._iter_open_spaces(enemy):
                dist, next_pos = self.find_path(unit.position, open_space)
                if dist is None:
                    continue

                if best_dist is None or dist < best_dist:
                    best_dist = dist
                    best_next_pos = next_pos

        if best_dist is not None:
            assert self.is_open(best_next_pos)
            self._grid[unit.position.row][unit.position.col] = '.'
            self._grid[best_next_pos.row][best_next_pos.col] = unit.kind
            unit.position = best_next_pos

    def _attack_with_unit(self, unit):
        best_enemy = None
        for enemy in self._iter_enemies(unit):
            if unit.is_adjacent(enemy):
                if best_enemy is None or enemy.hp < best_enemy.hp:
                    best_enemy = enemy
        if best_enemy is not None:
            unit.attack(best_enemy)
            if best_enemy.is_dead():
                self._grid[best_enemy.position.row][best_enemy.position.col] = '.'
                self._left[best_enemy.kind] -= 1
                if self._left[best_enemy.kind] == 0:
                    self._is_done = True

    def _iter_enemies(self, unit):
        for u in self._units:
            if u.kind != unit.kind and not u.is_dead():
                yield u

    def _iter_open_spaces(self, unit):
        for d in Battlefield.directions:
            p = unit.position + d
            if self.is_open(p):
                yield p

    def is_open(self, p):
        if 0 <= p.row < self.num_rows and 0 <= p.col < self.num_cols:
            return self._grid[p.row][p.col] == '.'
        return False

    def find_path(self, p1, p2):
        q = deque([(p1+d, 1) for d in Battlefield.directions if self.is_open(p1+d)])
        seen = set()
        while len(q) > 0:
            p, d = q.popleft()
            if p == p2:
                while p.prev is not None:
                    p = p.prev
                return d, p
            for dr in Battlefield.directions:
                np = p + dr
                np.prev = p
                if np not in seen and self.is_open(np):
                    q.append((np, d + 1))
                    seen.add(np)
        return None, None

    def is_done(self):
        return self._is_done

    def score(self):
        if not self.is_done():
            return 0

        s = 0
        for u in self._units:
            if u.is_dead():
                continue
            s += u.hp
        return s

    def elf_losses(self):
        return sum(int(u.is_dead()) for u in self._units if u.kind == 'E')


if __name__ == '__main__':
    lines = [line for line in fileinput.input()]
    # part 1
    b = Battlefield(lines)
    steps = 0
    while True:
        is_done = b.step()
        if is_done:
            break
        steps += 1
    score = b.score()
    print("Part 1:", steps, score, steps * score)

    # part 2
    mn = 4
    mx = 300
    while mx >= mn:
        ap = mn + (mx-mn) // 2
        print("Attack power", ap)
        b = Battlefield(lines, elf_attack_power=ap)
        steps = 0
        while True:
            is_done = b.step()
            if is_done:
                break
            if b.elf_losses() > 0:
                break
            steps += 1
        score = b.score()
        if b.elf_losses() == 0:
            mx = ap - 1
        else:
            mn = ap + 1

    print("Final attack power =", ap)
    print("Part 2:", steps, score, steps * score)
