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
    A = [a.strip() for a in A.splitlines()]
    B = [b.strip() for b in B.splitlines()]

# Part 1
total = 0
for b in B:
    for a in A:
        start, end = a.split('-')
        if int(b) >= int(start) and int(b) <= int(end):
            total += 1
            break
print(total)

# Part 2
seen = []
for start, end in [tuple(map(int, a.split('-'))) for a in A]:
    for s, e in seen:
        if s <= start <= end <= e:
            break
        if start <= s <= e <= end:
            seen.remove((s, e))
            continue
        if start <= s <= end <= e:
            end = s - 1
        elif s <= start <= e <= end:
            start = e + 1
    else:
        seen.append((start, end))

count = 0
for s, e in seen:
    count += e - s + 1
print(count)