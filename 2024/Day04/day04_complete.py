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
count = 0
for x in range(len(lines)):
    for y in range(len(lines[0])):
        count += sum(
            all(0 <= x+n*dx < len(lines) and 0 <= y+n*dy < len(lines[0]) and lines[x+n*dx][y+n*dy] == "XMAS"[n] for n in range(4))
            for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)])
print(count)

# Part 2
count = 0
for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[0]) - 1):
        count += (lines[x][y] == 'A' and sum(
            lines[x + dx][y + dy] == 'M' and lines[x - dx][y - dy] == 'S'
            for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        ) == 2)
print(count)