"""
Advent of Code 2024
Day 9: Disk Fragmenter
https://adventofcode.com/2024/day/9

Part 1:
    Given a string of numbers, every second character is the size of a block of data,
    and the next character is the size of the gap between them.
    Starting from the end, move each block to the first gap.
    :return the total of the block id times the position of the block.
Part 2:
    Move each block while keeping each set of blocks together.
    :return the total of the block id times the position of the block.
"""
# Part 1
## Read the disk
disk = []
with open('day09_test.txt') as f:
    line = f.readline()
    i = 0
    pos = 0
    while i+1 < len(line):
        size = int(line[i])
        for _ in range(size):
            disk.append(i//2)
        size = int(line[i+1])
        for _ in range(size):
            disk.append('.')
        i += 2
    size = int(line[i])
    for _ in range(size):
        disk.append(i//2)
print(disk)
## Move the blocks
i = 1
while i <= len(disk):
    if i == '.':
        pass
    elif '.' in disk:
        pos = disk.index('.')
        disk[pos] = disk[len(disk)-i]
        disk[len(disk)-i] = '.'
    else:
        break
    i += 1
    continue
disk.pop(0)
print(disk)
## Count the total
total = 0
for n, i in enumerate(disk):
    if i == '.':
        break
    total += n * i
print(total)



# Part 2
## Read the disk
disk = []
with open('day09_test.txt') as f:
    line = f.readline()
    i = 0
    pos = 0
    while i+1 < len(line):
        size = int(line[i])
        disk.append((i//2, size))
        size = int(line[i+1])
        disk.append(('.', size))
        i += 2
    size = int(line[i])
    disk.append((i//2, size))
print(disk)
## Move the blocks
i = 1
while i <= len(disk):
    item = disk[len(disk)-i]
    if item[0] == '.':
        i += 1
        continue
    for n, d in enumerate(disk):
        if d[0] != '.':
            continue
        if d[1] < item[1]:
            continue
        if n > len(disk)-i:
            continue
        disk[n] = item
        disk[len(disk)-i] = ('.', item[1])
        if d[1] > item[1]:
            disk.insert(n+1, ('.', d[1] - item[1]))
        break
    else:
        pass
    i += 1
## Count the total
total = 0
pos = 0
for i in disk:
    if i[0] == '.':
        pos += i[1]
    else:
        for _ in range(i[1]):
            total += pos * i[0]
            pos += 1
print(total)