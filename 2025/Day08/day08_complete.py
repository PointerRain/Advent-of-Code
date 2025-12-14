"""
Advent of Code 2025
day08: Playground
https://adventofcode.com/2025/day/8

Part 1:
    Given a list of points, connect them based on the shortest 1000 edges.
    :return: The product of the sizes of the three largest connected components after 1000 connections.
    :rtype: int
Part 2:
    Continue connecting points until all are connected.
    :return: The product of the x-coordinates of the last two points connected.
    :rtype: int
"""

LIMIT = 1000

with open("day08.txt") as f:
    data = [tuple(map(int, a.split(','))) for a in f.readlines()]

conns, count = [{i,} for i in range(len(data))], 0
for _, a, b in sorted([(sum((x1-x2)**2 for x1, x2 in zip(data[i], data[j])), i, j) for i in range(len(data)) for j in range(i+1, len(data))], key=lambda x: x[0]):
    conns.remove(A := (c for c in conns if a in c).__next__())
    (B := (c for c in conns if b in c).__next__() if any(b in c for c in conns) else set()) in conns and conns.remove(B)
    conns.append(A | B)
    (count := count + 1) == LIMIT and print((conn := sorted(map(len, conns), reverse=True))[0] * conn[1] * conn[2]) or len(conns) == 1 and print(data[a][0] * data[b][0]) or len(conns) == 1
    if len(conns) == 1:
        break