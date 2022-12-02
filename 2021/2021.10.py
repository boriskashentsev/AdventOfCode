import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

location = { ")": "(", "]": "[", "}": "{", ">": "<"}

penalty = {")": 3, "]": 57, "}": 1197, ">": 25137}
points = {"(": 1, "[": 2, "{": 3, "<": 4}

errorScore = 0
scores = []

for line in lines:
    newLine = ""
    errorFlag = False
    for element in line:
        if element in location.keys():
            if newLine[-1] != location[element]:
                errorScore += penalty[element]
                errorFlag = True
                break
            else:
                newLine = newLine[:-1]
        else:
            newLine += element
    if not errorFlag:
        score = 0
        reversed(list(newLine))
        for element in reversed(list(newLine)):
            score = score*5 + points[element]
        scores.append(score)


print("Part 1: ", errorScore)

# Part 2

print("Part 2: ", sorted(scores)[len(scores)//2])
