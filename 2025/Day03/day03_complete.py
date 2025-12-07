"""
Advent of Code 2025
day03: Lobby
https://adventofcode.com/2025/day/3

Part 1:
    Given a list of strings representing sequences of digits, for each string,
    find the largest two-digit number that can be formed by selecting digits in order from the string.
    :return: The sum of all such numbers found.
    :rtype: int
Part 2:
    Similar to Part 1, but find the largest twelve-digit number formed by selecting digits in from each string.
    :return: The sum of all such numbers found.
    :rtype: int
"""

with open('day03.txt') as f:
    A = [a.strip() for a in f.readlines()]

r = lambda s, k: int(max(s)) if k == 1 else 10**(k-1) * int(max(s[:-(k-1)])) + r(s[s.index(max(s[:-(k-1)]))+1:], k - 1)

# Part 1
total = sum(r(a, 2) for a in A)
print(total)

# Part 2
total = sum(r(a, 12) for a in A)
print(total)