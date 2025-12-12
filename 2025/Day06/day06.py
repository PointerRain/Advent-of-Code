"""
Advent of Code 2025
day06: Trash Compactor
https://adventofcode.com/2025/day/6

Part 1:
    Given a table of numbers and a list of operations, perform the operations column-wise and sum the results.
    :return: The sum of the results after performing the operations.
    :rtype: int
Part 2:
    Similar to Part 1, but the numbers are vertical with one digit per row.
    :return: The sum of the results after performing the operations.
    :rtype: int
"""

with open("day06.txt") as f:
    A = [a.replace('\n', '') for a in f.readlines()]

total = 0
for col in range(len([i for i in A[-1].split(' ') if i])):
    op = [i for i in A[-1].split(' ') if i][col]
    if op[0] == '+':
        summing = 0
        for r in range(len(A)-1):
            summing += int([i for i in A[r].split(' ') if i][col])
        total += summing
    elif op[0] == '*':
        product = 1
        for r in range(len(A)-1):
            product *= int([i for i in A[r].split(' ') if i][col])
        total += product
print(total)


ops = [i for i in A[-1].split(' ') if i]
op_positions = [i for i in range(len(A[-1])) if A[-1][i] != ' ']
all_rows = []
for r in range(len(A)-1):
    row = A[r]
    row_nums = []
    num = ''
    for c in range(len(row)):
        char = row[c]
        if c+1 in op_positions and num != '':
            row_nums.append(num)
            num = ''
        else:
            num += char
    if num.replace(' ', '') != '':
        row_nums.append(num)
    all_rows.append(row_nums)
total = 0
for problem in range(len(ops)):
    op = ops[problem]
    if op[0] == '*':
        count = 1
    elif op[0] == '+':
        count = 0
    problem_nums = list(row[problem] for row in all_rows)
    length = max(len(n) for n in problem_nums)
    for num in range(length):
        number = ''
        for digit in range(len(problem_nums)):
            if len(problem_nums[digit]) <= num:
                continue
            number += str(problem_nums[digit][num])
        if op[0] == '+':
            count += int(number)
        elif op[0] == '*':
            count *= int(number)
    total += count
print(total)