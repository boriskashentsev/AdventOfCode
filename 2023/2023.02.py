import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

result = 0
maximums = {'red': 12, 'green': 13, 'blue': 14}

for line in lines:
  gameParts= line.split(': ')
  gameNumber = int(gameParts[0].split(' ')[1])
  tries = gameParts[1].split('; ')
  validGame = True
  for playerTry in tries:
    cubes = playerTry.split(', ')
    for cube in cubes:
      cubeParts = cube.split(' ')
      if maximums[cubeParts[1]] < int(cubeParts[0]):
        validGame = False
        break
    if not validGame:
      break
  if validGame:
    result += gameNumber

print("Part 1: ", result)

# Part 2

result = 0

for line in lines:
  gameParts= line.split(': ')
  tries = gameParts[1].split('; ')
  gameMaximums = {'red': 0, 'green': 0, 'blue': 0}
  gamePower = 1
  for playerTry in tries:
    cubes = playerTry.split(', ')
    for cube in cubes:
      cubeParts = cube.split(' ')
      if gameMaximums[cubeParts[1]] < int(cubeParts[0]):
        gameMaximums[cubeParts[1]] = int(cubeParts[0])
  for key in gameMaximums.keys():
    gamePower *= gameMaximums[key]
  result += gamePower

print("Part 2: ", result)
