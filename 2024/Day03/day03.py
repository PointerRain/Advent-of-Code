"""
Advent of Code 2024
Day 3:
https://adventofcode.com/2024/day/3
Part 1:

Part 2:

"""
import re

rows = []
with open('day03.txt') as f:
    for line in f:
        rows.append(line)

# Part 1
numbers = [re.findall(r'mul\((\d+),(\d+)\)', row) for row in rows]
total = 0
for line in numbers:
    for pair in line:
        total += int(pair[0]) * int(pair[1])
print(total)

# Part 2
def find_ops(row):
    return re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", row)


lines = [find_ops(row) for row in rows]
total = 0
enabled = True

for line in lines:
    for op in (top[0] or top[1] or top[2] for top in line):
        if op.startswith('mul') and enabled:
            total += int(op[4:op.index(',')]) * int(op[op.index(',')+1:-1])
        elif op == "do()":
            enabled = True
        elif op == "don't()":
            enabled = False

print(total)