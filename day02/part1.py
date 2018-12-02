from collections import defaultdict

twos = 0
threes = 0
for line in open("input").readlines():
    line = line.strip()
    d = defaultdict(int)
    for ch in line:
        d[ch] += 1
    found_twos = False
    found_threes = False
    for k, v in d.items():
        if v == 2:
            found_twos = True
        if v == 3:
            found_threes = True
    twos += found_twos
    threes += found_threes
print(twos * threes)
