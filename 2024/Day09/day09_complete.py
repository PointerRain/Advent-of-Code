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
disk = []
with open('day09_test.txt') as f:
    line = f.readline()
    for i in range(0, len(line) - 1, 2):
        disk.extend([i // 2] * int(line[i]) + ['.'] * int(line[i + 1]))
    disk.extend([len(line) // 2] * int(line[len(line)-1]))

for i in reversed(range(len(disk))):
    disk[disk.index('.')], disk[i] = disk[i], '.'
total = sum((n-1) * i for n, i in enumerate(disk) if i != '.')
print(total)

# Part 2
disk = []
with open('day09_test.txt') as f:
    line = f.readline()
    for i in range(0, len(line) - 1, 2):
        disk.extend([(i//2, int(line[i])), ('.', int(line[i+1]))])
    disk.append((len(line)//2, int(line[len(line)-1])))
i = 1
while i <= len(disk):
    item = disk[-i]
    for n, d in enumerate(disk):
        if item[0] == '.' or d[0] != '.' or d[1] < item[1] or n > len(disk)-i:
            continue
        disk[n], disk[-i] = item, ('.', item[1])
        if d[1] > item[1]:
            disk.insert(n + 1, ('.', d[1] - item[1]))
        break
    i += 1
total = 0
pos = 0
for i in disk:
    if i[0] != '.':
        total += sum(n * i[0] for n in range(pos, pos+i[1]))
    pos += i[1]
print(total)