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

start = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'S')
end = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'E')
walls = {(x,y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == '#'}

frontier = {(start, (1, 0), 0)}
pos = start
explored = set()

# Part 1
while frontier and pos != end:
    pos, dir, true_cost = min(frontier, key=lambda x: x[2])
    frontier.remove((pos, dir, true_cost))
    frontier.update((new_pos, (dx, dy), true_cost + (1 if dir == (dx, dy) else 1001)) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (new_pos := (pos[0] + dx, pos[1] + dy)) not in walls and new_pos not in explored)
    explored.add(pos)
print(true_cost)

# Part 2
frontier = {(start, (1, 0), 0, frozenset({start}))}
costs = {}
paths = []

while frontier:
    pos, dir, cost, path = frontier.pop()
    if pos == end and cost == true_cost:
            paths.append(path)
    if cost >= true_cost or cost > costs.get(pos, float('inf')) or pos == end:
        continue
    costs[pos] = costs.get(pos, cost)
    frontier.update((new_pos, (dx, dy), cost + (1 if dir == (dx, dy) else 1001), path | {new_pos}) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (new_pos := (pos[0] + dx, pos[1] + dy)) not in walls and dir != (-dx, -dy))

print(len(set(tile for path in paths for tile in path)))