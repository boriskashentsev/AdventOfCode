import sys

from PIL import Image

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1


def printMap(myMap: list[str]):
    for row in myMap:
        print(row)
    print("   -----")


def printImage(myMap: list[str]):
    img = Image.new("L", (len(myMap), len(myMap[0])))
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == "#":
                img.putpixel((j, i), 255)
            elif myMap[i][j] == "O":
                img.putpixel((j, i), 125)

    img.save("2024/2024.18.bmp")


def printImageFromDepth(myMap: list[list[int]]):
    img = Image.new("L", (len(myMap), len(myMap[0])))
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            img.putpixel((j, i), min(255, myMap[j][i]))

    img.save("2024/2024.18.bmp")


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
                and myMap[newY][newX] == "."
                and (
                    depthMap[newY][newX] > 0
                    and depthMap[newY][newX] > value + 1
                    or depthMap[newY][newX] < 0
                )
            ):
                depthMap[newY][newX] = value + 1
                locations.append([newY, newX])


corruptedBytes = list(map(lambda x: x.split(","), inputFile.split("\n")))

memorySize = 71
corruptedBytesNumber = 1024

if len(sys.argv) > 1:
    memorySize = 7
    corruptedBytesNumber = 12

memory = []
depthMap = []

for i in range(memorySize):
    memory.append("." * memorySize)
    depthMap.append([*[-1] * memorySize])

for i in range(corruptedBytesNumber):
    [x, y] = list(map(lambda xx: int(xx), corruptedBytes[i]))
    memory[y] = memory[y][:x] + "#" + memory[y][x + 1 :]

memory[0] = "O" + memory[0][1:]
depthMap[0][0] = 0

doWidthStep(memory, depthMap, [[0, 0]])

print("Part 1: ", depthMap[len(memory) - 1][len(memory[len(memory) - 1]) - 1])

# Part 2
for i in range(corruptedBytesNumber + 1, len(corruptedBytes)):
    [x, y] = list(map(lambda xx: int(xx), corruptedBytes[i]))
    memory[y] = memory[y][:x] + "#" + memory[y][x + 1 :]
    depthMap = []
    for i in range(memorySize):
        depthMap.append([*[-1] * memorySize])
    depthMap[0][0] = 0
    doWidthStep(memory, depthMap, [[0, 0]])

    if depthMap[len(memory) - 1][len(memory[len(memory) - 1]) - 1] < 0:
        print("Part2: ", ",".join([str(x), str(y)]))
        break
