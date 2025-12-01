"""
Advent of Code 2024
day01: Historian Hysteria
https://adventofcode.com/2024/day/1
Two lists of numbers are given.
Part 1:
    Pair up the numbers and measure how far apart they are.
    Pair up the smallest number in the left list with the smallest number in the right list,
    then the second-smallest left number with the second-smallest right number, and so on.
    :return: The sum of the absolute differences between the pairs.
    :rtype: int
Part 2:
    For each number in the left list, count how many numbers in the right list are equal to it.
    :return: The sum of the numbers in the left list multiplied by the number of times they appear in the right list.
    :rtype: int
"""

A, B = [], []
with open('day01.txt') as f:
    for line in f:
        a, b = map(int, line.split())
        A.append(a)
        B.append(b)
A.sort()
B.sort()
# Part 1
diff = [abs(a-b) for a, b in zip(A,B)]
print(sum(diff))
# Part 2
total = 0
for a in A:
    sim = 0
    for b in B:
        if a == b:
            sim += 1
        if a < b:
            break
    total += a * sim
print(total)
