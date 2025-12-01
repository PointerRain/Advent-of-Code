"""
Advent of Code 2024
Day 10:
https://adventofcode.com/2024/day/10

Part 1:
    Given a topographical map, find the number of positions accessible from any starting position,
    if you can move to any position that is one unit higher than the current position.
Part 2:
    Given a topographical map, find the number of trails from any starting position to any end position.
"""

grid = []
with open('day10_test.txt') as f:
    for line in f:
        grid.append(list(map(int, line.strip())))

width = len(grid[0])
height = len(grid)

total = 0

def filter_positions(positions, pos, diff=1):
    out = []
    for i in positions:
        if i[0] == pos[0] - diff:
            if abs(i[1] - pos[1]) == 1 and abs(i[2] - pos[2]) == 0:
                out.append(i)
                continue
            if abs(i[1] - pos[1]) == 0 and abs(i[2] - pos[2]) == 1:
                out.append(i)
                continue
    return out

# Part 1
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == 0:
            accessible = {(0, x, y)}
            while True:
                scount = len(accessible)
                for nx in range(width):
                    for ny in range(height):
                        pos = (grid[ny][nx], nx, ny)
                        if any(filter_positions(accessible, pos)):
                            accessible.add(pos)
                if len(accessible) == scount:
                    break
            total += sum(1 for i in accessible if i[0] == 9)
print(total)

# Part 2
total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == 0:
            accessible = [(c, x, y)]
            while True:
                if not accessible:
                    break

                v, nx, ny = accessible.pop()

                if v == 9:
                    total += 1
                    continue

                if nx+1 < width and grid[ny][nx+1] == v + 1:
                    if (v+1, nx+1, ny) not in accessible:
                        accessible.append((v+1, nx+1, ny))
                if nx-1 >= 0 and grid[ny][nx-1] == v + 1:
                    if (v+1, nx-1, ny) not in accessible:
                        accessible.append((v+1, nx-1, ny))
                if ny+1 < height and grid[ny+1][nx] == v + 1:
                    if (v+1, nx, ny+1) not in accessible:
                        accessible.append((v+1, nx, ny+1))
                if ny-1 >= 0 and grid[ny-1][nx] == v + 1:
                    if (v+1, nx, ny-1) not in accessible:
                        accessible.append((v+1, nx, ny-1))
print(total)