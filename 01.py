def part1(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part2(left, right):
    return sum(a * right.count(a) for a in left)


if __name__ == '__main__':
    left = []
    right = []
    with open('01-input.txt', 'r') as input:
        for line in input.readlines():
            left.append(int(line.strip().split()[0]))
            right.append(int(line.strip().split()[1]))
    print(part1(left, right))
    print(part2(left, right))