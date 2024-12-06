import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def currentLocation(myMap):
  for i in range(len(myMap)):
    for j in range(len(myMap[i])):
      if myMap[i][j] in '^<>v':
        return [i,j]

def printWholeMap(myMap):
  for i in range(len(myMap)):
    print(myMap[i])
  print(' ')

rows = input.split('\n')

[y, x] = currentLocation(rows)

directions = '^>v<'
directionXmoves = {'^':[-1, 0], '>': [0, 1], 'v':[1, 0], '<': [0, -1]}

isAbleToWalk = True

while isAbleToWalk:
  direction = rows[y][x]
  newY = y + directionXmoves[direction][0]
  newX = x + directionXmoves[direction][1]
  if not (newY in range(len(rows)) and newX in range(len(rows[newY]))):
    isAbleToWalk = False
  else:
    if rows[newY][newX] == '#':
      rows[y] = rows[y][:x] + directions[(directions.find(direction) + 1) % len(directions)] + rows[y][x+1:]
    else:
      rows[newY] = rows[newY][:newX] + direction + rows[newY][newX+1:]
      rows[y] = rows[y][:x] + 'X' + rows[y][x+1:]
      y = newY
      x = newX

result = 0
for i in range(len(rows)):
  for j in range(len(rows[i])):
    if rows[i][j] in 'X^>v<':
      result += 1

print('Part 1: ', result)

# Part 2

def hasInfiniteLoop(myMap, location):
  directions = '^>v<'
  directionXmoves = {'^':[-1, 0], '>': [0, 1], 'v':[1, 0], '<': [0, -1]}
  isAbleToWalk = True
  walkedPlaces = {'^':[], '>': [], 'v':[], '<': []}
  [y, x] = location

  while isAbleToWalk:
    direction = myMap[y][x]
    newY = y + directionXmoves[direction][0]
    newX = x + directionXmoves[direction][1]
    if not (newY in range(len(myMap)) and newX in range(len(myMap[newY]))):
      isAbleToWalk = False
    else:
      if myMap[newY][newX] == '#':
        newDirection = directions[(directions.find(direction) + 1) % len(directions)]
        myMap[y] = myMap[y][:x] + newDirection + myMap[y][x+1:]
        if [newY, newX] in walkedPlaces[newDirection]:
          break
        else:
          walkedPlaces[newDirection].append([newY, newX])
      elif myMap[newY][newX] == direction:
        break
      else:
        myMap[newY] = myMap[newY][:newX] + direction + myMap[newY][newX+1:]
        if [newY, newX] in walkedPlaces[direction]:
          break
        else:
          walkedPlaces[direction].append([newY, newX])
        y = newY
        x = newX
  
  return isAbleToWalk

def placesToPlaceBlock (myMap):
  locations = []
  for i in range(len(myMap)):
    for j in range(len(myMap[i])):
      if myMap[i][j] in 'X^>v<':
        locations.append([i,j])
  return locations

blockPlaces = placesToPlaceBlock(rows)

rows = input.split('\n')

[y, x] = currentLocation(rows)

result = 0
for k in range(len(blockPlaces)):
  [i,j] = blockPlaces[k]
  if rows[i][j] == '.':
    rows[i] = rows[i][:j] + '#' + rows[i][j+1:]
    if hasInfiniteLoop(rows, [y, x]):
      result += 1
    rows = input.split('\n')

print('Part 2: ', result)