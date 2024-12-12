from itertools import combinations


def isConsistent(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)


def rangeAdjacent(nums):
    diffs = [abs(nums[i + 1] - nums[i]) for i in range(len(nums) - 1)]
    return max(diffs) <= 3 and min(diffs) >= 1


def part1(reports):
    return [isConsistent(report) and rangeAdjacent(report) for report in reports].count(True)


def part2(reports):
    return [any(isConsistent(list(r)) and rangeAdjacent(list(r)) for r in combinations(report, len(report) - 1)) for report in reports].count(True)


if __name__ == '__main__':
    reports = []
    with open('02-input.txt', 'r') as input:
        for line in input.readlines():
            reports.append([int(x) for x in line.strip().split()])
    print(part1(reports))
    print(part2(reports))