import fileinput
import re
from collections import Counter
import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divs.extend([i, n//i])
    divs.extend([n])
    return list(set(divs))


class Program(object):
    """docstring for Program"""

    def __init__(self, r, ip):
        self.r = r[:]
        self.ip = ip
        self.ip_value = 0

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

    def exec(self, instructions, stop_when_instruction=None):
        while 0 <= self.ip_value < len(instructions):
            self.r[self.ip] = self.ip_value
            inst, A, B, C = instructions[self.ip_value]
            getattr(self, inst)(A, B, C)
            self.ip_value = self.r[self.ip] + 1
            if stop_when_instruction == self.ip_value:
                break


ip = None
instructions = []
for line in fileinput.input():
    if line.startswith("#ip"):
        ip = int(line.split(" ")[-1])
        continue

    instr, A, B, C = line.split(" ")
    A, B, C = [int(x) for x in (A, B, C)]
    instructions.append((instr, A, B, C))

# part 1
program = Program([0 for i in range(6)], ip)
program.exec(instructions)
print("Part 1:", program.r[0])

# part 2
program = Program([1] + [0 for i in range(5)], ip)
program.exec(instructions, stop_when_instruction=3)

# the value of r[5]
print("Part 2:", sum(divisors(program.r[5])))
