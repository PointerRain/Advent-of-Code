"""
Advent of Code 2025
day02: Gift Shop
https://adventofcode.com/2025/day/2

Part 1:
    You are given a list of interval ranges.
    For each range, find all numbers that are some number repeated twice.
    :return: The sum of all such numbers found.
    :rtype: int
Part 2:
    Similar to Part 1, but find numbers that are some number repeated any number of times.
    :return: The sum of all such numbers found.
    :rtype: int
"""

with open('day02.txt') as f:
    A = f.read().strip().split(',')

# Part 1
total = sum(sum(n * (n // (10**(len(str(n))//2)) == n % (10**(len(str(n))//2))) for n in range(*map(int, a.split('-')))) for a in A)
print(total)

# Part 2
total = sum(sum(n * any([((n//(10**d)) + 10**(len(str(n))-d) * (n % (10**d)) == n) for d in range(1, len(str(n))//2 + 1)]) for n in range(*map(int, a.split('-')))) for a in A)
print(total)