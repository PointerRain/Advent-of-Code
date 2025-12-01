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

with open('day11.txt') as f:
    line = f.readline()
    nums = list(map(int, line.split(' ')))

print(nums)

# Part 1
def blink1(nums):
    new_nums = []
    for i in nums:
        if i == 0:
            new_nums.append(1)
        elif len(str(i)) % 2 == 0:
            a = int(str(i)[:len(str(i))//2])
            b = int(str(i)[len(str(i))//2:])
            new_nums.append(a)
            new_nums.append(b)
        else:
            new_nums.append(i*2024)
    return new_nums

new_nums = nums
for i in range(25):
    new_nums = blink1(new_nums)
print(len(new_nums))


# Part 2
new_nums = {i: nums.count(i) for i in nums}
print(new_nums)
def blink2(nums):
    new_nums = defaultdict(int)
    for v, n in nums.items():
        if v == 0:
            new_nums[1] += n
        elif len(str(v)) % 2 == 0:
            a = int(str(v)[:len(str(v))//2])
            b = int(str(v)[len(str(v))//2:])
            new_nums[a] += n
            new_nums[b] += n
        else:
            new_nums[v*2024] += n
    return new_nums

for i in range(75):
    new_nums = blink2(new_nums)
print(sum(v for k, v in new_nums.items()))