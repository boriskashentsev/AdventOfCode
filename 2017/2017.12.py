import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

connections = {}

for line in lines:
    parts = line.split(' <-> ')
    head = parts[0]
    destinations = parts[1].split(', ')
    if head not in connections.keys():
        connections[head] = set()
    for destination in destinations:
        if destination not in connections.keys():
            connections[destination] = set()
        connections[head].add(destination)
        connections[destination].add(head)

# Part 1

zeroGroup = ['0']
index = 0

while index < len(zeroGroup):
    for element in connections[zeroGroup[index]]:
        if element not in zeroGroup:
            zeroGroup.append(element)
    index += 1

print("Part 1:", len(zeroGroup))

# Part 2

def isInSeparateGroups(element, separateGroups):
    for group in separateGroups:
        if element in group:
            return True
    return False

separateGroups = []

for key in connections.keys():
    if not isInSeparateGroups(key, separateGroups):
        newGroup = [key]
        index = 0
        while index < len(newGroup):
            for element in connections[newGroup[index]]:
                if element not in newGroup:
                    newGroup.append(element)
            index += 1
        separateGroups.append(newGroup)

print("Part 2:", len(separateGroups))