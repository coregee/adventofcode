class Grid:
    def __init__(self, walls, boxes, robot):
        self.walls = walls
        self.boxes = boxes
        self.robot = robot

    def gps_sum(self):
        return sum(box[0] * 100 + box[1] for box in self.boxes)

    def move_robot(self, move):
        target = (self.robot[0] + move[0], self.robot[1] + move[1])
        if target not in self.boxes and target not in self.walls:  # nothing in the way
            self.robot = target
        elif target not in self.walls:  # box in the way
            last_box = target
            boxes_to_move = []
            while last_box in self.boxes:  # iterate through direction to first non-box space
                boxes_to_move.append(last_box)
                last_box = (last_box[0] + move[0], last_box[1] + move[1])
            if last_box not in self.walls:
                for box in boxes_to_move:
                    i = self.boxes.index(box)
                    self.boxes[i] = (box[0] + move[0], box[1] + move[1])
                self.robot = target


def part1(grid, moves):
    for move in moves:
        grid.move_robot(move)
    return grid.gps_sum()


class Grid2:
    def __init__(self, walls, boxes, robot):
        self.robot = (robot[0], robot[1] * 2)
        self.walls = []
        for (i, j) in walls:
            self.walls.extend([(i, j*2), (i, j*2 + 1)])
        self.boxes = []
        for (i, j) in boxes:
            self.boxes.append([(i, j*2), (i, j*2 + 1)])

    def gps_sum(self):
        return sum(box[0][0] * 100 + box[0][1] for box in self.boxes)

    def get_full_box(self, target):
        for i, box in enumerate(self.boxes):
            if target in box:
                return box
        return None

    def move_robot(self, move):
        target = (self.robot[0] + move[0], self.robot[1] + move[1])
        flat_boxes = sum(self.boxes, [])
        if target not in flat_boxes and target not in self.walls:
            self.robot = target
        elif target not in self.walls:
            if move in [[0, -1], [0, 1]]:  # horizontal movement
                last_coords = target
                boxes_to_move = set()
                while last_coords in flat_boxes:
                    boxes_to_move.add(tuple(self.get_full_box(last_coords)))
                    last_coords = (last_coords[0] + move[0], last_coords[1] + move[1])
                if last_coords not in self.walls:
                    for box in boxes_to_move:
                        i = self.boxes.index(list(box))
                        self.boxes[i] = [(box[0][0] + move[0], box[0][1] + move[1]),
                                         (box[1][0] + move[0], box[1][1] + move[1])]
                    self.robot = target
            else:  # vertical  movement :(
                last_coords = [target]
                boxes_to_move = set()
                while any(c in flat_boxes for c in last_coords) and all(c not in self.walls for c in last_coords):
                    # iterate through vertical stack until done with boxes or wall hit
                    next_boxes = set()
                    for c in last_coords:
                        box = self.get_full_box(c)
                        if box is not None:
                            next_boxes.add(tuple(box))
                    boxes_to_move.update(next_boxes)
                    last_coords = []
                    for (c0, c1) in next_boxes:
                        last_coords.append((c0[0] + move[0], c0[1] + move[1]))
                        last_coords.append((c1[0] + move[0], c1[1] + move[1]))
                if all(c not in self.walls for c in last_coords):
                    for box in boxes_to_move:
                        i = self.boxes.index(list(box))
                        self.boxes[i] = [(box[0][0] + move[0], box[0][1] + move[1]),
                                         (box[1][0] + move[0], box[1][1] + move[1])]
                    self.robot = target


def part2(grid, moves):
    i = 0
    for move in moves:
        i += 1
        print(f"Move {i}/{len(moves)}")
        grid.move_robot(move)
    return grid.gps_sum()


if __name__ == '__main__':
    walls = []
    boxes = []
    robot = None
    moves = []
    move_map = {
        '<': [0, -1],
        '>': [0, 1],
        '^': [-1, 0],
        'v': [1, 0]
    }
    with open('15-input.txt', 'r') as input:
        lines = input.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[i].strip())):
                if lines[i][j] == '#':
                    walls.append((i, j))
                elif lines[i][j] == 'O':
                    boxes.append((i, j))
                elif lines[i][j] == '@':
                    robot = (i, j)
                elif lines[i][j] in ['<', 'v', '>', '^']:
                    moves.append(lines[i][j])
    grid = Grid(walls, boxes, robot)
    grid2 = Grid2(walls, boxes, robot)
    moves = list(map(lambda char: move_map[char], moves))
    print(part1(grid, moves))
    print(part2(grid2, moves))