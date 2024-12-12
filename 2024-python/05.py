def isOrdered(row, pairs):
    for pair in pairs:
        if pair[0] in row and pair[1] in row:
            ordered = row.index(pair[0]) < row.index(pair[1])
            if not ordered:
                return False
    return True


def part1(pairs, rows):
    total = 0
    for row in rows:
        if isOrdered(row, pairs):
            total += row[(len(row) - 1) // 2]
    return total


def orderRow(pairs):
    row = []
    pair_dict = {}
    for pair in pairs:
        if pair[0] not in pair_dict:
            pair_dict[pair[0]] = [pair[1]]
        else:
            pair_dict[pair[0]].append(pair[1])
    # Sort by greatest-requirements first
    pair_dict = dict(sorted(pair_dict.items(), key=lambda item: len(item[1]), reverse=True))
    for k, v in pair_dict.items():
        if k not in row:
            row.append(k)
        for n in v:
            if n not in row:
                row.append(n)
            else:
                row.remove(n)
                row.insert(row.index(k) + 1, n)
    return row


def part2(pairs, rows):
    # Filter out ordered pairs
    rows = list(filter(lambda r: not isOrdered(r, pairs), rows))
    for i in range(len(rows)):
        rules = list(filter(lambda p: p[0] in rows[i] and p[1] in rows[i], pairs))
        rows[i] = orderRow(rules)
    total = 0
    for row in rows:
        total += row[(len(row) - 1) // 2]
    return total

if __name__ == '__main__':
    pairs = []
    rows = []
    with open('05-input.txt', 'r') as input:
        for line in input:
            if '|' in line:
                pairs.append([int(x) for x in line.strip().split('|')])
            elif ',' in line:
                rows.append([int(x) for x in line.strip().split(',')])
    print(part1(pairs, rows))
    print(part2(pairs, rows))