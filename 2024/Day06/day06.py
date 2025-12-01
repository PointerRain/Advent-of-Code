"""
Advent of Code 2024
Day 6: Guard Gallivant
https://adventofcode.com/2024/day/6

Part 1:
    Given a grid of '#' and '.', with a starting position and direction, follow the guard's path.
    The guard will turn right if she encounters a wall.
    :return The number of distinct positions the guard will visit before leaving the mapped area.
Part 2:
    You need to get the guard stuck in a loop by adding a single new obstruction.
    :return The number of different positions you could choose for this obstruction.
"""
grid = []
with open('day06.txt') as f:
    for line in f:
        grid.append(line.strip())

gpos = None
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
gdir = 0
visited = set()

width = len(grid[0])
height = len(grid)

for y, line in enumerate(grid):
    if '^' in line:
        ogpos = (line.index('^'), y)

ogpos = gpos
ogdir = gdir

# Part 1
while True:
    visited.add(gpos)
    x, y = gpos
    dx, dy = directions[gdir]
    if y + dy < 0 or y + dy >= height or x + dx < 0 or x + dx >= width:
        break
    if grid[y + dy][x + dx] == '#':
        gdir = (gdir + 1) % 4
    else:
        gpos = (x + dx, y + dy)
    if gpos[0] < 0 or gpos[0] >= width or gpos[1] < 0 or gpos[1] >= height:
        break
print(len(visited))

# Part 2
count_loops = 0
count_prev = 0
for obsx in range(len(grid[0])):
    for obsy in range(len(grid)):
        if grid[obsy][obsx] == '#':
            continue
        visited = set()
        gpos = ogpos
        gdir = ogdir
        while True:
            if gpos not in visited:
                visited.add(gpos)
                count_prev = 0
            else:
                count_prev += 1
                if count_prev >= 5000:
                    count_loops += 1
                    break
            x, y = gpos
            dx, dy = directions[gdir]
            if y + dy < 0 or y + dy >= height or x + dx < 0 or x + dx >= width:
                break
            if grid[y + dy][x + dx] == '#' or (x + dx, y + dy) == (obsx, obsy):
                gdir = (gdir + 1) % 4
            else:
                gpos = (x + dx, y + dy)
            if gpos[0] < 0 or gpos[0] >= width or gpos[1] < 0 or gpos[1] >= height:
                break
print(count_loops)
