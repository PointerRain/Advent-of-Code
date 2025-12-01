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
moves = moves.replace('\n', '')

# Part 1
robot = next((line.find('@'), y) for y, line in enumerate(grid) if '@' in line)
walls = {(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == '#'}
boxes = {(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == 'O'}

for move in moves:
    dx, dy = {'<': (-1, 0),'>': (1, 0),'^': (0, -1),'v': (0, 1)}[move]
    moving_boxes = set()
    explore = {(robot[0]+dx, robot[1]+dy)}
    while explore and (box := explore.pop()) not in walls:
        box not in boxes or moving_boxes.add(box) or explore.update({(box[0]+dx, box[1]+dy)})
    box in walls or boxes.difference_update(moving_boxes) or boxes.update((box[0]+dx, box[1]+dy) for box in moving_boxes)
    robot = (robot[0] + dx, robot[1] + dy) if box not in walls else robot
total = sum(box[1] * 100 + box[0] for box in boxes)
print(total)

# Part 2
robot = next((2*line.find('@'), y) for y, line in enumerate(grid) if '@' in line)
walls = {(2*x + i, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == '#' for i in range(2)}
boxes = {(2*x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == 'O'}

for move in moves:
    dx, dy = {'<': (-1, 0),'>': (1, 0),'^': (0, -1),'v': (0, 1)}[move]
    moving_boxes = set()
    explore = {(robot[0]+dx, robot[1]+dy)}
    while explore and (box := explore.pop()) not in walls:
        box not in boxes or moving_boxes.add(box) or explore.update({(box[0]+2*dx, box[1]+dy)} if dx else {(box[0]+dx, box[1]+dy), (box[0]+dx+1, box[1]+dy)})
        (box[0]-1, box[1]) in boxes and not moving_boxes.add((box[0]-1, box[1])) and explore.update({(box[0]+2*dx, box[1]+dy)} if dx else {(box[0]+dx, box[1]+dy), (box[0]+dx-1, box[1]+dy)})
    box in walls or boxes.difference_update(moving_boxes) or boxes.update((box[0]+dx, box[1]+dy) for box in moving_boxes)
    robot = (robot[0] + dx, robot[1] + dy) if box not in walls else robot
total = sum(box[1] * 100 + box[0] for box in boxes)
print(total)