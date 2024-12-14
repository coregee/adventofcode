import copy

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox


class Robot:
    def __init__(self, px, py, vx, vy):
        self.start_x = px
        self.start_y = py
        self.pos_x = px
        self.pos_y = py
        self.vel_x = vx
        self.vel_y = vy

    def pass_time(self, seconds, x, y):
        """Update position by grid constraints
        and time passed."""
        self.pos_x = (self.pos_x + (self.vel_x * seconds)) % x
        self.pos_y = (self.pos_y + (self.vel_y * seconds)) % y


class Grid:
    def __init__(self, robots, x, y):
        self.robots = robots
        self.x = x
        self.y = y

    def pass_time(self, seconds):
        for robot in self.robots:
            robot.pass_time(seconds, self.x, self.y)

    def get_safety_factor(self):
        q00, q01, q10, q11 = 0, 0, 0, 0
        for robot in self.robots:
            if robot.pos_x == self.x // 2 or robot.pos_y == self.y // 2:
                continue
            left = robot.pos_x in range(self.x // 2)
            up = robot.pos_y in range(self.y // 2)
            if left:
                if up:
                    q00 += 1
                else:
                    q01 += 1
            else:
                if up:
                    q10 += 1
                else:
                    q11 += 1
        return q00*q01*q10*q11


def part1(robots, x, y):
    grid = Grid(robots, x, y)
    grid.pass_time(100)
    return grid.get_safety_factor()


def part2(robots, x, y):
    # wasn't expecting this for part 2 lol
    grid = Grid(robots, x, y)
    seconds = 0

    def generate_graph():
        data = np.zeros((y, x))
        for robot in grid.robots:
            data[robot.pos_y][robot.pos_x] = 1
        return data

    def update(event):
        data = generate_graph()
        im.set_data(data)
        ax.set_title(f"Time passed: {seconds}")
        plt.draw()

    def get_next(event):
        nonlocal seconds
        s = int(input.text)
        grid.pass_time(s)
        seconds += s
        update(event)

    def get_prev(event):
        nonlocal seconds
        s = int(input.text)
        grid.pass_time(-s)
        seconds -= s
        update(event)

    data = generate_graph()
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    im = ax.imshow(data)
    ax.set_title(f"Time passed: {seconds}")

    ax_prev = plt.axes([0.2, 0.05, 0.1, 0.1])
    btn_prev = Button(ax_prev, 'Back')
    btn_prev.on_clicked(get_prev)

    ax_next = plt.axes([0.7, 0.05, 0.1, 0.1])
    btn_next = Button(ax_next, 'Forward')
    btn_next.on_clicked(get_next)

    ax_input = plt.axes([0.45, 0.05, 0.1, 0.1])
    input = TextBox(ax_input, "Increment: ", initial="1")

    plt.show()



if __name__ == '__main__':
    robots = []
    with open('14-input.txt', 'r') as input:
        x = 101
        y = 103
        for line in input:
            p = line.strip().split()[0][2:]
            v = line.strip().split()[1][2:]
            px, py = int(p.split(',')[0]), int(p.split(',')[1])
            vx, vy = int(v.split(',')[0]), int(v.split(',')[1])
            robots.append(Robot(px, py, vx, vy))
    print(part1(copy.deepcopy(robots), x, y))
    print(part2(copy.deepcopy(robots), x, y))