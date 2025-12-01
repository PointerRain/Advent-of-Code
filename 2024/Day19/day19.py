"""
Advent of Code 2024
Day 19 - Linen Layout
https://adventofcode.com/2024/day/19

Part 1:
    Given a list of towels and a list of messages, find the number of messages that can be made.
Part 2:
    Given a list of towels and a list of messages, find the total number of arrangements
    for all messages.
"""
with open("day19.txt") as f:
    data = f.read().split("\n\n")
    towels = data[0].strip().split(', ')
    messages = data[1].splitlines()

count = 0
for message in messages:
    test_messages = {message}
    while test_messages:
        test_message = test_messages.pop()
        if test_message == '':
            count += 1
            break
        new_messages = set()
        for towel in towels:
            if test_message.startswith(towel):
                new_messages.add(test_message[len(towel):])
        test_messages.update(new_messages)
print(count)

total = 0
for message in messages:
    test_messages = {message: 1}
    while test_messages:
        test_message = max(test_messages, key=len)
        count = test_messages.pop(test_message)
        if test_message == '':
            total = total + count
        new_messages = {}
        for n in range(1, len(test_message)+1):
            if test_message[:n] in towels:
                new_messages[test_message[n:]] = test_messages.get(test_message[n:], 0) + count
        test_messages.update(new_messages)
print(total)