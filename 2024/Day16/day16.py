"""
Advent of Code 2024
Day 16 - Reindeer Maze
adventofcode.com/2024/day/16

Part 1:
    Given a maze with walls, find the cost of a shortest path from S to E.
Part 2:
    Given a maze with walls, find the number of tiles that are part of all shortest paths.
"""

with open('day16.txt') as f:
    grid = [l.strip() for l in f]

walls = set()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
        elif c == 'E':
            end = (x, y)
        elif c == '#':
            walls.add((x, y))
        elif c == '.':
            pass
        else:
            print('Unknown character:', c)

width = len(grid[0])
height = len(grid)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

frontier = {(start, (1, 0), 0)}
explored = set()

# Part 1
while frontier:
    node, dir, cost = min(frontier, key=lambda x: x[2])
    frontier.remove((node, dir, cost))
    if node == end:
        print(cost)
        break
    for dx, dy in directions:
        new_node = (node[0] + dx, node[1] + dy)
        if new_node[0] < 0 or new_node[0] >= width or new_node[1] < 0 or new_node[1] >= height:
            continue
        if new_node in walls or new_node in explored:
            continue
        if dir == (dx, dy):
            new_cost = cost + 1
        elif dir == (-dx, -dy):
            continue
            new_cost = cost + 2001
        else:
            new_cost = cost + 1001
        frontier.add((new_node, (dx, dy), new_cost))
    explored.add(node)

# Part 2
frontier = {(start, (1, 0), 0, frozenset({start}))}
true_cost = 83432
paths = []

costs = {}

while frontier:
    node, dir, cost, path = frontier.pop()
    if node == end:
        if cost == true_cost:
            paths.append(path)
        continue
    if cost >= true_cost:
        continue
    if node not in costs:
        costs[node] = cost
    for dx, dy in directions:
        new_node = (node[0] + dx, node[1] + dy)
        if new_node[0] < 0 or new_node[0] >= width or new_node[1] < 0 or new_node[1] >= height:
            continue
        if new_node in walls:
            continue
        if new_node in costs and cost > costs[new_node]:
            continue
        if dir == (dx, dy):
            new_cost = cost + 1
        elif dir == (-dx, -dy):
            continue
        else:
            new_cost = cost + 1001
        frontier.add((new_node, (dx, dy), new_cost, path | {new_node}))
    explored.add(node)

print(len(set(tile for path in paths for tile in path)))
