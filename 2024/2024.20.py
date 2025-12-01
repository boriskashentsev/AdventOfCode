import sys

from PIL import Image

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()


def printMap(myMap: list):
    for row in myMap:
        print(row)
    print("   -----")


def printImage(myMap: list[str], withStrings: bool = True):
    img = Image.new("L", (len(myMap), len(myMap[0])))
    maxValue = -1
    if not withStrings:
        for row in myMap:
            maxValue = max(*row, maxValue)

    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if withStrings:
                if myMap[i][j] == "#":
                    img.putpixel((j, i), 255)
                elif myMap[i][j] in "SE":
                    img.putpixel((j, i), 125)
            else:
                value = min(max(0, int(myMap[i][j] * 255 / maxValue)), 255)
                img.putpixel((j, i), value)

    img.save("2024/2024.20.bmp")


def findState(myMap: list[str], state: str) -> list[int]:
    for i in range(len(myMap)):
        if myMap[i].find(state) >= 0:
            return [i, myMap[i].find(state)]


def doWidthStep(
    myMap: list[str], depthMap: list[list[int]], locations: list[list[int]]
):
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while len(locations) > 0:
        location = locations.pop(0)
        value = depthMap[location[0]][location[1]]
        for d in dd:
            newX = location[1] + d[1]
            newY = location[0] + d[0]
            if (
                newY in range(len(myMap))
                and newX in range(len(myMap[newY]))
                and myMap[newY][newX] in ".E"
                and (
                    depthMap[newY][newX] > 0
                    and depthMap[newY][newX] > value + 1
                    or depthMap[newY][newX] < 0
                )
            ):
                depthMap[newY][newX] = value + 1
                locations.append([newY, newX])


def checkForSkips(myMap: list[list[int]], finishTime: int):
    result = 0
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == -1:
                # Lets check only horisontal and vertical skips for now
                # vertical
                if (
                    (i - 1) in range(len(myMap))
                    and (i + 1) in range(len(myMap))
                    and myMap[i - 1][j] >= 0
                    and myMap[i + 1][j] >= 0
                ):
                    values = [myMap[i - 1][j], myMap[i + 1][j]]
                    # print(values)
                    savingTime = abs(values[0] - values[1]) - 2
                    if savingTime >= 100:
                        result += 1
                # horisontal
                if (
                    (j - 1) in range(len(myMap[i]))
                    and (j + 1) in range(len(myMap[i]))
                    and myMap[i][j - 1] >= 0
                    and myMap[i][j + 1] >= 0
                ):
                    values = [myMap[i][j - 1], myMap[i][j + 1]]
                    # print(values)
                    savingTime = abs(values[0] - values[1]) - 2
                    if savingTime >= 100:
                        result += 1
    return result


# Part 1


raceTrack = inputFile.split("\n")

startLocation = findState(raceTrack, "S")
finishLocation = findState(raceTrack, "E")

depthMap = []
for i in range(len(raceTrack)):
    depthMap.append([*[-1] * len(raceTrack[i])])
depthMap[startLocation[0]][startLocation[1]] = 0

doWidthStep(raceTrack, depthMap, [startLocation])

printImage(depthMap, withStrings=False)

finishTime = depthMap[finishLocation[0]][finishLocation[1]]

print(
    "Part 1: ",
    checkForSkips(
        depthMap,
        finishTime,
    ),
)
