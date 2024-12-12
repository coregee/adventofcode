def get_trails(position, grid):
    # Recursion time!!
    result = set()
    y, x = position[0], position[1]
    current = grid[y][x]
    if current == 9:
        result.add((y, x))
    else:
        neighbours = []
        if y-1 in range(len(grid)) and grid[y-1][x] == current + 1:  # N
            neighbours.append((y-1, x))
        if x-1 in range(len(grid[0])) and grid[y][x-1] == current + 1:  # W
            neighbours.append((y, x-1))
        if y+1 in range(len(grid)) and grid[y+1][x] == current + 1:  # S
            neighbours.append((y+1, x))
        if x+1 in range(len(grid[0])) and grid[y][x+1] == current + 1:  # E
            neighbours.append((y, x+1))
        for neighbour in neighbours:
            result.update(get_trails(neighbour, grid))
    return result


def part1(grid):
    trailheads = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads[(i, j)] = []
    for trailhead in trailheads.keys():
        trailheads[trailhead] = get_trails(trailhead, grid)
    return sum(len(values) for values in trailheads.values())


def get_rating(position, grid):
    rating = 0
    y, x = position[0], position[1]
    current = grid[y][x]
    if current == 9:
        rating += 1
    else:
        neighbours = []
        if y-1 in range(len(grid)) and grid[y-1][x] == current + 1:  # N
            neighbours.append((y-1, x))
        if x-1 in range(len(grid[0])) and grid[y][x-1] == current + 1:  # W
            neighbours.append((y, x-1))
        if y+1 in range(len(grid)) and grid[y+1][x] == current + 1:  # S
            neighbours.append((y+1, x))
        if x+1 in range(len(grid[0])) and grid[y][x+1] == current + 1:  # E
            neighbours.append((y, x+1))
        rating += sum(get_rating(neighbour, grid) for neighbour in neighbours)
    return rating


def part2(grid):
    trailheads = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads[(i, j)] = []
    for trailhead in trailheads.keys():
        trailheads[trailhead] = get_rating(trailhead, grid)
    return sum(value for value in trailheads.values())


if __name__ == '__main__':
    with open('10-input.txt', 'r') as input:
        grid = [list(int(x) for x in line.strip()) for line in input]
    print(part1(grid))
    print(part2(grid))