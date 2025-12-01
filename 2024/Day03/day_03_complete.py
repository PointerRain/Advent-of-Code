"""
Advent of Code 2024
Day 3:
https://adventofcode.com/2024/day/3
Part 1:

Part 2:

"""
import re

file = open('day03.txt', 'r').read().strip()

# Part 1
total = sum(int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', file))
print(total)

# Part 2
total = 0
enabled = True

for mul_op, do_op, dont_op in re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", file):
    if mul_op and enabled:
        total += int(mul_op[4:mul_op.index(',')]) * int(mul_op[mul_op.index(',')+1:-1])
    elif do_op:
        enabled = True
    elif dont_op:
        enabled = False

print(total)