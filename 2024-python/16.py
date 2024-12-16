def is_junction(grid, pos):
    """Determines if the grid position is a junction (3+ neighbours)"""
    y, x = pos[0], pos[1]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbours = 0
    for dir in dirs:
        if grid[y+dir[0]][x+dir[1]] != '#':
            neighbours += 1
    return neighbours >= 3


def is_dead_end(grid, pos):
    """Determines if the grid position is a dead-end (3+ walls)"""
    y, x = pos[0], pos[1]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    walls = 0
    for dir in dirs:
        if grid[y+dir[0]][x+dir[1]] == '#':
            walls += 1
    return walls >= 3


def get_neighbours(grid, node):
    """Return a list of neighbour junctions from the given node.
    Each neighbour is represented as ((y,x), out-dir, in-dir, cost)"""
    y, x = node
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbours = []
    for dir in dirs:
        out_dir = dir
        y1, x1 = y+dir[0], x+dir[1]
        if grid[y1][x1] != '#':
            cost = 1
            while not is_junction(grid, (y1, x1)) and not is_dead_end(grid, (y1, x1))\
                    and grid[y1][x1] != 'E' and grid[y1][x1] != 'S':
                y2, x2 = y1+dir[0], x1+dir[1]
                if grid[y2][x2] == '#':  # time to turn
                    cost += 1000
                    if dir[0] == 0:
                        adj_dirs = [(1, 0), (-1, 0)]
                    else:
                        adj_dirs = [(0, 1), (0, -1)]
                    if grid[y1 + adj_dirs[0][0]][x1 + adj_dirs[0][1]] != '#':
                        dir = adj_dirs[0]
                    else:
                        dir = adj_dirs[1]
                else:
                    y1, x1 = y2, x2
                    cost += 1
            if is_junction(grid, (y1, x1)) or grid[y1][x1] == 'E' or grid[y1][x1] == 'S':
                neighbours.append(((y1, x1), out_dir, dir, cost))
    return neighbours


class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.start = None
        self.end = None
        self.nodes = {}  # { (y1, x1): [((y2, x2), out-dir, in-dir, cost), (...)] }
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'S':
                    self.nodes[(i, j)] = get_neighbours(grid, (i, j))
                    self.start = (i, j)
                elif self.grid[i][j] == 'E':
                    self.nodes[(i, j)] = get_neighbours(grid, (i, j))
                    self.end = (i, j)
                elif self.grid[i][j] == '.':
                    if is_junction(self.grid, (i, j)):
                        self.nodes[(i, j)] = get_neighbours(grid, (i, j))


def get_turn_cost(current_dir, next_dir):
    if current_dir == next_dir:
        return 0
    elif current_dir in [(0, 1), (0, -1)] and next_dir in [(1, 0), (-1, 0)]\
            or current_dir in [(1, 0), (-1, 0)] and next_dir in [(0, 1), (0, -1)]:
        return 1000
    else:
        return 2000


def get_next(unvisited):
    best_node = None
    best_dist = float('inf')

    # Iterate over each node and its corresponding list of (dist, dir) tuples
    for node, values in unvisited.items():
        for dist, dir in values:
            # Check if the current direction has smaller magnitude
            if dist < best_dist:
                best_node = node
                best_dist = dist
    return best_node

def part1(maze):
    """Determines the minimum cost to traverse the maze from start to end,
    beginning by facing east. Hello Dijkstra."""
    # i hate this
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    unvisited = { key: [[float('inf'), dir] for dir in dirs] for key in maze.nodes.keys() }
    unvisited[maze.start] = [[0, (0, 1)], [1000, (1, 0)], [1000, (-1, 0)], [2000, (0, -1)]]
    visited = {}
    while len(unvisited) > 0:
        node = get_next(unvisited)
        values = unvisited[node]  # list of [distance, direction]
        for (neighbour, out_dir, in_dir, n_cost) in maze.nodes[node]:
            if neighbour in visited.keys():
                continue
            n_cost += min(cost + get_turn_cost(direction, out_dir) for cost, direction in values)
            for i in range(4):
                d_cost = n_cost + get_turn_cost(in_dir, unvisited[neighbour][i][1])
                if d_cost < unvisited[neighbour][i][0]:
                    unvisited[neighbour][i][0] = d_cost
        visited[node] = min(cost for cost, direction in values)
        del unvisited[node]
    return visited[maze.end]


if __name__ == '__main__':
    grid = []
    with open('16-input.txt', 'r') as input:
        for row in input:
            grid.append(list(row.strip()))
    maze = Maze(grid)
    print(part1(maze))