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

def dist(a,b):
    return sum((x1-x2)**2 for x1, x2 in zip(a, b))

edges = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        d = dist(data[i],data[j])
        edges.append((d, i, j))
edges.sort(key=lambda x: x[0])

connections = [{i,} for i in range(len(data))]
conn_count = 0
for edge in edges:
    a = edge[1]
    b = edge[2]
    A = None
    B = None
    for conns in connections:
        if a in conns:
            A = conns
        if b in conns:
            B = conns
        if A is not None and B is not None:
            break
    if A is not None and B is not None and A != B:
        merged = A.union(B)
        connections.remove(A)
        connections.remove(B)
        connections.append(merged)
    conn_count += 1
    if conn_count == LIMIT:
        connections.sort(key=lambda a: len(a), reverse=True)
        total = 1
        for conns in connections[:3]:
            total *= len(conns)
        print(total)
    if len(connections) == 1:
        print(data[a][0] * data[b][0])
        break


