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
    A = [a.strip() for a in f.readlines()]
# Part 1
d = 50
count = sum((d := (d + (1 if a[0] == 'R' else -1) * int(a[1:])) % 100) == 0 for a in A)
print(count)
# Part 2
d = 50
count = sum(sum((d := (d + (1 if a[0] == 'R' else -1)) % 100) == 0 for _ in range(int(a[1:]))) for a in A)
print(count)
