import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

numberOfFullInclusions = 0

for line in lines:
  ranges=list(map(lambda x: x.split('-'),line.split(',')))
  firstRange = '.'+'.'.join(list(map(lambda x: str(x), list(range(int(ranges[0][0]), int(ranges[0][1]) + 1)))))+'.'
  secondRange = '.'+'.'.join(list(map(lambda x: str(x), list(range(int(ranges[1][0]), int(ranges[1][1]) + 1)))))+'.'
  if firstRange in secondRange or secondRange in firstRange:
    numberOfFullInclusions += 1
    ###
    # Beautiful way to print intersections
    ###
    # if firstRange in secondRange:
    #   spacesToFill = secondRange.find(ranges[0][0])-1
    #   print('--------------------')
    #   print(('.'*spacesToFill)+firstRange)
    #   print(secondRange)
    # else:
    #   spacesToFill = firstRange.find(ranges[1][0])-1
    #   print('--------------------')
    #   print(firstRange)
    #   print(('.'*spacesToFill)+secondRange)

  
print("Part 1: ", numberOfFullInclusions)

# Part 2

def wrapNumber(str):
  return '.'+str+'.'

numberOfPartialInclusions = 0

for line in lines:
  ranges=list(map(lambda x: x.split('-'),line.split(',')))
  firstRange = '.'+'.'.join(list(map(lambda x: str(x), list(range(int(ranges[0][0]), int(ranges[0][1]) + 1)))))+'.'
  secondRange = '.'+'.'.join(list(map(lambda x: str(x), list(range(int(ranges[1][0]), int(ranges[1][1]) + 1)))))+'.'
  if wrapNumber(ranges[0][0]) in secondRange or wrapNumber(ranges[0][1]) in secondRange:
    numberOfPartialInclusions += 1
  elif wrapNumber(ranges[1][0]) in firstRange or wrapNumber(ranges[1][1]) in firstRange:
    numberOfPartialInclusions += 1

print("Part 2: ", numberOfPartialInclusions)