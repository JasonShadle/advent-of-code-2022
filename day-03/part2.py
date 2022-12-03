#!/usr/bin/env python3
file = open('input.txt', 'r')
lines = file.read().splitlines()

commonLetters = []

for i in range(0, len(lines) // 3):
    j = i*3
    commonLetters.append(set(lines[j]).intersection(lines[j+1]).intersection(lines[j+2]).pop()[0])

total = 0

for letter in commonLetters:
    offset = 38 if letter.isupper() else 96
    total = total + ord(letter) - offset

print(total)