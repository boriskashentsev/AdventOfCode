import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

def checkCondition(parts, registers):
    condition = True
    if parts[1] == '>':
        condition = registers[parts[0]] > int(parts[2])
    elif parts[1] == '>=':
        condition = registers[parts[0]] >= int(parts[2])
    elif parts[1] == '<':
        condition = registers[parts[0]] < int(parts[2])
    elif parts[1] == '<=':
        condition = registers[parts[0]] <= int(parts[2])
    elif parts[1] == '==':
        condition = registers[parts[0]] == int(parts[2])
    elif parts[1] == '!=':
        condition = registers[parts[0]] != int(parts[2])
    return condition

registers = {}

maxValuePart2 = -1
for line in lines:
    parts = line.split(' ')
    if parts[0] not in registers.keys():
        registers[parts[0]] = 0
    if parts[4] not in registers.keys():
        registers[parts[4]] = 0
    if checkCondition(parts[4:], registers):
        registers[parts[0]] += int(parts[2]) if parts[1] == 'inc' else -1*int(parts[2])
        if registers[parts[0]] > maxValuePart2:
            maxValuePart2 = registers[parts[0]]

maxValuePart1 = -1
for key in registers.keys():
    if maxValuePart1 < registers[key]:
        maxValuePart1 = registers[key]

print("Part 1:", maxValuePart1)
print("Part 2:",maxValuePart2)