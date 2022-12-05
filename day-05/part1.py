#!/usr/bin/env python3
file = open('input.txt', 'r')
start_grid = [
    ['S','L','F','Z','D','B','R','H'],
    ['R','Z','M','B','T'],
    ['S','N','H','C','L','Z'],
    ['J','F','C','S'],
    ['B','Z','R','W','H','G','P'],
    ['T','M','N','D','G','Z','J','V'],
    ['Q','P','S','F','W','N','L','G'],
    ['R','Z','M'],
    ['T','R','V','G','L','C','M']
]
has_started = False

for line in file:
    line = line.strip()
    input_split = line.split()
    amount = int(input_split[1])
    from_index = int(input_split[3]) - 1
    to_index = int(input_split[5]) - 1

    for x in range(0,amount):
        letter = start_grid[from_index].pop(0)
        start_grid[to_index].insert(0, letter)

topOrder = ''
for line in start_grid:
    topOrder = topOrder + line.pop(0)

print(topOrder)