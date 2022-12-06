#!/usr/bin/env python3
file = open('input.txt', 'r')
segment_length = 4

for line in file:
    line = line.strip()
    
    for startIndex in range(0, len(line) - segment_length - 1):
        segment = line[startIndex: startIndex + segment_length]
        # print(segment, set(segment))
        if (len(set(segment)) == len(segment)): 
            print(startIndex + segment_length)
            break
