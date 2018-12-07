from collections import defaultdict
import re
import heapq


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parents = set()


re_steps = re.compile("""Step (.+) must be finished before step (.+) can begin.""")
steps = []
nodes = dict()
with open('input.txt', 'r') as f:
    for line in f:
        m = re_steps.match(line)
        a, b = m[1], m[2]
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[a].children.add(nodes[b])
        nodes[b].parents.add(nodes[a])

q = [n.name for n in nodes.values() if len(n.parents) == 0]
heapq.heapify(q)
ans = []
while len(q) > 0:
    name = heapq.heappop(q)
    ans.append(name)

    node = nodes[name]
    for child in node.children:
        child.parents.remove(node)
        if len(child.parents) == 0:
            heapq.heappush(q, child.name)

print("".join(ans))
