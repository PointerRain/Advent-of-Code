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
    bytes = list(tuple(map(int, l.strip().split(','))) for l in f)

start = (0,0)
length = 70

exit = (length,length)


byte_count = 1024
path = {}
frontier = {start}
explored = set()
count = 0
while frontier:
    pos = frontier.pop()
    if pos == exit:
        break
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if new_pos in explored or new_pos in frontier:
            continue
        if new_pos in bytes[:byte_count]:
            continue
        if new_pos[0] < 0 or new_pos[0] > length or new_pos[1] < 0 or new_pos[1] > length:
            continue
        frontier.add(new_pos)
        if new_pos not in path:
            path[new_pos] = pos
        count += 1
    explored.add(pos)

pos = exit
true_path = []
while True:
    true_path.append(pos)
    if pos == start:
        break
    pos = path[pos]

print(len(true_path)-1)

for y in range(length+1):
    for x in range(length+1):
        if (x,y) in true_path:
            print('O', end='')
        elif (x,y) in bytes[:byte_count]:
            print('#', end='')
        else:
            print(' ', end='')
    print('|')

# Part 2
byte_count = 2924

while True:
    frontier = {start}
    explored = set()
    path = {}
    count = 0
    while frontier:
        pos = frontier.pop()
        if pos == exit:
            break
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos in explored or new_pos in frontier:
                continue
            if new_pos in bytes[:byte_count]:
                continue
            if new_pos[0] < 0 or new_pos[0] > length or new_pos[1] < 0 or new_pos[1] > length:
                continue
            frontier.add(new_pos)
            if new_pos not in path:
                path[new_pos] = pos
            count += 1
        explored.add(pos)
    else:
        print('No path found')
        print(byte_count)
        print(bytes[byte_count-1])
        break
    byte_count += 1

for y in range(length+1):
    for x in range(length+1):
        if (x,y) in true_path:
            print('O', end='')
        elif (x,y) in bytes[:byte_count]:
            print('#', end='')
        else:
            print(' ', end='')
    print('|')