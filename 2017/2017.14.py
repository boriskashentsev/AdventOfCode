import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

def calculateHash(str):
  lengths = list(map(lambda x: ord(x), list(str))) + [17, 31, 73, 47, 23]

  index = 0
  skipSize = 0

  myList = list(range(256))

  for i in range(64):
      for length in lengths:
          if length <= len(myList):
              endIndex = index + length
              listToReverse = []
              if endIndex > len(myList):
                  listToReverse = list(reversed(myList[index:] + myList[:endIndex-len(myList)]))
                  myList = listToReverse[len(myList)-index:] + myList[endIndex-len(myList):index] + listToReverse[:len(myList)-index]
              else:
                  listToReverse = list(reversed(myList[index:endIndex]))
                  myList = myList[:index] + listToReverse + myList[endIndex:]
              index = (index + length + skipSize) % len(myList)
              skipSize += 1

  finalHash = ''

  for i in range(16):
      result = myList[16*i]
      for j in range(1,16):
          result ^= myList[16*i + j]
      hexResult = hex(result)
      finalHash += '0'*(4-len(hexResult)) + hexResult[2:]
  return finalHash

def hashToBin(hash):
  return bin(int(hash, 16))[2:].zfill(128)

# Part 1

result = 0

binMap = []

for num in range(128):
  line = input + '-' + str(num)

  hash = calculateHash(line)
  binLine = hashToBin(hash)
  binMap.append(list(map(lambda x: '.' if x == '0' else '#', list(binLine))))
  for char in binLine:
    if char == '1':
      result += 1

print("Part 1: ", result)

# Part 2

def lookForRegionStart(binMap):
  ''' A very slow way to find the new region '''
  for i in range(len(binMap)):
    for j in range(len(binMap[0])):
      if binMap[i][j] == '#':
        return [i, j]
  return[-1, -1]

def colorRegion(binMap, x, y):
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]
  if binMap[x][y] == '#':
    binMap[x][y] = ' '
    for i in range(len(dx)):
      if (x + dx[i]) in range(128) and (y + dy[i]) in range(128):
        binMap = colorRegion(binMap, x + dx[i], y + dy[i])
  return binMap

regionExists = True
numberOfRegions = 0

while regionExists:
  [x,y] = lookForRegionStart(binMap)
  if x<0 and y<0:
    regionExists = False
  else:
    numberOfRegions += 1
    binMap = colorRegion(binMap, x, y)

print("Part 2: ", numberOfRegions)
