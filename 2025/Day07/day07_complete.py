"""
Advent of Code 2025
day07: Laboratories
https://adventofcode.com/2025/day/7

Part 1:
    Given a map of a laboratory with starting point 'S' and branching paths indicated by '^',
    count the number of unique split points from 'S' to the bottom.
    :return: The number of unique split points.
    :rtype: int
Part 2:
    Similar to Part 1, but count the total number of distinct paths from 'S' to the bottom.
    :return: The total number of distinct paths.
    :rtype: int
"""

with open("day07.txt") as f:
    A = [a.strip() for a in f.readlines()]

start = A[0].index('S')

splitters = set()
D = {}

def count_splits(x, y):
    if (x, y) in D:
        return set(), D[(x, y)]
    string = ''.join(A[yy][x] for yy in range(y, len(A)))
    return ((L := count_splits(x - 1, y + string.index('^') + 1))[0] | (R := count_splits(x + 1, y + string.index('^') + 1))[0] | {(x, y + string.index('^'))},
            D.update({(x,y): L[1] + R[1] if '^' in string else 1}) or D[(x,y)]) if '^' in string else (set(), 1)


total_paths = count_splits(start, 0)
print(len(total_paths[0]))
print(total_paths[1])