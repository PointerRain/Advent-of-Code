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
from collections import defaultdict

robots = []
with open('day14.txt') as f:
    for line in f:
        ax, ay = map(int, re.findall(r'p=(.*),(.*) ', line)[0])
        bx, by = map(int, re.findall(r'v=(.*),(.*)', line)[0])
        robots.append([ax, ay, bx, by])

width = 11
height = 7

width = 101
height = 103

quads = [0,0,0,0]

# Part 1
for rob in robots:
    x,y = ((rob[0] + 100*rob[2]) % width, (rob[1] + 100*rob[3]) % height)
    if x < width//2 and y < height//2:
        quads[0] += 1
    elif x > width//2 and y < height//2:
        quads[1] += 1
    elif x > width//2 and y > height//2:
        quads[2] += 1
    elif x < width//2 and y > height//2:
        quads[3] += 1
total = quads[0] * quads[1] * quads[2] * quads[3]
print(total)

# Part 2
for i in range(10000000):
    pos = set()
    cols = defaultdict(int)
    rows = defaultdict(int)
    for rob in robots:
        pos.add(((rob[0] + i * rob[2]) % width, (rob[1] + i* rob[3]) % height))
        cols[(rob[0] + i * rob[2]) % width] += 1
        rows[(rob[1] + i * rob[3]) % height] += 1
    third_col = sorted(cols.values(), reverse=True)[2] if len(cols) >= 3 else None
    third_row = sorted(rows.values(), reverse=True)[2] if len(rows) >= 3 else None
    if third_col >= 23:
        if third_row >= 20:
            print(i)
            for y in range(height//2):
                for x in range(width):
                    if (x,y) in pos:
                        print('#', end='')
                    else:
                        print(' ', end='')
                print('|',end='')
                for x in range(width):
                    if (x,y+height//2) in pos:
                        print('#', end='')
                    else:
                        print(' ', end='')
                print('|')
            input()