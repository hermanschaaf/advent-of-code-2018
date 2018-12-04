from collections import defaultdict
import re

guards = defaultdict(int)
minutes = defaultdict(lambda: [0 for i in range(60)])
r = re.compile(r"""^\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.+)$""")
re_guard = re.compile(r"""Guard \#(\d+) begins shift""")

id, start, end = None, 0, 0
lines = sorted(list(open('input', 'r').readlines()))
for line in lines:
    f = r.findall(line.strip())[0]
    times, text = list(map(int, f[:-1])), f[-1]
    if text.startswith("Guard"):
        id = int(re_guard.findall(text)[0])
    elif text.startswith("falls"):
        start = times[-1]
    elif text.startswith("wakes"):
        end = times[-1]
        guards[id] += end - start
        for m in range(start, end):
            minutes[id][m] += 1
    else:
        assert False, "unhandled case"

most = sorted(guards.items(), key=lambda x: x[1], reverse=True)[0][0]
minute = minutes[most].index(max(minutes[most]))
print(most * minute)
