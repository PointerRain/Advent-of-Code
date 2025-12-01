"""
Advent of Code 2025
day01: Secret Entrance
https://adventofcode.com/2025/day/1

Part 1:
    You are given a list of instructions to move left or right a circular dial with
    The dial has 100 positions (0-99) and starts at position 50.
    Count how many times the dial lands on position 0 after executing all instructions.
    :return: The count of times the dial lands on position 0.
    :rtype: int
Part 2:
    Similar to Part 1, but count whenever the dial passes over position 0 during the movement.
    :return: The count of times the dial passes over position 0.
    :rtype: int
"""

with open('day01.txt') as f:
    A = [f.readlines()]
    A = [a.strip() for a in A[0]]

# Part 1
d = 50
count = 0
for a in A:
    direction = a[0]
    distance = int(a[1:])
    if direction == 'L':
        d -= distance
    elif direction == 'R':
        d += distance
    d = d % 100
    if d == 0:
        count += 1
print(count)

# Part 2
d = 50
count = 0
for a in A:
    direction = a[0]
    distance = int(a[1:])
    for _ in range(distance):
        if direction == 'L':
            d -= 1
        elif direction == 'R':
            d += 1
        d = d % 100
        if d == 0:
            count += 1
print(count)