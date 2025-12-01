"""
Advent of Code 2024
Day 12: Garden Groups
https://adventofcode.com/2024/day/12

Part 1:
    You are given a grid of characters where each character represents a garden plot.
    A garden is a group of same characters that are all connected to each other.
    You are to determine the total area of the garden and the total perimeter of the garden.
    :return: The sum of the area multiplied by the perimeter for each garden.
Part 2:
    Instead of the perimeter of the garden, count the number of fences surrounding each garden.
    A fence is a straight line that separates two garden plots.
    :return: The sum of the area multiplied by the number of fences for each garden.
"""
grid = []
with open('day12.txt') as f:
    for line in f:
        grid.append(line.strip())

width = len(grid[0])
height = len(grid)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

explored = set()
total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if (x, y) in explored:
            continue
        frontier = [(x, y)]
        area = 0
        perimeter = 0
        fences = set()
        while True:
            if not frontier:
                break
            nx, ny = frontier.pop()
            area += 1
            for dx, dy in directions:
                if 0 <= nx+dx < width and 0 <= ny+dy < height:
                    if grid[ny+dy][nx+dx] != c:
                        perimeter += 1
                    elif (nx+dx, ny+dy) not in explored and (nx+dx, ny+dy) not in frontier:
                        frontier.append((nx+dx, ny+dy))
                else:
                    perimeter += 1
            explored.add((nx, ny))
        total += area * perimeter
print(total)

# Part 2
explored = set()
total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if (x, y) in explored:
            continue
        frontier = [(x, y)]
        area = 0
        fence_count = 0
        fences = set()
        while True:
            if not frontier:
                break
            nx, ny = frontier.pop()
            area += 1
            for dx, dy in directions:
                if 0 <= nx+dx < width and 0 <= ny+dy < height:
                    if grid[ny+dy][nx+dx] != c:
                        fences.add((nx, ny, dx, dy))
                    elif (nx+dx, ny+dy) not in explored and (nx+dx, ny+dy) not in frontier:
                        frontier.append((nx+dx, ny+dy))
                else:
                    fences.add((nx, ny, dx, dy))
            explored.add((nx, ny))

        explored_fences = set()
        for fence in fences:
            if fence in explored_fences:
                continue
            frontier_fences = [fence]
            while True:
                if not frontier_fences:
                    break
                fx, fy, dx, dy = frontier_fences.pop()
                if (fx, fy, dx, dy) in explored_fences:
                    continue
                if (fx+dy, fy+dx, dx, dy) in fences:
                    frontier_fences.append((fx+dy, fy+dx, dx, dy))
                if (fx-dy, fy-dx, dx, dy) in fences:
                    frontier_fences.append((fx-dy, fy-dx, dx, dy))
                explored_fences.add((fx, fy, dx, dy))
            fence_count += 1
        total += area * fence_count
print(total)