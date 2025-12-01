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
        for char in characters:
            for nx in range(width):
                for ny in range(height):
                    if nx == ox and ny == oy:
                        continue
                    if grid[ny][nx] == char:
                        dx, dy = nx - ox, ny - oy
                        x, y = nx, ny
                        while True:
                            x += dx
                            y += dy
                            if x < 0 or x >= width or y < 0 or y >= height:
                                break
                            if grid[y][x] == char:
                                count.add((ox, oy))

print(len(count))

# Part 2
count = set()
for oy, line in enumerate(grid):
    for ox, c in enumerate(line):
        for char in characters:
            if char != c:
                continue
            for nx in range(width):
                for ny in range(height):
                    if nx == ox and ny == oy:
                        continue
                    if grid[ny][nx] == char:
                        dx, dy = nx - ox, ny - oy
                        lcd = gcd(dx, dy)
                        dx //= lcd
                        dy //= lcd
                        x, y = ox, oy
                        while True:
                            x += dx
                            y += dy
                            if x < 0 or x >= width or y < 0 or y >= height:
                                break
                            count.add((x, y))
print(len(count))