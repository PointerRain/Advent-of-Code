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

with open('day13_test.txt') as f:
    games = f.read().split('\n\n')

total = 0
for game in games:
    game = game.split('\n')
    ax, ay = map(int, re.findall(r'X\+(.*), Y\+(.*)', game[0])[0])
    bx, by = map(int, re.findall(r'X\+(.*), Y\+(.*)', game[1])[0])
    target = re.findall(r'X=(.*), Y=(.*)', game[2])[0]
    for a in range(0, 100):
        for b in range(0, 100):
            if ax*a + bx*b == int(target[0]) and ay*a + by*b == int(target[1]):
                total += 3*a + b
                break
print(total)

import numpy as np

total = 0
for game in games:
    game = game.split('\n')
    ax, ay = map(int, re.findall(r'X\+(.*), Y\+(.*)', game[0])[0])
    bx, by = map(int, re.findall(r'X\+(.*), Y\+(.*)', game[1])[0])
    target = re.findall(r'X=(.*), Y=(.*)', game[2])[0]
    d = 10000000000000
    A = np.array([[ax, bx], [ay, by]])
    B = np.array([d + int(target[0]), d + int(target[1])])
    a, b = np.linalg.solve(A, B)
    if a >= 0 and b >= 0:
        if abs(a - round(a)) <= 0.001 and abs(b - round(b)) <= 0.001:
            total += 3*round(a) + round(b)
print(total)