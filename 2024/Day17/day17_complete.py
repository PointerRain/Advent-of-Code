"""
Advent of Code 2024
Day 17 - Chronospatial Computer
https://adventofcode.com/2024/day/17

Part 1:
    Given a program for a simple computer with 8 instructions and three registers,
    simulate the program and print the output.
Part 2:
    Find the smallest initial value for register A that will produce the same output as the program.
"""
import re

with open('day17.txt') as f:
    regs, prog = f.read().split('\n\n')
    regA, regB, regC = (int(re.findall(r + r': (.*)', regs)[0]) for r in 'ABC')
    prog = list(map(int, prog.split(' ')[1].split(',')))

# Part 1
pointer = 0
A, B, C = regA, regB, regC
while pointer < len(prog):
    A = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 0 else A
    B = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 6 else B
    C = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 7 else C
    B = B ^ (prog[pointer+1] if prog[pointer] == 1 else C) if prog[pointer] in [1,4] else {4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) % 8 if prog[pointer] == 2 else B
    print({4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) % 8, end=',') if prog[pointer] == 5 else None
    pointer = prog[pointer+1] if prog[pointer] == 3 and A != 0 else pointer + 2
print()

# Part 2
i = 0
output = []
while output != prog:
    pointer = 0
    A, B, C = i, regB, regC
    output = []
    while pointer < len(prog):
        A = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 0 else A
        B = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 6 else B
        C = A // 2**{4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) if prog[pointer] == 7 else C
        B = B ^ (prog[pointer+1] if prog[pointer] == 1 else C) if prog[pointer] in [1,4] else {4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) % 8 if prog[pointer] == 2 else B
        output.append({4: A, 5: B, 6: C}.get(prog[pointer+1], prog[pointer+1]) % 8) if prog[pointer] == 5 else None
        pointer = prog[pointer+1] if prog[pointer] == 3 and A != 0 else pointer + 2
    i += next((10**(13+x) for x in range(-1, -13, -1) if output[x] != prog[x]), 1)
print(i-1)