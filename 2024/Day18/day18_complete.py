"""
Advent of Code 2024
Day 18 - RAM Run
https://adventofcode.com/2024/day/18

Part 1:
    Given a maze and a list of obstacles, find the cost of a shortest path from S to E if the first
    1024 obstacles are active.
Part 2:
    Given a maze and a list of obstacles, find the coordinates of the first obstacle that prevents
    the maze from being solved.
"""
with open('day18.txt') as f:
    bytes = [tuple(map(int, l.strip().split(','))) for l in f]

pos, length, exit = (0, 0), 70, (70, 70)
byte_count, frontier, explored = 1024, {(pos, 0)}, set()

while frontier and pos != exit:
    pos, cost = min(frontier, key=lambda x: x[1])
    frontier.remove((pos, cost))
    frontier.update({(new_pos, cost + 1) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (new_pos := (pos[0] + dx, pos[1] + dy)) not in explored and new_pos not in frontier and new_pos not in bytes[:byte_count] and 0 <= new_pos[0] <= length and 0 <= new_pos[1] <= length})
    explored.add(pos)
print(cost)

# Part 2
byte_count, path = 1024, set()

while True:
    byte_count += 1
    pos = (0,0)
    if len(path) == 0 or bytes[byte_count-1] in path:
        frontier, explored = {((0, 0), frozenset())}, set()
        while frontier and pos != exit:
            pos, path = frontier.pop()
            frontier.update({(new_pos, path | {new_pos}) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (new_pos := (pos[0] + dx, pos[1] + dy)) not in explored and new_pos not in frontier and new_pos not in bytes[:byte_count] and 0 <= new_pos[0] <= length and 0 <= new_pos[1] <= length})
            explored.add(pos)
        if pos != exit:
            break
print(','.join(map(str, bytes[byte_count - 1])))
