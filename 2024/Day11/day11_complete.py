"""
Advent of Code 2024
Day 11: Plutonian Pebbles
https://adventofcode.com/2024/day/11

Part 1:
    You are given a list of integers. You are to perform the following operation 25 times:
    - If the integer is 0, replace it with 1.
    - If the integer has an even number of digits, split it into two integers of equal length.
    - Otherwise, multiply the integer by 2024.
    :return: The length of the list after 25 operations.
Part 2:
    :return: The sum of the values in the list after 75 operations.
"""
from collections import defaultdict

with open('day11_test.txt') as f:
    onums = list(map(int, f.readline().split(' ')))

# Part 1
nums = {i: onums.count(i) for i in onums}
for _ in range(25):
    new_nums = defaultdict(int)
    for v, n in nums.items():
        if v == 0:
            new_nums[1] += n
        elif len(str(v)) % 2 == 0:
            new_nums[int(str(v)[:len(str(v))//2])] += n
            new_nums[int(str(v)[len(str(v))//2:])] += n
        else:
            new_nums[v*2024] += n
    nums = new_nums
print(sum(n for v, n in nums.items()))

# Part 2
nums = {i: onums.count(i) for i in onums}
for _ in range(75):
    new_nums = defaultdict(int)
    for v, n in nums.items():
        if v == 0:
            new_nums[1] += n
        elif len(str(v)) % 2 == 0:
            new_nums[int(str(v)[:len(str(v))//2])] += n
            new_nums[int(str(v)[len(str(v))//2:])] += n
        else:
            new_nums[v*2024] += n
    nums = new_nums
print(sum(n for v, n in nums.items()))