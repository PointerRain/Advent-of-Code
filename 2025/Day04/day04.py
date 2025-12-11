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

width = len(data[0])
height = len(data)
total = 0
for x in range(width):
    for y in range(height):
        cell = data[y][x]
        if cell == "@":
            count = 0
            if x-1 >= 0 and data[y][x - 1] == "@":
                count += 1
            if x+1 < width and data[y][x + 1] == "@":
                count += 1
            if y-1 >= 0 and data[y - 1][x] == "@":
                count += 1
            if y+1 < height and data[y + 1][x] == "@":
                count += 1
            if x-1 >= 0 and y-1 >= 0 and data[y - 1][x - 1] == "@":
                count += 1
            if x+1 < width and y-1 >= 0 and data[y - 1][x + 1] == "@":
                count += 1
            if x-1 >= 0 and y+1 < height and data[y + 1][x - 1] == "@":
                count += 1
            if x+1 < width and y+1 < height and data[y + 1][x + 1] == "@":
                count += 1
            if count < 4:
                total += 1

print(total)


width = len(data[0])
height = len(data)
total = 0
old_data = data.copy()
while True:
    for x in range(width):
        for y in range(height):
            cell = data[y][x]
            if cell == "@":
                count = 0
                if x-1 >= 0 and data[y][x - 1] == "@":
                    count += 1
                if x+1 < width and data[y][x + 1] == "@":
                    count += 1
                if y-1 >= 0 and data[y - 1][x] == "@":
                    count += 1
                if y+1 < height and data[y + 1][x] == "@":
                    count += 1
                if x-1 >= 0 and y-1 >= 0 and data[y - 1][x - 1] == "@":
                    count += 1
                if x+1 < width and y-1 >= 0 and data[y - 1][x + 1] == "@":
                    count += 1
                if x-1 >= 0 and y+1 < height and data[y + 1][x - 1] == "@":
                    count += 1
                if x+1 < width and y+1 < height and data[y + 1][x + 1] == "@":
                    count += 1
                if count < 4:
                    line = list(data[y])
                    line[x] = "."
                    data[y] = "".join(line)
                    total += 1
    if data == old_data:
        break
    old_data = data.copy()

print("\nFinal State:")
for line in data:
    print(line)
print(total)