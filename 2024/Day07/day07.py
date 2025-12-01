"""
Advent of Code 2024
Day 7:
https://adventofcode.com/2024/day/7

Part 1:
    Given a list of equations, missing their operators (+ or *),
    find the sum of the equations that can be true.
Part 2:
    Find the sum of the equations that can be true if concatenation is allowed.
    Equations are always evaluated left to right.
"""

equations = []
with open('day07.txt') as f:
    for line in f:
        result = int(line.strip().split(':')[0])
        eq = list(map(int, line.strip().split(':')[1].strip().split(' ')))
        equations.append((result, eq))


total = 0
for eq in equations:
    output, inputs = eq
    possibilities = [(inputs[0], str(inputs[0]))]
    for inp in inputs[1:]:
        new = []
        for (value, m) in possibilities:
            new += [(value + inp, f'{m.split("=")[0]}+ {inp} = {value} + {inp}'), (value * inp, f'{m.split("=")[0]} * {inp} = {value} * {inp}')]
        possibilities = new
    for p, m in possibilities:
        if p == output:
            total += output
            break
print(total)

total = 0
for eq in equations:
    output, inputs = eq
    possibilities = [inputs[0]]
    for inp in inputs[1:]:
        new = []
        for value in possibilities:
            new += [value + inp, value * inp, int(str(value) + str(inp))]
        possibilities = new
    if output in possibilities:
        total += output
print(total)