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

# Part 1
total = 0
for a in A:
    for i in range(99, 10, -1):
        b = [c for c in a if c in str(i)]
        if str(i) in ''.join(b):
            total += i
            break
print(total)

# Part 2
total = 0
count = 0
for a in A:
    out = 0
    v = a
    for d in range(12, 0, -1):
        m = max(list(v) if d == 1 else list(v)[:-(d-1)])
        out = out * 10 + int(m)
        v = v[v.index(m) + 1:]
    count += 1
    total += out
print(total)