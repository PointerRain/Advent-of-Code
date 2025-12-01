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
with open('day12.txt') as f:
    grid = [line.strip() for line in f]

explored = set()
total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        frontier = [(x, y)] if (x, y) not in explored else []
        area = 0
        perimeter = 0
        while frontier:
            nx, ny = frontier.pop()
            area += 1
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                perimeter += (c := (0 <= nx + dx < len(grid[0]) and 0 <= ny + dy < len(grid))) and grid[ny + dy][nx + dx] != char or not c
                c and grid[ny + dy][nx + dx] == char and (nx + dx, ny + dy) not in explored and (nx + dx, ny + dy) not in frontier and frontier.append((nx + dx, ny + dy))
            explored.add((nx, ny))
        total += area * perimeter
print(total)

# Part 2
explored = set()
total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        frontier = [(x, y)] if (x, y) not in explored else []
        area = 0
        fences = set()
        while frontier:
            nx, ny = frontier.pop()
            area += 1
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                (w := 0 <= nx + dx < len(grid[0]) and 0 <= ny + dy < len(grid)) and (c := grid[ny + dy][nx + dx] != char) and fences.add((nx, ny, dx, dy))
                w and not c and (nx + dx, ny + dy) not in explored | set(frontier) and frontier.append((nx + dx, ny + dy))
                not w and fences.add((nx, ny, dx, dy))
            explored.add((nx, ny))
        explored_fences = set()
        for fence in fences:
            frontier = [fence] if (c := fence not in explored_fences) else []
            while frontier:
                (v := frontier.pop()) not in explored_fences and (d:=(v[0] + v[3], v[1] + v[2], v[2], v[3])) in fences and frontier.append(d)
                v not in explored_fences and (d:=(v[0] - v[3], v[1] - v[2], v[2], v[3])) in fences and frontier.append((v[0] - v[3], v[1] - v[2], v[2], v[3]))
                explored_fences.add(v)
            total += area * c
print(total)