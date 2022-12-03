#!/usr/bin/env python3
file = open('input.txt', 'r')

outcomeDict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
symbolDict = {
    'A': 1,
    'B': 2,
    'C': 3
}
pointChangeForOutcome = {
    'X': -1,
    'Y': 0,
    'Z': 1
}

def getPoints(outcome, computer):
    return getUserSymbolPointValue(outcome, computer) + outcomeDict.get(outcome)

def getUserSymbolPointValue(outcome, computer):
    pointChange = pointChangeForOutcome.get(outcome)
    computerPoints = symbolDict.get(computer)
    return list(symbolDict.values())[(computerPoints + pointChange - 1) % 3]

total = 0
for line in file:
    inputs = line.strip().split(' ')
    total = total + getPoints(inputs[1], inputs[0])

print(total)