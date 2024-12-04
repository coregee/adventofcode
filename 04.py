def rotate(array):
    return [list(row) for row in zip(*array[::-1])]


def getDiagonals(array, trim=False):
    rows = len(array)
    cols = len(array[0])
    diagonals = []
    start = 1 if trim else 0
    for a in range(start, cols):
        diagonal = [array[b][a + b] for b in range(min(rows, cols - a))]
        diagonals.append(diagonal)
    return diagonals


def part1(array):
    diagonals = []
    for i in range(4):
        array = rotate(array)
        diagonals.extend(getDiagonals(array, i < 2))
    lines = [''.join(d) for d in diagonals] + [''.join(a) for a in array] + [''.join(a) for a in rotate(array)]
    count = 0
    for line in lines:
        count += line.count('XMAS')
        count += line.count('SAMX')
    return count


def getMASx(array):
    rows = len(array)
    cols = len(array[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if array[i][j] == 'M' \
                    and array[i + 2][j] == 'M' \
                    and array[i][j + 2] == 'S' \
                    and array[i + 2][j + 2] == 'S' \
                    and array[i + 1][j + 1] == 'A':
                count += 1
    return count


def part2(array):
    count = 0
    for _ in range(4):
        array = rotate(array)
        count += getMASx(array)
    return count


if __name__ == '__main__':
    with open('04-input.txt', 'r') as input:
        array = [list(line.strip()) for line in input]
    print(part1(array))
    print(part2(array))