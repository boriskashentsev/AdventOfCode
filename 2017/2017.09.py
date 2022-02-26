import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n') # even though the input will have only 1 line, it is used for testing

def skipTrash(line, index, skippedTrash):
    while index < len(line):
        if line[index] == '>':
            return (index, skippedTrash)
        elif line[index] == '!':
            index += 1
        else:
            skippedTrash += 1
        index += 1

def checkInnerGroup(line, index, depth, score, skippedTrash):
    while index < len(line):
        if line[index] == '{':
            (index, score, skippedTrash) = checkInnerGroup(line, index+1, depth + 1, score, skippedTrash)
        elif line[index] == '<':
            (index, skippedTrash) = skipTrash(line, index + 1, skippedTrash)
        elif line[index] == '!':
            index +=1
        elif line[index] == '}':
            score += depth
            return(index, score, skippedTrash)
        index += 1
    return (index, score, skippedTrash)

for line in lines:
    index = 0
    if line[index] =='{':
        (index, score, skippedTrash) = checkInnerGroup(line, index+1, 1, 0, 0)
    print(score, skippedTrash)

