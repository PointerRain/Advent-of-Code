"""
Advent of Code 2024
Day 15 - Warehouse Woes
https://adventofcode.com/2024/day/15

Part 1:
    Given a grid with walls, boxes, and a robot, simulate the robot's movement based on a sequence of moves.
    The robot can push boxes, but cannot push them through walls.
    :return: the sum of the distances of all boxes from the top-left corner of the grid after all moves.
Part 2:
    Each position in the grid is now 2x1 as well as the boxes but not the robot.
    :return: the sum of the distances of all boxes from the top-left corner of the grid after all moves.
"""
with open('day15.txt') as f:
    grid, moves = f.read().split('\n\n')

grid = grid.split('\n')
robot = None
walls = set()
boxes = set()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == '@' and robot is None:
            robot = (2*x, y)
        elif c == '#':
            walls.add((2*x, y))
            walls.add((2*x+1, y))
        elif c == 'O':
            boxes.add((2*x, y))
moves = moves.replace('\n', '')
print(robot, walls, boxes, moves)

width = 2*len(grid[0])
height = len(grid)

directions = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1)
}

for move in moves:
    dx, dy = directions[move]
    nx, ny = robot[0]+dx, robot[1]+dy
    removing_boxes = set()
    adding_boxes = set()
    while True:
        if (nx, ny) in walls:
            # print('Hit wall')
            break
        elif (nx, ny) in boxes:
            removing_boxes.add((nx, ny))
            adding_boxes.add((nx+dx, ny+dy))
            nx, ny = nx+dx, ny+dy
        else:
            # Move everything
            robot = (robot[0] + dx, robot[1] + dy)
            for box in removing_boxes:
                boxes.remove(box)
            for box in adding_boxes:
                boxes.add(box)
            break
    print(f'Move {move}: {robot}')
    for y in range(height):
        for x in range(width):
            if (x, y) == robot:
                print('@', end='')
            elif (x, y) in walls:
                print('#', end='')
            elif (x, y) in boxes:
                print('O', end='')
            else:
                print('.', end='')
        print()

total = 0
for box in boxes:
    total += box[1] * 100 + box[0]
print(total)

# Part 2
for move in moves:
    dx, dy = directions[move]
    nx, ny = robot[0]+dx, robot[1]+dy
    removing_boxes = set()
    adding_boxes = set()
    explore = {(nx, ny)}
    while explore:
        nx, ny = explore.pop()
        if (nx, ny) in walls:
            break
        if dx == 1 and (nx, ny) in boxes:
            removing_boxes.add((nx, ny))
            adding_boxes.add((nx+dx, ny+dy))
            explore.add((nx+2*dx, ny+dy))
        elif dx == -1 and (nx-1, ny) in boxes:
            removing_boxes.add((nx-1, ny))
            adding_boxes.add((nx+dx-1, ny+dy))
            explore.add((nx+2*dx, ny+dy))
        elif (nx, ny) in boxes:
            removing_boxes.add((nx, ny))
            adding_boxes.add((nx+dx, ny+dy))
            explore.add((nx+dx, ny+dy))
            explore.add((nx+dx+1, ny+dy))
        elif (nx-1, ny) in boxes:
            removing_boxes.add((nx-1, ny))
            adding_boxes.add((nx+dx-1, ny+dy))
            explore.add((nx+dx-1, ny+dy))
            explore.add((nx+dx, ny+dy))
    else:
        robot = (robot[0] + dx, robot[1] + dy)
        for box in removing_boxes:
            boxes.remove(box)
        for box in adding_boxes:
            boxes.add(box)

total = 0
for box in boxes:
    total += box[1] * 100 + box[0]
print(total)