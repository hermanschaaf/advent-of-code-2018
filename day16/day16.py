import fileinput
import re
from collections import Counter


class Program(object):
    """docstring for Program"""

    def __init__(self, r):
        self.r = r[:]

    def addr(self, A, B, C):
        self.r[C] = self.r[A] + self.r[B]

    def addi(self, A, B, C):
        self.r[C] = self.r[A] + B

    def mulr(self, A, B, C):
        self.r[C] = self.r[A] * self.r[B]

    def muli(self, A, B, C):
        self.r[C] = self.r[A] * B

    def banr(self, A, B, C):
        self.r[C] = self.r[A] & self.r[B]

    def bani(self, A, B, C):
        self.r[C] = self.r[A] & B

    def borr(self, A, B, C):
        self.r[C] = self.r[A] | self.r[B]

    def bori(self, A, B, C):
        self.r[C] = self.r[A] | B

    def setr(self, A, B, C):
        self.r[C] = self.r[A]

    def seti(self, A, B, C):
        self.r[C] = A

    def gtir(self, A, B, C):
        if A > self.r[B]:
            self.r[C] = 1
        else:
            self.r[C] = 0

    def gtri(self, A, B, C):
        if self.r[A] > B:
            self.r[C] = 1
        else:
            self.r[C] = 0

    def gtrr(self, A, B, C):
        if self.r[A] > self.r[B]:
            self.r[C] = 1
        else:
            self.r[C] = 0

    def eqir(self, A, B, C):
        if A == self.r[B]:
            self.r[C] = 1
        else:
            self.r[C] = 0

    def eqri(self, A, B, C):
        if self.r[A] == B:
            self.r[C] = 1
        else:
            self.r[C] = 0

    def eqrr(self, A, B, C):
        if self.r[A] == self.r[B]:
            self.r[C] = 1
        else:
            self.r[C] = 0


allops = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
]

re_cmd = re.compile(r'\d+ \d+ \d+ \d+')
samples = []
lines = [line.strip() for line in fileinput.input() if line.strip()]
i = 0
while not re_cmd.match(lines[i]):
    before, cmd, after = lines[i:i+3]
    before = [int(c) for c in before[before.index("[")+1:before.index("]")].split(",")]
    cmd = [int(c) for c in cmd.split(" ")]
    after = [int(c) for c in after[after.index("[")+1:after.index("]")].split(",")]
    samples.append((before, cmd, after))
    i += 3

program_code = [[int(c) for c in line.split(" ")] for line in lines[i:]]

part1_ans = 0
opmap = dict((i, set(allops[:])) for i in range(len(allops)))
rev_opmap = dict((op, set(i for i in range(len(allops)))) for op in allops)
for before, cmd, after in samples:
    opcode, A, B, C = cmd
    cnt = 0
    for op in allops:
        program = Program(before)
        f = getattr(program, op)
        f(A, B, C)
        if program.r == after:
            cnt += 1
        else:
            if op in opmap[opcode]:
                opmap[opcode].remove(op)
                rev_opmap[op].remove(opcode)
    if cnt >= 3:
        part1_ans += 1
print("Part 1:", part1_ans)

final = {}
while True:
    changes = 0
    for code, ops in opmap.items():
        if len(ops) == 1:
            op = list(ops)[0]
            final[op] = code
            changes += 1

    for op, opcodes in rev_opmap.items():
        if len(opcodes) == 1:
            code = list(opcodes)[0]
            final[op] = code
            changes += 1

    for op, opcode in final.items():
        if opcode in opmap:
            del opmap[opcode]
        if op in rev_opmap:
            del rev_opmap[op]

        for _, ops in opmap.items():
            if op in ops:
                ops.remove(op)
        for _, codes in opmap.items():
            if opcode in codes:
                codes.remove(opcode)
    if changes == 0:
        print("Failed to find consistent codes")
        exit(1)
    if len(final) == len(allops):
        break

final_rev = dict((v, k) for k, v in final.items())
program = Program([0, 0, 0, 0])
for op, A, B, C in program_code:
    getattr(program, final_rev[op])(A, B, C)

print("Part 2:", program.r[0])
