#!/usr/bin/env python3
file = open('input.txt', 'r')
totalOverlaps = 0
def contains_full_range(elf1, elf2):
    elf1_range = [int(x) for x in elf1.split('-')]
    elf2_range = [int(x) for x in elf2.split('-')]

    if (elf1_range[0] <= elf2_range[0] and elf1_range[1] >= elf2_range[1]
        or (elf2_range[0] <= elf1_range[0] and elf2_range[1] >= elf1_range[1])):
        return True
    return False

for line in file:
    line = line.strip()
    assignments = line.split(',')
    if (contains_full_range(assignments[0], assignments[1])): totalOverlaps = totalOverlaps + 1

print(totalOverlaps)