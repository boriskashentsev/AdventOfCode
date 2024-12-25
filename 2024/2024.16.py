import sys

from PIL import Image

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1

sys.setrecursionlimit(4000)


def printMap(
    track: list[str],
    location: list[int] = [-1, -1],
    formated: int = 0,
    rightCorner: int = 0,
):
    if formated == 0:
        for i in range(len(track)):
            if location[0] != i:
                print(track[i])
            else:
                print(track[i][: location[1]] + "@" + track[i][location[1] + 1 :])
    else:
        for i in range(rightCorner if rightCorner > 0 else len(track)):
            line = ""
            for j in (
                range(len(track[i]) - rightCorner, len(track[i]))
                if rightCorner > 0
                else range(len(track[i]))
            ):
                value = str(track[i][j])
                line += " " * max(0, formated - len(value)) + value
            print(line)
    print("   -----")


def buildPointsMap(track: list[str]) -> list[list[int]]:
    points = []
    for line in track:
        points.append([*[0] * len(line)])
    return points


def findState(track: list[str], state: str) -> list[int]:
    for i in range(len(track)):
        if state in track[i]:
            return [i, track[i].find(state)]


def walkAround(
    track: list[str],
    points: list[list[int]],
    location: list[int],
    direction: str,
    currentPoints: int,
):
    steps = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}
    directions = "^>v<"
    forwardPoint = 1
    turnPoint = 1000
    # check if we came
    if track[location[0]][location[1]] == "E":
        return
    # going forward
    if track[location[0] + steps[direction][0]][
        location[1] + steps[direction][1]
    ] in ".E" and (
        points[location[0] + steps[direction][0]][location[1] + steps[direction][1]]
        > currentPoints + forwardPoint
        or points[location[0] + steps[direction][0]][location[1] + steps[direction][1]]
        == 0
    ):
        points[location[0] + steps[direction][0]][location[1] + steps[direction][1]] = (
            currentPoints + forwardPoint
        )
        walkAround(
            track,
            points,
            [location[0] + steps[direction][0], location[1] + steps[direction][1]],
            direction,
            currentPoints + forwardPoint,
        )

    if points[location[0]][location[1]] >= currentPoints:
        # turning left
        walkAround(
            track,
            points,
            location,
            directions[(directions.find(direction) - 1) % len(directions)],
            currentPoints + turnPoint,
        )
        # turning right
        walkAround(
            track,
            points,
            location,
            directions[(directions.find(direction) + 1) % len(directions)],
            currentPoints + turnPoint,
        )


track = inputFile.split("\n")

points = buildPointsMap(track)
start = findState(track, "S")
finish = findState(track, "E")

walkAround(track, points, start, ">", 0)
result = points[finish[0]][finish[1]]

print("Part 1: ", result)


# Part 2


def goBack(
    path: list[str],
    walkedPath: list[list[int]],
    location: list[int],
    endLocation: list[int],
):
    steps = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    if path[location[0]][location[1]] == 0:
        return
    else:
        walkedPath[location[0]][location[1]] = 1

    for step in steps:
        [y, x] = [location[0] + step[0], location[1] + step[1]]
        if (
            location == endLocation
            and path[location[0]][location[1]] - path[y][x] in [1, 1001]
            and walkedPath[y][x] == 0
        ) or (
            location != endLocation
            and path[location[0]][location[1]] - path[y][x] in [-999, 1, 1001]
            and walkedPath[y][x] == 0
        ):
            goBack(path, walkedPath, [y, x], endLocation)


def walkAroundAgain(
    walkedPath: list[list[int]],
    path: list[list[int]],
    direction: str,
    currentPoints: int,
    endState: list,
):
    steps = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}
    directions = "^>v<"
    forwardPoint = 1
    turnPoint = 1000
    location = path[-1]
    if currentPoints > endState[1]:
        return
    if currentPoints == endState[1] and location == endState[0]:
        for step in path:
            walkedPath[step[0]][step[1]] = 2
    else:
        newLocation = [
            location[0] + steps[direction][0],
            location[1] + steps[direction][1],
        ]
        if walkedPath[newLocation[0]][newLocation[1]] > 0 and newLocation not in path:
            walkAroundAgain(
                walkedPath,
                [*path, newLocation],
                direction,
                currentPoints + forwardPoint,
                endState,
            )
        # left
        turnLeft = directions[(directions.find(direction) - 1) % len(directions)]
        leftLocation = [
            location[0] + steps[turnLeft][0],
            location[1] + steps[turnLeft][1],
        ]
        if (
            walkedPath[leftLocation[0]][leftLocation[1]] > 0
            and leftLocation not in path
        ):
            walkAroundAgain(
                walkedPath,
                [*path, leftLocation],
                turnLeft,
                currentPoints + forwardPoint + turnPoint,
                endState,
            )
        # right
        turnRight = directions[(directions.find(direction) + 1) % len(directions)]
        rightLocation = [
            location[0] + steps[turnRight][0],
            location[1] + steps[turnRight][1],
        ]
        if (
            walkedPath[rightLocation[0]][rightLocation[1]] > 0
            and rightLocation not in path
        ):
            walkAroundAgain(
                walkedPath,
                [*path, rightLocation],
                turnRight,
                currentPoints + forwardPoint + turnPoint,
                endState,
            )


finish = findState(track, "E")
walkedPath = buildPointsMap(track)
walkedPath[start[0]][start[1]] = 1

goBack(points, walkedPath, finish, finish)
walkAroundAgain(walkedPath, [[*start]], ">", 0, [finish, points[finish[0]][finish[1]]])

result = 0
for row in walkedPath:
    for element in row:
        if element > 1:
            result += 1

print("Part 2: ", result)

img = Image.new("L", (len(walkedPath), len(walkedPath[0])))
for i in range(len(walkedPath)):
    for j in range(len(walkedPath[i])):
        if walkedPath[i][j] >= 1:
            img.putpixel((j, i), 125 * walkedPath[i][j])

img.save("2024/2024.16.bmp")
