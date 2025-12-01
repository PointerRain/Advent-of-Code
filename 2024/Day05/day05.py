"""
Advent of Code 2024
Day 5:
https://adventofcode.com/2024/day/5

Part 1:
    Given page ordering rules and the unordered pages to produce in each update,
    Determine which updates are already in the correct order.
    :return the sum of the middle page number from those correctly-ordered updates.
Part 2:
    Find the updates which are not in the correct order.
    :return the sum middle page numbers after correctly ordering just those updates.
"""
with open('day05.txt', 'r') as file:
    orders, updates = file.read().split('\n\n')
    orders = [(int(o.split('|')[0]),int(o.split('|')[1])) for o in orders.split('\n')]
    updates = [list(map(int, u.split(','))) for u in updates.split('\n')]

total = 0
for u in updates:
    for o in orders:
        if o[1] not in u or o[0] not in u:
            continue
        if u.index(o[1]) < u.index(o[0]):
            break
    else:
        total += u[len(u)//2]
print(total)

total = 0
for u in updates:
    curr_u = u.copy()
    incorrect = False
    for _ in range(len(curr_u)):
        for o in orders:
            if o[1] not in curr_u or o[0] not in curr_u:
                continue
            if curr_u.index(o[1]) < curr_u.index(o[0]):
                curr_u.remove(o[0])
                index = curr_u.index(o[1])
                curr_u.insert(index, o[0])
                incorrect = True
    if incorrect:
        total += curr_u[len(curr_u)//2]

print(total)