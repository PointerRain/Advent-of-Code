"""
Advent of Code 2024
Day 1: Historian Hysteria
    https://adventofcode.com/2024/day/1
Two lists of numbers are given.

Part 1:
    Pair up the numbers and measure how far apart they are.
    Pair up the smallest number in the left list with the smallest number in the right list,
    then the second-smallest left number with the second-smallest right number, and so on.
    :return: The sum of the absolute differences between the pairs.
Part 2:
    For each number in the left list, count how many numbers in the right list are equal to it.
    :return: The sum of the numbers in the left list multiplied by the number of times they appear in the right list.
"""

with open('day01.txt') as f:
    A, B = map(sorted, map(list, zip(*[list(map(int, line.split())) for line in f])))

# Part 1
diff = sum([abs(a-b) for a, b in zip(A,B)])
print(diff)

# Part 2
total = sum([a * B.count(a) for a in A])
print(total)