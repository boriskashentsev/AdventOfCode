from msilib.schema import Directory
import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy
from math import copysign

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

def calculateDistance(originalDirections):
    directions = deepcopy(originalDirections)
    if directions['ne'] * directions['nw'] > 0:
        correction = min(abs(directions['ne']),abs(directions['nw']))
        directions['n'] += int(copysign(correction, directions['ne']))
        directions['ne'] = int(copysign(abs(directions['ne'])-correction,directions['ne']))
        directions['nw'] = int(copysign(abs(directions['nw'])-correction,directions['nw']))

    if directions['ne'] * directions['n'] < 0:
        correction = min(abs(directions['ne']),abs(directions['n']))
        directions['nw'] += int(copysign(correction, directions['n']))
        directions['ne'] = int(copysign(abs(directions['ne'])-correction,directions['ne']))
        directions['n'] = int(copysign(abs(directions['n'])-correction,directions['n']))

    if directions['nw'] * directions['n'] < 0:
        correction = min(abs(directions['nw']),abs(directions['n']))
        directions['ne'] += int(copysign(correction, directions['n']))
        directions['nw'] = int(copysign(abs(directions['nw'])-correction,directions['nw']))
        directions['n'] = int(copysign(abs(directions['n'])-correction,directions['n']))

    result = 0
    for key in directions.keys():
        result += abs(directions[key])

    return result

steps = input.split(',')

# Part 1

directions = {'nw': 0, 'n':0, 'ne':0}
transition = {'nw':['nw',1],'n':['n',1],'ne':['ne',1],'sw':['ne',-1],'se':['nw',-1],'s':['n',-1],}

for step in steps:
    directions[transition[step][0]] += transition[step][1]

print("Part 1:", calculateDistance(directions))

# Part 2

directions = {'nw': 0, 'n':0, 'ne':0}

maxDistance = -1

for step in steps:
    directions[transition[step][0]] += transition[step][1]
    distance = calculateDistance(directions)
    if maxDistance < distance:
        maxDistance = distance

print('Part 2:', maxDistance)
