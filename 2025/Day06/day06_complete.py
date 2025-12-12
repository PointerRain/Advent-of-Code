"""
Advent of Code 2025
day06: Trash Compactor
https://adventofcode.com/2025/day/6

Part 1:
    Given a table of numbers and a list of operations, perform the operations column-wise and sum the results.
    :return: The sum of the results after performing the operations.
    :rtype: int
Part 2:
    Similar to Part 1, but the numbers are vertical with one digit per row.
    :return: The sum of the results after performing the operations.
    :rtype: int
"""
from functools import reduce

with open("day06.txt") as f:
    A = [a.replace('\n', '') for a in f.readlines()]
    ops = [i for i in A[-1].split(' ') if i]

# Part 1
total = sum(reduce(int.__mul__ if op == '*' else int.__add__, (int([i for i in row.split(' ') if i][col]) for row in A[:-1]), op == '*') for col, op in enumerate(ops))
print(total)

# Part 2
all_rows = [''.join('|' if c+1 in [i for i, char in enumerate(A[-1]) if char != ' '] else char for c, char in enumerate(row)).split('|') for row in A[:-1]]
total = sum(reduce(int.__mul__ if op == '*' else int.__add__,
                   (int(''.join(digit[num] for digit in (row[problem] for row in all_rows) if len(digit) > num)) for num in range(max(len(digit) for digit in (row[problem] for row in all_rows)))),
                   op == '*') for problem, op in enumerate(ops))
print(total)