import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1


def printMap(myMap: list) -> None:
    for row in myMap:
        print(row)


def hasSpaceToColor(myMap: list, ch: str) -> list:
    for i in range(len(myMap)):
        if ch in myMap[i]:
            return [i, myMap[i].index(ch)]
    return []


def colorAreaWithPerimeter(
    garden: list, coloringMap: list, location: list, uncoloredChar: str
) -> list:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    [y, x] = location
    ch = garden[y][x]
    coloringMap[y] = coloringMap[y][:x] + "#" + coloringMap[y][x + 1 :]
    # Check Perimeter
    perimeter = 0
    for i in range(len(dx)):
        [newY, newX] = [y + dy[i], x + dx[i]]
        if newY in range(len(garden)) and newX in range(len(garden[newY])):
            neighbour = garden[newY][newX]
            if neighbour != ch:
                perimeter += 1
        else:
            perimeter += 1
    # Continue Coloring
    neighboursValues = [0, 0]
    for i in range(len(dx)):
        [newY, newX] = [y + dy[i], x + dx[i]]
        if newY in range(len(garden)) and newX in range(len(garden[newY])):
            if garden[newY][newX] == ch and coloringMap[newY][newX] == uncoloredChar:
                rest = colorAreaWithPerimeter(
                    garden, coloringMap, [newY, newX], uncoloredChar
                )
                neighboursValues = [
                    neighboursValues[0] + rest[0],
                    neighboursValues[1] + rest[1],
                ]
    return [neighboursValues[0] + perimeter, neighboursValues[1] + 1]


garden = input.split("\n")

uncoloredChar = "."
coloringMap = list(map(lambda x: uncoloredChar * len(x), garden))
isColoring = True
result = 0
while isColoring:
    location = hasSpaceToColor(coloringMap, uncoloredChar)
    if len(location) > 0:
        [perimeter, area] = colorAreaWithPerimeter(
            garden, coloringMap, location, uncoloredChar
        )
        result += perimeter * area
    else:
        isColoring = False

print("Part 1: ", result)

# Part 2


def checkCorner(garden: list, location: list, cornerDirections: list) -> bool:

    def gardenValue(garder: list, y: int, x: int) -> str:
        if y not in range(len(garden)) or x not in range(len(garden[y])):
            return "."
        return garden[y][x]

    [dy, dx] = cornerDirections
    [y, x] = location
    ch = garden[y][x]
    diag = gardenValue(garden, y + dy[0], x + dx[0])
    if diag != ch:
        left = gardenValue(garden, y + dy[1], x + dx[1])
        right = gardenValue(garden, y + dy[2], x + dx[2])
        if (left == ch and right == ch) or (left != ch and right != ch):
            return True
    else:
        left = gardenValue(garden, y + dy[1], x + dx[1])
        right = gardenValue(garden, y + dy[2], x + dx[2])
        if left != ch and right != ch:
            return True
    return False


def checkCorners(garden: list, location: list) -> int:
    dy = [[-1, 0, -1], [-1, -1, 0], [1, 0, 1], [1, 1, 0]]
    dx = [[-1, -1, 0], [1, 0, 1], [1, 1, 0], [-1, 0, -1]]
    result = 0
    for i in range(len(dy)):
        if checkCorner(garden, location, [dy[i], dx[i]]):
            result += 1
    return result


def colorAreaWithSides(
    garden: list, coloringMap: list, location: list, uncoloredChar: str
) -> list:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    [y, x] = location
    ch = garden[y][x]
    coloringMap[y] = coloringMap[y][:x] + "#" + coloringMap[y][x + 1 :]
    # Check Sides
    corners = checkCorners(garden, location)
    # Continue Coloring
    neighboursValues = [0, 0]
    for i in range(len(dx)):
        [newY, newX] = [y + dy[i], x + dx[i]]
        if newY in range(len(garden)) and newX in range(len(garden[newY])):
            if garden[newY][newX] == ch and coloringMap[newY][newX] == uncoloredChar:
                rest = colorAreaWithSides(
                    garden, coloringMap, [newY, newX], uncoloredChar
                )
                neighboursValues = [
                    neighboursValues[0] + rest[0],
                    neighboursValues[1] + rest[1],
                ]
    return [neighboursValues[0] + corners, neighboursValues[1] + 1]


garden = input.split("\n")

uncoloredChar = "."
coloringMap = list(map(lambda x: uncoloredChar * len(x), garden))
isColoring = True
result = 0
while isColoring:
    location = hasSpaceToColor(coloringMap, uncoloredChar)
    if len(location) > 0:
        [corners, area] = colorAreaWithSides(
            garden, coloringMap, location, uncoloredChar
        )
        result += corners * area
    else:
        isColoring = False

print("Part 2: ", result)
