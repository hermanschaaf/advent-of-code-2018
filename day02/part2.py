from collections import defaultdict


def diff_by_one(w, w2):
    d = 0
    pos = 0
    for i, ch in enumerate(w):
        if ch != w2[i]:
            d += 1
            pos = i
    if d != 1:
        return False
    return w[:pos] + w[pos+1:]


words = []
for line in open("input").readlines():
    words.append(line)

for i, w in enumerate(words):
    for u, w2 in enumerate(words[i+1:], i+1):
        ans = diff_by_one(w, w2)
        if ans:
            print(ans)
            exit(0)
