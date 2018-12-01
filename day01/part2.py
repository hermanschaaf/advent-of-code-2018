v = 0
f = list(map(int, open("day1.in").readlines()))
k = set()
done = False
while not done:
    for fi in f:
        v += fi
        if v in k:
            done = True
            break
        k.add(v)
print(v)