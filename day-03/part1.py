#!/usr/bin/env python3
file = open('input.txt', 'r')
commonLetters = []

for line in file:
    line = line.strip()
    sets = [line[:len(line)//2],line[len(line)//2:]]
    commonLetters.append((set(sets[0]) & set(sets[1])).pop()[0])

total = 0
print(commonLetters)
for letter in commonLetters:
    offset = 38 if letter.isupper() else 96
    total = total + ord(letter) - offset

print(total)