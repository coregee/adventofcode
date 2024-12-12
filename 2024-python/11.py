import copy
from collections import defaultdict


def process_stone(stone):
    if stone == 0:
        return [1]
    else:
        string = str(stone)
        length = len(string)
        if length % 2 == 0:
            left = int(string[:length//2])
            right = int(string[length//2:])
            return [left, right]
        else:
            return [stone * 2024]


def process_blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        next_values = process_stone(stone)
        for val in next_values:
            new_stones[val] += count
    return new_stones


def puzzle(line, blinks):
    """oh dear"""
    # Create a lookup of [stone]: [count]
    stones = defaultdict(int)
    for stone in line:
        stones[stone] = 1
    for i in range(blinks):
        stones = process_blink(stones)
    return sum(stones.values())


if __name__ == '__main__':
    line = []
    with open('11-input.txt', 'r') as input:
        for row in input:
            for x in row.strip().split():
                line.append(int(x))
    print(puzzle(copy.deepcopy(line), 25))
    print(puzzle(copy.deepcopy(line), 75))