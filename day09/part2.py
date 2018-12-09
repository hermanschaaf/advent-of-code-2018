from collections import deque, defaultdict

r = open('input.txt', 'r').read().split(" ")
p, n = int(r[0]), int(r[-2])


class Circle(object):
    def __init__(self):
        self.circle = None

    def add(self, i):
        if i == 0:
            self.circle = deque([0])
            return 0

        if i % 23 == 0:
            self.circle.rotate(7)
            score = i + self.circle.pop()
            self.circle.rotate(-1)
            return score

        self.circle.rotate(-1)
        self.circle.append(i)
        return 0


# part 2
players = [0 for i in range(p)]
circle = Circle()
n *= 100
for i in range(n+1):
    players[i % p] += circle.add(i)

print(max(players))
