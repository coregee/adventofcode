import copy
import time

def part1(grid):
    # Get starting coordinates
    for i in range(len(grid)):
        if '^' in grid[i]:
            x = grid[i].index('^')
            y = i
            break
    direction = 'up'

    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        # Store the direction(s) faced on the tile as a set
        if not isinstance(grid[y][x], set):
            grid[y][x] = set()
        grid[y][x].add(direction)

        # Traverse the grid
        if direction == 'up':
            try:
                if grid[y-1][x] == '#':
                    direction = 'right'
                else:
                    y -= 1
            except:
                y -= 1
        elif direction == 'right':
            try:
                if grid[y][x+1] == '#':
                    direction = 'down'
                else:
                    x += 1
            except:
                x += 1
        elif direction == 'down':
            try:
                if grid[y+1][x] == '#':
                    direction = 'left'
                else:
                    y += 1
            except:
                y += 1
        else:  # left
            try:
                if grid[y][x-1] == '#':
                    direction = 'up'
                else:
                    x -= 1
            except:
                x -= 1
    # Tally up
    return sum(isinstance(x, set) for y in grid for x in y)


def is_loop(grid, y, x, direction):
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        if direction in grid[y][x]:
            return True

        if not isinstance(grid[y][x], set):
            grid[y][x] = set()
        grid[y][x].add(direction)

        if direction == 'up':
            if y - 1 in range(len(grid)) and grid[y - 1][x] == '#':
                direction = 'right'
            else:
                y -= 1
        elif direction == 'right':
            if x + 1 in range(len(grid[0])) and grid[y][x + 1] == '#':
                direction = 'down'
            else:
                x += 1
        elif direction == 'down':
            if y + 1 in range(len(grid)) and grid[y + 1][x] == '#':
                direction = 'left'
            else:
                y += 1
        else:  # direction == 'left'
            if x - 1 in range(len(grid[0])) and grid[y][x - 1] == '#':
                direction = 'up'
            else:
                x -= 1
    return False


CHECKED = []
def check_loop(grid, y, x, direction):
    y1, x1 = y, x  # coordinates of next tile (for obstacle)
    if direction == 'up':
        y1 -= 1
        direction = 'right'
    elif direction == 'right':
        x1 += 1
        direction = 'down'
    elif direction == 'down':
        y1 += 1
        direction = 'left'
    else:  # direction == 'left'
        x1 -= 1
        direction = 'up'
    if x1 in range(len(grid[0])) and y1 in range(len(grid)) \
            and [y1, x1] not in CHECKED:
        CHECKED.append([y1, x1])
        t_grid = copy.deepcopy(grid)
        t_grid[y1][x1] = '#'
        return is_loop(t_grid, y, x, direction)
    else:
        return False


def part2(grid):
    # Set initial coords and direction
    for i in range(len(grid)):
        if '^' in grid[i]:
            x = grid[i].index('^')
            y = i
            break
    direction = 'up'

    count = 0

    while x in range(len(grid[0])) and y in range(len(grid)):
        # Store the direction(s) faced on the tile as a set
        if not isinstance(grid[y][x], set):
            grid[y][x] = set()
        grid[y][x].add(direction)

        # Check if adding an obstacle ahead creates a loop
        if check_loop(grid, y, x, direction):
            count += 1
            print(f'Count: {count}')

        # Move to next tile or change direction
        if direction == 'up':
            if y - 1 in range(len(grid)) and grid[y - 1][x] == '#':
                direction = 'right'
            else:
                y -= 1
        elif direction == 'right':
            if x + 1 in range(len(grid[0])) and grid[y][x + 1] == '#':
                direction = 'down'
            else:
                x += 1
        elif direction == 'down':
            if y + 1 in range(len(grid)) and grid[y + 1][x] == '#':
                direction = 'left'
            else:
                y += 1
        else:  # direction == 'left'
            if x - 1 in range(len(grid[0])) and grid[y][x - 1] == '#':
                direction = 'up'
            else:
                x -= 1
    return count


if __name__ == '__main__':
    with open('06-input.txt', 'r') as input:
        grid = [list(line.strip()) for line in input]
    print(part1(copy.deepcopy(grid)))
    start = time.time()
    print(part2(copy.deepcopy(grid)))
    end = time.time()
    print(f"This took {end - start:.2f} seconds of your life away.")