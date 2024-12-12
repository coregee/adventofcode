from itertools import combinations


def get_antinodes(pair, y, x):
    """Returns the coordinates of the two antinodes for the provided
    pair of [(y1,x1), (y2,x2)] coordinates.
    y and x are dimensions of target array."""
    y1, x1, y2, x2 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    if y1 < y2:
        ay1 = y1 - abs(y1 - y2)
        ay2 = y2 + abs(y1 - y2)
    else:
        ay1 = y1 + abs(y1 - y2)
        ay2 = y2 - abs(y1 - y2)
    if x1 < x2:
        ax1 = x1 - abs(x1 - x2)
        ax2 = x2 + abs(x1 - x2)
    else:
        ax1 = x1 + abs(x1 - x2)
        ax2 = x2 - abs(x1 - x2)
    nodes = []
    if ay1 in range(y) and ax1 in range(x):
        nodes.append((ay1, ax1))
    if ay2 in range(y) and ax2 in range(x):
        nodes.append((ay2, ax2))
    return nodes


def part1(rows):
    nodes = {}
    antinodes = set()
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            signal = rows[i][j]
            if signal == '.':
                continue
            if signal not in nodes:
                nodes[signal] = []
            nodes[signal].append((i, j))
    for key, values in nodes.items():
        pairs = list(combinations(values, 2))
        for pair in pairs:
            antinodes.update(get_antinodes(pair, len(rows), len(rows[0])))
    return len(antinodes)


def get_res_antinodes(pair, y, x):
    """Returns the coordinates of all resonant antinodes
    for the provided pair of [(y1,x1), (y2,x2)] coordinates,
    within the y, x bounds of the array."""
    y1, x1, y2, x2 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    y_step = y1 - y2
    x_step = x1 - x2
    nodes = []
    i = 0
    while (y1 + y_step * i) in range(y) and (x1 + x_step * i) in range(x):
        nodes.append((y1 + y_step * i, x1 + x_step * i))
        i += 1
    i = 0
    while (y2 - y_step * i) in range(y) and (x2 - x_step * i) in range(x):
        nodes.append((y2 - y_step * i, x2 - x_step * i))
        i += 1
    return nodes


def part2(rows):
    nodes = {}
    antinodes = set()
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            signal = rows[i][j]
            if signal == '.':
                continue
            if signal not in nodes:
                nodes[signal] = []
            nodes[signal].append((i, j))
    for key, values in nodes.items():
        pairs = list(combinations(values, 2))
        for pair in pairs:
            antinodes.update(get_res_antinodes(pair, len(rows), len(rows[0])))
    return len(antinodes)


if __name__ == '__main__':
    with open('08-input.txt', 'r') as input:
        grid = [list(row.strip()) for row in input]
    print(part1(grid))
    print(part2(grid))