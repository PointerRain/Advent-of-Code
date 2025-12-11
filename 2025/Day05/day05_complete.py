"""
Advent of Code 2025
day05: Cafeteria
https://adventofcode.com/2025/day/5

Part 1:
    Given a list of ranges and a list of numbers, determine how many numbers fall within at least one of the ranges.
    :return: The count of numbers that fall within at least one range.
    :rtype: int
Part 2:
    Similar to Part 1, but calculate the total count of unique numbers covered by the ranges.
    :return: The total count of unique numbers covered by the ranges.
    :rtype: int
"""

with open('day05.txt') as f:
    A, B = f.read().split('\n\n')
    A = [tuple(map(int, a.strip().split('-'))) for a in A.splitlines()]
    B = map(int, [b.strip() for b in B.splitlines()])

# Part 1
total = sum(any(a[0] <= b <= a[1] for a in A) for b in B)
print(total)

# Part 2
total = sum(e - max(s, v + 1) + 1 for n, (s, e) in enumerate(sorted(A)) if e > (v := max(i[1] for i in sorted(A)[:n]) if n else -1))
print(total)