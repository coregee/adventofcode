def get_section(grid, coordinates, section=None):
    """Takes 2D grid and coordinates,
    returns set of tile coordinate tuples in section"""
    if section is None:
        section = set()

    section.add(coordinates)

    i = coordinates[0]
    j = coordinates[1]
    plant = grid[i][j]

    if i-1 in range(len(grid)) and (i-1, j) not in section and grid[i-1][j] == plant:
        get_section(grid, (i-1, j), section)
    if j-1 in range(len(grid)) and (i, j-1) not in section and grid[i][j-1] == plant:
        get_section(grid, (i, j-1), section)
    if i+1 in range(len(grid)) and (i+1, j) not in section and grid[i+1][j] == plant:
        get_section(grid, (i+1, j), section)
    if j+1 in range(len(grid)) and (i, j+1) not in section and grid[i][j+1] == plant:
        get_section(grid, (i, j+1), section)

    return section


def fence_cost(section):
    """Takes set of (i, j) tuples. Returns cost of fencing them."""
    # this is very inefficient, but i do not care
    cost = 0
    for (i, j) in section:
        if (i-1, j) not in section:
            cost += 1
        if (i, j-1) not in section:
            cost += 1
        if (i+1, j) not in section:
            cost += 1
        if (i, j+1) not in section:
            cost += 1
    return cost


def part1(grid):
    sections = []
    traversed = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in traversed:
                result = get_section(grid, (i, j))
                sections.append(result)
                traversed.extend(result)
    cost = 0
    for section in sections:
        cost += fence_cost(section) * len(section)
    return cost


def rotate(direction, is_ccw=False):
    if not is_ccw:
        if direction == 'right':
            return 'down'
        elif direction == 'down':
            return 'left'
        elif direction == 'left':
            return 'up'
        else:
            return 'right'
    else:
        if direction == 'right':
            return 'up'
        elif direction == 'up':
            return 'left'
        elif direction == 'left':
            return 'down'
        else:
            return 'right'


def num_sides(section):
    """Takes a set of (i, j) coordinates.
    Returns the number of sides the 2D grid representation has."""
    # this is an abomination i am sorry
    borders = []
    for (i, j) in section:
        if (i-1,j) not in section:
            borders.append((i-1, j))
        if (i, j-1) not in section:
            borders.append((i, j-1))
        if (i+1, j) not in section:
            borders.append((i+1, j))
        if (i, j+1) not in section:
            borders.append((i, j+1))
    row_groups = {}  # {row: [col nodes]}
    col_groups = {}  # {col: [row nodes]}
    for (i, j) in borders:
        if i not in row_groups:
            row_groups[i] = {j}
        else:
            row_groups[i].add(j)
        if j not in col_groups:
            col_groups[j] = {i}
        else:
            col_groups[j].add(i)
    sides = 0

    for row, cols in row_groups.items():
        cols = list(cols)
        cols.sort()
        top = False
        bottom = False
        for i in range(len(cols)):
            if (row-1, cols[i]) in section:
                if not top:
                    sides += 1
                    top = True
            else:
                top = False
            if (row+1, cols[i]) in section:
                if not bottom:
                    sides += 1
                    bottom = True
            else:
                bottom = False
            if (row, cols[i]+1) in section or (i+1 in range(len(cols)) and cols[i]+1 != cols[i+1]):
                top = False
                bottom = False

    for col, rows in col_groups.items():
        rows = list(rows)
        rows.sort()
        left = False
        right = False
        for i in range(len(rows)):
            if (rows[i], col-1) in section:
                if not left:
                    sides += 1
                    left = True
            else:
                left = False
            if (rows[i], col+1) in section:
                if not right:
                    sides += 1
                    right = True
            else:
                right = False
            if (rows[i]+1, col) in section or (i+1 in range(len(rows)) and rows[i]+1 != rows[i+1]):
                left = False
                right = False

    return sides


def part2(grid):
    sections = []
    traversed = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in traversed:
                result = get_section(grid, (i, j))
                sections.append(result)
                traversed.extend(result)
    cost = 0
    for section in sections:
        amount = num_sides(section) * len(section)
        cost += amount
    return cost


if __name__ == '__main__':
    with open('12-input.txt', 'r') as input:
        grid = [list(row.strip()) for row in input]
    print(part1(grid))
    print(part2(grid))