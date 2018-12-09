r = open('input.txt', 'r').read().split(" ")
p, n = int(r[0]), int(r[-2])


class Circle(object):
    def __init__(self):
        self.ar = []
        self.ind = 0

    def add(self, i):
        n = len(self.ar)
        if n <= 1:
            self.ar.append(i)
            if n == 1:
                self.ind += 1
            return 0

        if i % 23 == 0:
            a = (self.ind-7) % n
            r = self.ar.pop(a)
            n -= 1
            self.ind = a % n
            return i + r

        b = (self.ind+1) % n
        self.ar.insert(b+1, i)
        self.ind = b + 1
        return 0

    def __repr__(self):
        s = []
        for i, a in enumerate(self.ar):
            if i == self.ind:
                s.append("{"+str(self.ar[i])+"}")
            else:
                s.append(str(self.ar[i]))
        return ", ".join(s)


# part 1
players = [0 for i in range(p)]
cp = 0
circle = Circle()
for i in range(n+1):
    players[cp] += circle.add(i)
    cp = (cp + 1) % p

print(max(players))
