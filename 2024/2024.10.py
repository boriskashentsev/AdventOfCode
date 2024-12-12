import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

rows = input.split("\n")

zeros = []
nines = []
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == "0":
            zeros.append([i, j])
        elif rows[i][j] == "9":
            nines.append([i, j])


def printMap(myMap: list) -> None:
    for row in myMap:
        print(row)


def walkDownWithoutOverlap(
    myMap: list, index: int, topographyMap: list, y: int, x: int
):
    currentValue = int(topographyMap[y][x])
    if currentValue > 0:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(len(dx)):
            newY = y + dy[i]
            newX = x + dx[i]
            if newY in range(len(topographyMap)) and newX in range(
                len(topographyMap[newY])
            ):
                if (
                    currentValue - int(topographyMap[newY][newX]) == 1
                    and index not in myMap[newY][newX]
                ):
                    myMap[newY][newX].append(index)
                    walkDownWithoutOverlap(myMap, index, topographyMap, newY, newX)


newMap = []
for i in range(len(rows)):
    row = []
    for j in range(len(rows[i])):
        row.append([])
    newMap.append(row)

for i, nine in enumerate(nines):
    newMap[nine[0]][nine[1]] = [i]

for i in range(len(nines)):
    walkDownWithoutOverlap(newMap, i, rows, nines[i][0], nines[i][1])


result = 0
for zero in zeros:
    result += len(newMap[zero[0]][zero[1]])

print("Part 1: ", result)

# Part 2


def walkDownWithOverlap(myMap: list, topographyMap: list, y: int, x: int):
    currentValue = int(topographyMap[y][x])
    if currentValue > 0:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(len(dx)):
            newY = y + dy[i]
            newX = x + dx[i]
            if newY in range(len(topographyMap)) and newX in range(
                len(topographyMap[newY])
            ):
                if currentValue - int(topographyMap[newY][newX]) == 1:
                    myMap[newY][newX] += 1
                    walkDownWithOverlap(myMap, topographyMap, newY, newX)


newMap = []
for i in range(len(rows)):
    row = []
    for j in range(len(rows[i])):
        row.append(0)
    newMap.append(row)

for i, nine in enumerate(nines):
    newMap[nine[0]][nine[1]] = 1

for i in range(len(nines)):
    walkDownWithOverlap(newMap, rows, nines[i][0], nines[i][1])

result = 0
for zero in zeros:
    result += newMap[zero[0]][zero[1]]

print("Part 2: ", result)
