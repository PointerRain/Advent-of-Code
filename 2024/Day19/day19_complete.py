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
    test_messages = {test_message := message}
    while test_messages and test_message:
        test_message = test_messages.pop()
        test_messages.update({test_message[len(towel):] for towel in towels if test_message.startswith(towel)})
    count += test_message == ''
print(count)

total = 0
for message in messages:
    test_messages = {message: 1}
    while test_messages:
        test_message = max(test_messages, key=len)
        count = test_messages.pop(test_message)
        total += count * (test_message == '')
        test_messages.update({test_message[n:]: test_messages.get(test_message[n:], 0) + count for n in range(1, len(test_message)+1) if test_message[:n] in towels})
print(total)