from collections import defaultdict
import re
import heapq


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parents = set()


def cost(v):
    return ord(v) - ord('A') + 1


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

workers = 5
timedelta = 60
timenow = 0

backlog = [n.name for n in nodes.values() if len(n.parents) == 0]
heapq.heapify(backlog)
timeline = []
heapq.heapify(timeline)
ans = []
done = 0
while done != len(nodes):
    while len(backlog) > 0 and workers > 0:
        name = heapq.heappop(backlog)
        t = (timenow + timedelta + cost(name), name)
        heapq.heappush(timeline, t)
        workers -= 1

    timenow, name = heapq.heappop(timeline)
    done += 1
    workers += 1
    node = nodes[name]
    for child in node.children:
        child.parents.remove(node)
        if len(child.parents) == 0:
            heapq.heappush(backlog, child.name)

print(timenow)
