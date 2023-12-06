import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

def solver(seeds, lines): 
  i = 2
  while i < len(lines):
    if ':' in lines[i]:
      i += 1
      currentMap = []
      while i < len(lines) and lines[i] != '':
        currentMap.append(list(map(lambda x: int(x), lines[i].split(' '))))
        i += 1
    for j in range(len(seeds)):
      seed = seeds[j]
      for category in currentMap:
        if seed >= category[1] and seed < category[1] + category[2]:
          delta = seed - category[1]
          seed = category[0] + delta
          break
      seeds[j] = seed
    # print(seeds)
    i += 1
  return min(seeds)


seeds = list( map(lambda x: int(x),lines[0].split(' ')[1:]))

print("Part 1:", solver(seeds, lines))

# Part 2

seedRanges = list( map(lambda x: int(x),lines[0].split(' ')[1:]))
seeds = []
i = 0
minimumValue = -1
while i < len(seedRanges):
  seeds = list(range(seedRanges[i], seedRanges[i]+seedRanges[i+1]))
  # for j in range(seedRanges[i], seedRanges[i]+seedRanges[i+1]):
    # print(j)
  value = solver(seeds, lines)
  if minimumValue == -1 or minimumValue > (value):
    minimumValue = value
  i += 2
  print(len(seedRanges), i)

print("Part 2:", minimumValue)
