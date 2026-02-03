"""
Advent of Code 2025
day09:
https://adventofcode.com/2025/day/9

Part 1:
    Given a list of points, find the maximum area of a rectangle defined by any two points.
    :return: The area of the rectangle
    :rtype: int
Part 2:
    The points define a polygon. Find the maximum area of a rectangle defined by any two points that
    lies entirely within the polygon.
    :return: The area of the rectangle within the polygon
    :rtype: int
"""

with open("day09.txt") as f:
    data = [tuple(map(int, a.split(','))) for a in f.readlines()]

max_A = 0
for a in data:
    for b in data:
        if a == b:
            continue

        A = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        max_A = max(max_A, A)
print(max_A)

max_A = 0
for a in data:
    for b in data:
        for n, c in enumerate(data):
            d = data[(n + 1) % len(data)]
            if len({c, d, a, b}) < 4:
                continue
            if max(c[0], d[0]) <= min(a[0], b[0]):
                continue
            if max(c[1], d[1]) <= min(a[1], b[1]):
                continue
            if min(c[0], d[0]) >= max(a[0], b[0]):
                continue
            if min(c[1], d[1]) >= max(a[1], b[1]):
                continue
            break
        else:
            A = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            max_A = max(A, max_A)

print(max_A)