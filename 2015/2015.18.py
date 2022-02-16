from operator import contains
import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

neighbours = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

steps = 100

def numberOfOnLights (grid):
    lightsOnNumber = 0
    for line in grid:
        for element in line:
            if element == '#':
                lightsOnNumber += 1
    return lightsOnNumber

def nextStep(grid):
    newGrid = []
    for i in range(len(grid)):
        lineForNewGrid = []
        for j in range(len(grid[i])):
            onNeighbours = 0
            for neighbour in neighbours:
                newI = i + neighbour[0]
                newJ = j + neighbour[1]
                if newI >= 0 and newI < len(grid) and newJ >= 0 and newJ < len(grid[i]):
                    if grid[newI][newJ] == '#':
                        onNeighbours += 1
            if (grid[i][j] == '#' and onNeighbours in [2,3]) or (grid[i][j] == '.' and onNeighbours == 3):
                lineForNewGrid.append('#')
            else:
                lineForNewGrid.append('.')
        newGrid.append(lineForNewGrid)
    return newGrid

# Part 1

grid = []
for line in lines:
    grid.append(list(line))

for i in range(steps):
    grid = nextStep(grid)

print(numberOfOnLights(grid))

# Part 2

def addFaultylights(grid):
    grid[0][0] = '#'
    grid[0][len(grid[0])-1] = '#'
    grid[len(grid)-1][0] = '#'
    grid[len(grid)-1][len(grid[0])-1] = '#'

grid = []
for line in lines:
    grid.append(list(line))
addFaultylights(grid)

for i in range(steps):
    grid = nextStep(grid)
    addFaultylights(grid)

print(numberOfOnLights(grid))