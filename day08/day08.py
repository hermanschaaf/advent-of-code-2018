class Node(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    def total(self):
        s = sum(self.metadata)
        for ch in self.children:
            s += ch.total()
        return s

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        v = 0
        for m in self.metadata:
            ind = m - 1
            if 0 <= ind < len(self.children):
                v += self.children[ind].value()
        return v


def read(numbers, i=0):
    node = Node()
    c = numbers[i]
    m = numbers[i+1]
    used = 2
    for ch in range(c):
        child_node, u = read(numbers, i+used)
        node.children.append(child_node)
        used += u
    for mi in range(m):
        node.metadata.append(numbers[i+used+mi])
    used += m
    return node, used


numbers = list(map(int, open('input.txt').read().split(" ")))
root, _ = read(numbers)
print(root.total())
print(root.value())
