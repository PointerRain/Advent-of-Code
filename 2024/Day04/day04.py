"""
Advent of Code 2024
Day 4:
https://adventofcode.com/2024/day/4
Part 1:
    This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
    How many times does XMAS appear?
Part 2:
    It's actually an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
    How many times does an X-MAS appear?
"""

with open('day04.txt', 'r') as file:
    lines = [line.strip() for line in file]

# Part 1
directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
count = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        for dx, dy in directions:
            x, y = i, j
            for n in range(4):
                if not (0 <= x < len(lines) and 0 <= y < len(lines[0]) and lines[x][y] == "XMAS"[n]):
                    break
                x += dx
                y += dy
            else:
                count += 1
print(count)


# Part 2
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
count = 0

for x in range(1, len(lines)-1):
    for y in range(1, len(lines[0])-1):
        cell_count = 0
        if lines[x][y] != 'A':
            continue
        for dx, dy in directions:
            if lines[x+dx][y+dy] == 'M' and lines[x-dx][y-dy] == 'S':
                cell_count += 1
        if cell_count == 2:
            count += 1
        if cell_count > 2:
            print(x, y, cell_count)
print(count)