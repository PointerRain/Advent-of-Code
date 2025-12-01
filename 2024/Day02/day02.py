"""
Advent of Code 2024
Day 2:
https://adventofcode.com/2024/day/2
Many reports, one report per line.
Each report is a list of numbers called levels that are separated by spaces.
Part 1:
    A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    :return: The number of safe reports.
Part 2:
    Same rules apply as before, except if removing a single level from an unsafe report would make it safe,
    the report instead counts as safe.
    :return: The new number of safe reports.
"""

rows = []

with open('day02.txt') as f:
    for line in f:
        rows.append(list(map(int, line.strip().split())))

# Part 1
safe = 0

for row in rows:
    if sorted(row) == row or sorted(row) == row[::-1]:
        for n in range(1, len(row)):
            if abs(row[n] - row[n-1]) < 1 or abs(row[n] - row[n-1]) > 3:
                break
        else:
            safe += 1

print(safe)

# Part 2
safe = 0

for row in rows:
    for skip in range(len(row)):
        new_row = row[:skip] + row[skip+1:]
        if sorted(new_row) == new_row or sorted(new_row) == new_row[::-1]:
            for n in range(1, len(new_row)):
                if abs(new_row[n] - new_row[n-1]) < 1 or abs(new_row[n] - new_row[n-1]) > 3:
                    break
            else:
                break
    else:
        continue
    safe += 1

print(safe)
