def isLowestPoint(map, x, y):
    steps = [[0,-1],[-1,0],[0,1],[1,0]]
    for step in steps:
        newX = x+step[1]
        newY = y+step[0]
        if (newY) in range (len(map)) and (newX) in range(len(map[newY])) and int(map[newY][newX]) <= int(map[y][x]):
            return False
    return True

def isPartOfBasin(map, basins, x, y):
    steps = [[0,-1],[-1,0],[0,1],[1,0]]
    for step in steps:
        newX = x+step[1]
        newY = y+step[0]
        if (newY) in range (len(map)) and (newX) in range(len(map[newY])) and (basins[newY][newX] != '*')  and int(map[newY][newX]) <= int(map[y][x]):
            return False
    return True

def increaseWater(map, surface, coordinates, depth):
    steps = [[0,-1],[-1,0],[0,1],[1,0]]
    notAnEdge = []
    newCoordinates = []
    overflowTest = False
    for i in range(len(coordinates)):
        [x,y] = coordinates[i]
        edgeTest = 0
        for step in steps:
            newX = x+step[1]
            newY = y+step[0]
            if (newY) in range(len(surface)) and (newX) in range(len(surface[newY])):
                if surface[newY][newX] == '*':
                    edgeTest += 1
                elif int(map[newY][newX]) == depth:
                    newCoordinates.append([newX, newY])
        if edgeTest == 4:
            notAnEdge.append(i)
    for [x,y] in newCoordinates:
        for step in steps:
            newX = x+step[1]
            newY = y+step[0]
            if (newY) in range(len(surface)) and (newX) in range(len(surface[newY])):
                if int(map[newY][newX]) < depth and surface[newY][newX] != '*':
                    overflowTest = True
                elif int(map[newY][newX]) == depth and [newX, newY] not in newCoordinates:
                    newCoordinates.append([newX, newY])
    if not overflowTest:
        for coordinate in newCoordinates:
            if coordinate not in coordinates:
                coordinates.append(coordinate)

    return overflowTest

def findBasin(map, surface, x, y, size):
    edgeCoordinates = [[x,y]]
    for depth in range(int(map[y][x])+1, 9):
        isOverflown = increaseWater(map, surface, edgeCoordinates, depth)
        if isOverflown:
            break
        else:
            for [x, y] in edgeCoordinates:
                surface[y] = surfaceMap[y][:x] + '*' + surfaceMap[y][x+1:]
    return [surface, len(edgeCoordinates)]


def prettyPrint(surface, land, colorIndex = 0, backgroundIndex = 0):
    print('*** MAP ***')
    colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    background = ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']
    colorIndex = randrange(len(colors))
    backgroundIndex = randrange(len(background))
    backgroundIndex = (backgroundIndex + 1) % len(colors) if backgroundIndex == colorIndex else backgroundIndex
    for i in range(len(land)):
        line = ''
        for j in range(len(land[i])):
            character = ''
            if(land[i][j] == '*'):
                character = colored(surface[i][j], colors[colorIndex], background[backgroundIndex])
            else:
                character = surface[i][j]
            line += character
        print(line)

def showMapAsImage(surface, scale = 1):
    surfaceImage=list(map(lambda y: list(map(lambda x:(int(x)*28, int(x)*28, int(x)*28), y)), surface))
    surfaceAsArray = np.array(surfaceImage, dtype=np.uint8)
    surfaceAsArray = np.kron(surfaceAsArray, np.ones((scale, scale, 1), dtype=np.uint8))
    im = Image.fromarray(surfaceAsArray)
    im.show()

import sys
from termcolor import colored, cprint
from random import randrange, seed
from PIL import Image
import numpy as np
sys.path.append('./')
from utils.filename import calculateFileName

seed(version = 2)

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

result = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if isLowestPoint(lines, j, i):
            result += 1 + int(lines[i][j])

print("Part 1 result:",result)

# Part 2

surfaceMap = ['.'*len(lines[0])]*len(lines)
basinSizes = []
#showMapAsImage(lines,3)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if isLowestPoint(lines, j, i):
            surfaceMap[i] = surfaceMap[i][:j] + '*' + surfaceMap[i][j+1:]
            [surfaceMap, basinSize] = findBasin(lines, surfaceMap, j, i, 1)
            basinSizes.append(basinSize)

prettyPrint(lines, surfaceMap)

basinSizes.sort(reverse=True)

print("Part 2 result:", basinSizes[0]*basinSizes[1]*basinSizes[2])