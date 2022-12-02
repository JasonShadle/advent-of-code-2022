#!/usr/bin/env python3
file = open('input.txt', 'r')
maxCal = [0,0,0]
current = 0

for line in file:
    if line.strip() == "":
        maxCal.append(current)
        current = 0
    else: 
        current = current + int(line)

maxCal.sort()
print(sum(maxCal[-3:]))