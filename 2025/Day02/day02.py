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
    A = f.read()
    A = A.strip().split(',')

total = 0
for a in A:
    start, end = a.split('-')
    for i in range(int(start), int(end)+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                total += i
print(total)

IDs = set()
for a in A:
    start, end = a.split('-')
    for i in range(int(start), int(end)+1):
        for q in range(2, 22):
            if len(str(i)) % q == 0:
                section_size = len(str(i)) // q
                first = str(i)[:len(str(i))//q]
                for s in range(q):
                    if str(i)[s*section_size:(s+1)*section_size] != first:
                        break
                else:
                    IDs.add(i)
print(sum(IDs))