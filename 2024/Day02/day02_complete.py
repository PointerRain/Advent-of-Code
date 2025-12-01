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
safe = sum((row == sorted(row) or row == sorted(row, reverse=True)) and all(1 <= abs(row[i] - row[i-1]) <= 3 for i in range(1, len(row))) for row in rows)
print(safe)

# Part 2
safe = sum(any(((new_row := row[:skip] + row[skip+1:]) == sorted(new_row) or new_row == sorted(new_row, reverse=True)) and all(1 <= abs(new_row[i] - new_row[i-1]) <= 3 for i in range(1, len(new_row))) for skip in range(len(row))) for row in rows)
print(safe)
