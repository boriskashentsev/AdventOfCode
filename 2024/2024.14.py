import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1

robots = inputFile.split("\n")

lobby = [101, 103]

quadrants = [0, 0, 0, 0]
seconds = 100


def isInTheMiddle(position: list, lobby: list) -> bool:
    for i in range(len(position)):
        if position[i] == int(lobby[i] / 2):
            return True
    return False


def findQuadrant(position: list, lobby: list) -> int:
    result = 0
    for i in range(len(position)):
        result += 0 if position[i] < int(lobby[i] / 2) else i + 1
    return result


for robot in robots:
    [position, velocity] = robot.split(" ")
    position = list(map(lambda x: int(x), position[2:].split(",")))
    velocity = list(map(lambda x: int(x), velocity[2:].split(",")))
    newPosition = []
    for i in range(len(position)):
        newPosition.append((position[i] + velocity[i] * seconds) % lobby[i])
    if not isInTheMiddle(newPosition, lobby):
        quadrants[findQuadrant(newPosition, lobby)] += 1

result = 1
for quadrant in quadrants:
    result *= quadrant

print("Part 1: ", result)

# Part 2


def printMap(myMap: list) -> None:
    for row in myMap:
        print("   ", row)


for i in range(100):
    seconds = 8 + 101 * i  # Through tries and observation...
    coloringMap = list(map(lambda x: " " * lobby[1], range(lobby[0])))
    print(seconds)
    for robot in robots:
        [position, velocity] = robot.split(" ")
        position = list(map(lambda x: int(x), position[2:].split(",")))
        velocity = list(map(lambda x: int(x), velocity[2:].split(",")))
        newPosition = []
        for i in range(len(position)):
            newPosition.append((position[i] + velocity[i] * seconds) % lobby[i])
        coloringMap[newPosition[0]] = (
            coloringMap[newPosition[0]][: newPosition[1]]
            + "#"
            + coloringMap[newPosition[0]][newPosition[1] + 1 :]
        )
    printMap(coloringMap)
    input("Press Enter to continue...")
