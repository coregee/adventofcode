import re


def part1(text):
    matches = re.findall(r"mul\(\d+,\d+\)", text)
    total = 0
    for match in matches:
        a = int(match[4:-1].split(',')[0])
        b = int(match[4:-1].split(',')[1])
        total += a * b
    return total


def part2(text):
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)
    total = 0
    enabled = True
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            a = int(match[4:-1].split(',')[0])
            b = int(match[4:-1].split(',')[1])
            total += a * b
    return total


if __name__ == '__main__':
    with open('03-input.txt', 'r') as input:
        lines = ''.join(line.strip() for line in input)
    print(part1(lines))
    print(part2(lines))