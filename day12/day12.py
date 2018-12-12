fp = open('input.txt', 'r')
pad = 500
padding = ['.' for i in range(pad)]
line = [c for c in fp.readline().strip().split(" ")[-1]]
state = padding[:] + line + padding[:]
fp.readline()
d = set()
for line in fp:
    p = line.strip().split(" ")
    if p[-1] == '#':
        d.add(p[0])

prev = {}
prev_left, prev_right = 0, len(line) - 1
prev_score = 0
end_step = 50000000000
for step in range(end_step):
    left, right = None, None
    newstate = ['.' for i in range(len(state))]
    score = 0
    for i in range(2, len(state)-2):
        s = ''.join(state[i-2:i+3])
        if s in d:
            newstate[i] = '#'
            score += i - pad
            if left is None:
                left = i
            right = i

    if state[prev_left:prev_right+1] == newstate[left:right+1]:
        score += (score - prev_score) * (end_step - step - 1)
        print(score)
        break
    prev_score = score
    prev_left, prev_right = left, right
    state = newstate
    if step == 19:
        print(score)
