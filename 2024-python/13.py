import numpy as np
import re


class Machine:
    def __init__(self, ax, ay, bx, by, px, py):
        self.ax = int(ax)
        self.ay = int(ay)
        self.bx = int(bx)
        self.by = int(by)
        self.px = int(px)
        self.py = int(py)


def solve_machine1(m):
    solutions = []
    for i in range(101):
        # Check A press
        rax = m.px - (i * m.ax)
        ray = m.py - (i * m.ay)
        b1, b2 = (rax / m.bx), (ray / m.by)
        if b1 == b2 and b1 in range(101) and b2 in range(101) and b1.is_integer() and b2.is_integer():
            solutions.append((i, b1))
        # Check B press
        rbx = m.px - (i * m.bx)
        rby = m.py - (i * m.by)
        a1, a2 = (rbx / m.ax), (rby / m.ay)
        if a1 == a2 and a1 in range(101) and a2 in range(101) and a1.is_integer() and a2.is_integer():
            solutions.append((a1, i))
    if len(solutions) == 0:
        return 0
    solutions = list(map(lambda s: s[0] * 3 + s[1], solutions))
    return min(solutions)


def part1(machines):
    tokens = 0
    for machine in machines:
        tokens += solve_machine1(machine)
    return tokens


def solve_machine2(m):
    det = (m.ax * m.by) - (m.ay * m.bx)
    if det == 0:
        return 0
    else:
        an = (m.px * m.by) - (m.py * m.bx)
        bn = (m.ax * m.py) - (m.ay * m.px)
        a = an / det
        b = bn / det
        if a.is_integer() and b.is_integer():
            return 3 * a + b
        else:
            return 0


def part2(machines):
    tokens = 0
    for machine in machines:
        tokens += solve_machine2(machine)
    return tokens


if __name__ == '__main__':
    p1machines = []
    p2machines = []
    with open('13-input.txt', 'r') as input:
        lines = input.readlines()
        i = 0
        while i+2 < len(lines):
            a = re.sub(r"[^0-9,]", "", lines[i])
            ax, ay = a.split(',')[0], a.split(',')[1]
            b = re.sub(r"[^0-9,]", "", lines[i+1])
            bx, by = b.split(',')[0], b.split(',')[1]
            p = re.sub(r"[^0-9,]", "", lines[i+2])
            px, py = int(p.split(',')[0]), int(p.split(',')[1])
            p1machines.append(Machine(ax,ay, bx,by, px,py))
            px += 10000000000000
            py += 10000000000000
            p2machines.append(Machine(ax,ay, bx,by, px,py))
            i += 4
    print(part1(p1machines))
    print(part2(p2machines))