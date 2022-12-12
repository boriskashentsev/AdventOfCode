import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def calculateUnique(numbers:list):
  result = [0,0,0]
  for number in numbers:
    result[number] += 1
  return result

layerSize = [25, 6]
layerLen = layerSize[0]*layerSize[1]
minZeros = layerLen + 1
result = 0

numbers = list(map(lambda x: int(x), list(input)))

for i in range(len(numbers)//layerLen):
  layer = numbers[i*layerLen:(i+1)*layerLen]
  values = calculateUnique(layer)
  if values[0] < minZeros:
    minZeros = values[0]
    result = values[1] * values[2]

print("Part 1: ", result)

# Part 2

def decideColor(number):
  if number == 0:
    return ' '
  elif number == 1:
    return '#'
  else:
    return '.'

def printImage(layer, size):
  for i in range(size[1]):
    line = layer[i*size[0]:(i+1)*size[0]]
    print(''.join(list(map(lambda x: decideColor(x),line))))

finalLayer = numbers[:layerLen]

for i in range(1, len(numbers)//layerLen):
  layer = numbers[i*layerLen:(i+1)*layerLen]
  for j in range(len(finalLayer)):
    if finalLayer[j] == 2:
      finalLayer[j] = layer[j]

print("Part 2:")
printImage(finalLayer, layerSize)