#!/usr/bin/env python3
file = open('input.txt', 'r')
maxCal = 0
current = 0

for line in file:
    if line.strip() == "":
        if current > maxCal:
            maxCal = current
        current = 0
    else: 
        current = current + int(line)

print(maxCal if maxCal > current else current)