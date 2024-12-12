from itertools import product


def part1(equations):
    total = 0
    operators = [
        lambda x, y: x + y,
        lambda x, y: x * y
    ]
    for key, values in equations.items():
        operations_list = list(product(operators, repeat=len(values) - 1))
        results = []
        for operations in operations_list:
            result = values[0]
            for i in range(1, len(values)):
                result = operations[i-1](result, values[i])
            results.append(result)
        if key in results:
            total += key
    return total


def part2(equations):
    total = 0
    operators = [
        lambda x, y: x + y,
        lambda x, y: x * y,
        lambda x, y: int(str(x) + str(y))
    ]
    for key, values in equations.items():
        operations_list = list(product(operators, repeat=len(values) - 1))
        results = []
        for operations in operations_list:
            result = values[0]
            for i in range(1, len(values)):
                result = operations[i-1](result, values[i])
            results.append(result)
        if key in results:
            total += key
    return total


if __name__ == '__main__':
    equations = {}
    with open('07-input.txt', 'r') as input:
        for line in input:
            key = int(line.strip().split(':')[0])
            values = [int(x) for x in line.strip().split(':')[1].split()]
            equations[key] = values
    print(part1(equations))
    print(part2(equations))