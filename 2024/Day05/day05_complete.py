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
    orders = [tuple(map(int, o.split('|'))) for o in orders.split('\n')]
    updates = [list(map(int, u.split(','))) for u in updates.split('\n')]

# Part 1
total = sum(u[len(u) // 2] * all(o[1] not in u or o[0] not in u or u.index(o[1]) >= u.index(o[0]) for o in orders) for u in updates)
print(total)

# Part 2
total = 0
for u in updates:
    incorrect = False
    for _ in u:
        for o in orders:
            if o[1] in u and o[0] in u and u.index(o[1]) < u.index(o[0]):
                a = u.insert(u.index(o[1]), u.pop(u.index(o[0])))
                incorrect = True
    total += u[len(u)//2] * incorrect
print(total)