"""
Advent of Code 2024
Day 13 - Claw Contraption
https://adventofcode.com/2024/day/13

Part 1:
    Given two vectors and a target point, find the integer coefficients of the vectors that will reach the target point.
    The maximum value of the coefficients is 100.
    :return: The sum of the sum of coefficients of the vectors that reach accessible target points.
Part 2:
    Given two vectors and a much further away target point,
    find the integer coefficients of the vectors that will reach the target point.
    :return: The sum of the sum of coefficients of the vectors that reach accessible target points.
"""

import re
import numpy as np

with open('day13.txt') as f:
    games = f.read().split('\n\n')

# Part 1
total = sum((3*round((sol := np.linalg.solve(np.array([list(map(int, re.findall(r'X\+(.*),', game))), list(map(int, re.findall(r'Y\+(.*)', game)))]), np.array(list(map(int, re.findall(r'X=(.*), Y=(.*)', game)[0])))))[0]) + round(sol[1])) * all(0 <= v <=100 and abs(v - round(v)) <= 0.001 for v in sol) for game in games)
print(total)

# Part 2
total = sum((3*round((sol := np.linalg.solve(np.array([list(map(int, re.findall(r'X\+(.*),', game))), list(map(int, re.findall(r'Y\+(.*)', game)))]), np.array([t + 10000000000000 for t in map(int, re.findall(r'X=(.*), Y=(.*)', game)[0])])))[0]) + round(sol[1])) * all(abs(v - round(v)) <= 0.001 for v in sol) for game in games)
print(total)