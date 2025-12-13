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
        return D[(x, y)]
    count = 0
    ypos = y
    while ypos < len(A):
        if A[ypos][x] == '^':
            splitters.add((x, ypos))
            count += count_splits(x-1, ypos+1)
            count += count_splits(x+1, ypos+1)
            D[(x, y)] = count
            return count
        ypos += 1
    D[(x, y)] = 1
    return 1

total_paths = count_splits(start, 0)
print(len(splitters))
print(total_paths)