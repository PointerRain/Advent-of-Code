"""
Advent of Code 2024
Day 6: Guard Gallivant
https://adventofcode.com/2024/day/6

Part 1:
    Given a grid of '#' and '.', with a starting position and direction, follow the guard's path.
    The guard will turn right if she encounters a wall.
    :return The number of distinct positions the guard will visit before leaving the mapped area.
Part 2:
    You need to get the guard stuck in a loop by adding a single new obstruction.
    :return The number of different positions you could choose for this obstruction.
"""
from multiprocessing import Pool

with open('day06.txt') as f:
    grid = [line.strip() for line in f]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
width, height = len(grid[0]), len(grid)

ogpos = next((line.index('^'), y) for y, line in enumerate(grid) if '^' in line)
ogdir = 0


# Part 2
def test_for_loop(obstacle: tuple) -> bool:
    visited = set()
    gpos, gdir = ogpos, ogdir
    while True:
        if (gpos, gdir) in visited:
            return True
        visited.add((gpos, gdir))
        x, y = gpos
        dx, dy = directions[gdir]
        if not (0 <= y + dy < height and 0 <= x + dx < width):
            return False
        if grid[y + dy][x + dx] == '#' or (x + dx, y + dy) == obstacle:
            gdir = (gdir + 1) % 4
        else:
            gpos = (x + dx, y + dy)


if __name__ == '__main__':
    visited = set()
    gpos, gdir = ogpos, ogdir

    # Part 1
    while True:
        visited.add(gpos)
        x, y = gpos
        dx, dy = directions[gdir]
        if not (0 <= y + dy < height and 0 <= x + dx < width):
            break
        if grid[y + dy][x + dx] == '#':
            gdir = (gdir + 1) % 4
        else:
            gpos = (x + dx, y + dy)

    print(len(visited))

    with Pool() as pool:
        count_loops = sum(pool.map(test_for_loop, visited))

    print(count_loops)
