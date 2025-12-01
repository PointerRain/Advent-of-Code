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
    regA = int(re.findall(r'A: (.*)', regs)[0])
    regB = int(re.findall(r'B: (.*)', regs)[0])
    regC = int(re.findall(r'C: (.*)', regs)[0])
    prog = list(map(int, prog.split(' ')[1].split(',')))

print(regA, regB, regC)
print(prog)

def combo_operand(op, A, B, C):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C
    else:
        print('Unknown opperand:', op)

# Part 1
pointer = 0
A = regA
B = regB
C = regC
while True:
    if pointer >= len(prog):
        break
    instr = prog[pointer]
    opperand = prog[pointer + 1]
    if instr == 0:
        A = A // 2**combo_operand(opperand, A, B, C)
    elif instr == 1:
        B = B ^ opperand
    elif instr == 2:
        B = combo_operand(opperand, A, B, C) % 8
    elif instr == 3:
        if A == 0:
            pass
        else:
            pointer = opperand - 2
    elif instr == 4:
        B = B ^ C
    elif instr == 5:
        print(combo_operand(opperand, A, B, C) % 8, end=',')
    elif instr == 6:
        B = A // 2**combo_operand(opperand, A, B, C)
    elif instr == 7:
        C = A // 2**combo_operand(opperand, A, B, C)
    pointer += 2
print()

# Part 2
i = 0
while True:
    pointer = 0
    A = 247839653009590 + i
    B = regB
    C = regC
    output = []
    print(A, end=' ')
    while True:
        if pointer >= len(prog):
            break
        instr = prog[pointer]
        opperand = prog[pointer + 1]
        if instr == 0:
            A = A // 2**combo_operand(opperand, A, B, C)
        elif instr == 1:
            B = B ^ opperand
        elif instr == 2:
            B = combo_operand(opperand, A, B, C) % 8
        elif instr == 3:
            if A == 0:
                pass
            else:
                pointer = opperand - 2
        elif instr == 4:
            B = B ^ C
        elif instr == 5:
            output.append(combo_operand(opperand, A, B, C) % 8)
            pass
        elif instr == 6:
            B = A // 2**combo_operand(opperand, A, B, C)
        elif instr == 7:
            C = A // 2**combo_operand(opperand, A, B, C)
        else:
            print('Unknown instruction:', instr)
        pointer += 2
    print(output)
    if output == prog:
        print(247839653009590 + i)
        break
    if len(output) < len(prog):
        print('Too short')
        i += 10000000
    elif len(output) > len(prog):
        print('Too long')
    # elif output[-2:] != prog[-2:]:
    #     # print('-2', end=' ')
    #     i += 100000000
    # elif output[-4:] != prog[-4:]:
    #     # print('-4', end=' ')
    #     i += 10000000
    # elif output[-5:] != prog[-5:]:
    #     # print('-5', end=' ')
    #     i += 100000
    # elif output[-6:] != prog[-6:]:
    #     # print('-6', end=' ')
    #     i += 10000
    # elif output[-7:] != prog[-7:]:
    #     # print('-7', end=' ')
    #     i += 1000
    if output[-9:] != prog[-9:]:
        print('-9', end=' ')
        i += 100
    i += 1