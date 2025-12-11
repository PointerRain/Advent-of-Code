"""
Advent of Code 2025
day04: Printing Department
https://adventofcode.com/2025/day/4

Part 1:
    Given a matrix of characters, count how many "@" characters have fewer than 4 neighboring "@" characters (including diagonals).
    :return: The count of "@" characters with fewer than 4 neighboring "@" characters.
    :rtype: int
Part 2:
    Similar to Part 1, but iteratively replace "@" characters with "." if they have fewer than 4 neighboring "@" characters, until no more changes occur.
    :return: The total number of "@" characters replaced with ".".
    :rtype: int
"""

with open("day04.txt") as f:
    data = f.read().strip().split("\n")

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

# Part 1
total = sum(data[y][x] == '@' and sum(0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data) and data[y+dy][x+dx] == "@" for dx, dy in directions) < 4 for x in range(len(data[0])) for y in range(len(data)))
print(total)

# Part 2
total = 0
while True:
    changes = 0
    updated_data = data.copy()
    for y, row in enumerate(data):
        changes, updated_data[y] = changes + (v := ["x" if cell == "@" and sum(0 <= x+dx < len(row) and 0 <= y+dy < len(data) and data[y+dy][x+dx] == "@" for dx, dy in directions) < 4 else cell for x, cell in enumerate(row)]).count('x'), ''.join(v).replace('x', '.')
    if changes == 0:
        break
    data = updated_data
    total += changes
print(total)