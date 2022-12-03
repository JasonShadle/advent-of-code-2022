#!/usr/bin/env python3
file = open('input.txt', 'r')

outcomeDict = {
    'win': 6,
    'tie': 3,
    'lose': 0
}
symbolDict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

def getPoints(user, computer):
    diff = symbolDict.get(user) - symbolDict.get(computer)
    if (diff == 0):
        return symbolDict.get(user) + outcomeDict.get('tie')
    if (diff == 1 or diff == -2):
        return symbolDict.get(user) + outcomeDict.get('win')
   
    return symbolDict.get(user) + outcomeDict.get('lose')

total = 0
for line in file:
    inputs = line.strip().split(' ')
    total = total + int(getPoints(inputs[1], inputs[0]))

print(total)