import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1


def printMap(warehouse):
    for row in warehouse:
        print(row)
    print("   -----")


def countGPSSum(warehouse: list[str], box: str = "O") -> int:
    result = 0
    for i in range(1, len(warehouse) - 1):
        if box in warehouse[i]:
            for j in range(1, len(warehouse[i]) - 1):
                if warehouse[i][j] == box:
                    result += 100 * i + j
    return result


def robotLocation(warehouse: list[str], robot: str) -> list[int]:
    for i in range(len(warehouse)):
        if robot in warehouse[i]:
            return [i, warehouse[i].index(robot)]


def doSimpleStep(warehouse: list[str], move: str):
    wall = "#"
    robot = "@"
    emptySpot = "."
    steps = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

    location = robotLocation(warehouse, robot)
    dimention = 0
    row = ""
    if move in "<>":
        dimention = 1
        row = warehouse[location[0]]
    elif move in "^v":
        row = "".join(list(map(lambda x: x[location[1]], warehouse)))

    isWorking = 1  # [-1, 0, 1]: [ Not possible to do the step, Stepped correctly, Still checking]
    index = location[dimention]
    element = row[index]
    row = row[:index] + emptySpot + row[index + 1 :]
    while isWorking > 0:
        newIndex = index + steps[move][dimention]
        if newIndex in range(len(row)):
            newElement = row[newIndex]
            if newElement != element:
                if newElement == wall:
                    isWorking = -1
                elif newElement == emptySpot:
                    isWorking = 0
                row = row[:newIndex] + element + row[newIndex + 1 :]
        element = newElement
        index = newIndex

    if isWorking == 0:
        if dimention == 1:
            warehouse[location[0]] = row
        else:
            for i in range(len(warehouse)):
                warehouse[i] = (
                    warehouse[i][: location[1]]
                    + row[i]
                    + warehouse[i][location[1] + 1 :]
                )


[warehouse, moves] = inputFile.split("\n\n")

warehouse = warehouse.split("\n")
moves = "".join(moves.split("\n"))

for move in moves:
    doSimpleStep(warehouse, move)

print("Part 1: ", countGPSSum(warehouse))

# Part 2


def rebuildWarehouse(warehouse: list[str]):
    for i in range(len(warehouse)):
        newRow = ""
        for element in warehouse[i]:
            if element == "@":
                newRow += "@."
            elif element == "O":
                newRow += "[]"
            else:
                newRow += element * 2
        warehouse[i] = newRow


def doStep(warehouse: list[str], move: str):
    wall = "#"
    robot = "@"
    emptySpot = "."
    steps = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

    location = robotLocation(warehouse, robot)
    # print(move)
    if move in "<>":
        dimention = 1
        row = warehouse[location[0]]

        isWorking = 1  # [-1, 0, 1]: [ Not possible to do the step, Stepped correctly, Still checking]
        index = location[dimention]
        element = row[index]
        row = row[:index] + emptySpot + row[index + 1 :]
        while isWorking > 0:
            newIndex = index + steps[move][dimention]
            if newIndex in range(len(row)):
                newElement = row[newIndex]
                if newElement != element:
                    if newElement == wall:
                        isWorking = -1
                    elif newElement == emptySpot:
                        isWorking = 0
                    row = row[:newIndex] + element + row[newIndex + 1 :]
            element = newElement
            index = newIndex
        if isWorking == 0:
            warehouse[location[0]] = row
    elif move in "^v":
        dimention = 0
        index = location[dimention]

        row = warehouse[location[dimention]]
        row = row[: location[1]] + emptySpot + row[location[1] + 1 :]

        newWarehouseRest = []
        newWarehouseRest.append(row)

        movingParts = {location[1]: robot}
        isWorking = 1

        while isWorking > 0:
            newIndex = index + steps[move][dimention]
            newRow = warehouse[newIndex]
            newMovingParts = {}
            for x in movingParts.keys():
                if warehouse[newIndex][x] == "#":
                    isWorking = -1
                    break
                elif warehouse[newIndex][x] == "[":
                    newMovingParts[x] = "["
                    if x + 1 not in newMovingParts.keys():
                        newMovingParts[x + 1] = "]"
                        newRow = newRow[: x + 1] + emptySpot + newRow[x + 2 :]
                elif warehouse[newIndex][x] == "]":
                    newMovingParts[x] = "]"
                    if x - 1 not in newMovingParts.keys():
                        newMovingParts[x - 1] = "["
                        newRow = newRow[: x - 1] + emptySpot + newRow[x:]
                newRow = newRow[:x] + movingParts[x] + newRow[x + 1 :]
            newWarehouseRest.append(newRow)

            if isWorking == -1:
                break

            if len(newMovingParts.keys()) == 0:
                isWorking = 0
            else:
                index = newIndex
                movingParts = newMovingParts

        if isWorking == 0:
            for i in range(len(newWarehouseRest)):
                warehouse[location[dimention] + i * steps[move][dimention]] = (
                    newWarehouseRest[i]
                )


[warehouse, moves] = inputFile.split("\n\n")

warehouse = warehouse.split("\n")
moves = "".join(moves.split("\n"))
rebuildWarehouse(warehouse)

for move in moves:
    doStep(warehouse, move)

print("Part 2: ", countGPSSum(warehouse, "["))
