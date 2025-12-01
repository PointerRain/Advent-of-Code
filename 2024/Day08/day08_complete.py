"""
Advent of Code 2024
Day 8: Resonant Collinearity
https://adventofcode.com/2024/day/8

Part 1:
    Given a grid of characters, find the number of points that are collinear with another point of the same character,
    if the distance to one of the points is double the distance to the other point.
Part 2:
    Given a grid of characters, find the number of points that are collinear with another point of the same character.
"""
from math import gcd

grid = []
with open('day08.txt') as f:
    for line in f:
        grid.append(line.strip())

width = len(grid[0])
height = len(grid)
characters = set()
for line in grid:
    characters |= set(line)
characters -= {'.'}

# Part 1
count = set()
for oy, line in enumerate(grid):
    for ox, c in enumerate(line):
        if c not in characters:
            continue
        for nx in range(width):
            for ny in range(height):
                if grid[ny][nx] != c or (nx, ny) == (ox, oy):
                    continue
                dx, dy = nx - ox, ny - oy
                x, y = nx + dx, ny + dy
                # print(f"{(ox, oy), (nx, ny), (x, y)}, {grid[y][x]}")
                if 0 <= x < width and 0 <= y < height and grid[y][x] == c:
                    count.add((x, y))
                x, y = ox - dx, oy - dy
                if 0 <= x < width and 0 <= y < height and grid[y][x] == c:
                    count.add((x, y))
print(len(count))

# Part 2
count = set()
for oy, line in enumerate(grid):
    for ox, c in enumerate(line):
        if c not in characters:
            continue
        for nx in range(width):
            for ny in range(height):
                if grid[ny][nx] != c or (nx, ny) == (ox, oy):
                    continue
                dx, dy = nx - ox, ny - oy
                dx, dy = dx // gcd(dx, dy), dy // gcd(dx, dy)
                x, y = ox, oy
                while 0 <= x < width and 0 <= y < height:
                    x += dx
                    y += dy
                    if x < 0 or x >= width or y < 0 or y >= height:
                        break
                    count.add((x, y))
print(len(count))