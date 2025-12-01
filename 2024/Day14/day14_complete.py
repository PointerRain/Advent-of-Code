"""
Advent of Code 2024
Day 14 - Restroom Redoubt
https://adventofcode.com/2024/day/14

Part 1:
    Given a list of robots with positions and velocities,
    find the number of robots in each quadrant after 100 seconds.
    :return: The product of the number of robots in each quadrant.
Part 2:
    Given a list of robots with positions and velocities,
    find the time at which the robots will form a tree shape.
    :return: The time at which the robots will form a tree shape.
"""

import re

robots = []
with open('day14.txt') as f:
    for line in f:
        ax, ay = map(int, re.findall(r'p=(.*),(.*) ', line)[0])
        bx, by = map(int, re.findall(r'v=(.*),(.*)', line)[0])
        robots.append([ax, ay, bx, by])

width = 101
height = 103

# Part 1
total = (quads := list(map(len, map(list, [filter(l, [((r[0] + 100*r[2]) % width, (r[1] + 100*r[3]) % height) for r in robots]) for l in (lambda p: p[0] < width//2 and p[1] < height//2, lambda p: p[0] > width//2 and p[1] < height//2, lambda p: p[0] < width//2 and p[1] > height//2, lambda p: p[0] > width//2 and p[1] > height//2)]))))[0] * quads[1] * quads[2] * quads[3]
print(total)

# Part 2
for i in range(10000):
    if max([[(rob[0] + i * rob[2]) % width for rob in robots].count(x) for x in range(width)]) >= 23 and max([[(rob[1] + i * rob[3]) % height for rob in robots].count(y) for y in range(height)]) >= 20:
        print(i)
        break