import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

def printOctopi(octopi):
  for line in octopi:
    print(''.join([str(element%10) for element in line]))

def step(octopi: list):
  di = [-1, -1, 0, 1, 1, 1, 0, -1]
  dj = [0, -1, -1, -1, 0, 1, 1, 1]
  flashes = []
  numberOfFlashes = 0
  for i in range(len(octopi)):
    for j  in range(len(octopi[i])):
      octopi[i][j] += 1
      if octopi[i][j] == 10:
        flashes.append([i, j])
  while len(flashes) > 0:
    numberOfFlashes += 1
    [i, j] = flashes.pop()
    for k in range(len(di)):
      if (i + di[k]) in range(len(octopi)) and (j + dj[k]) in range(len(octopi[i])):
        octopi[i + di[k]][j + dj[k]] += 1
        if octopi[i + di[k]][j + dj[k]] == 10:
          flashes.append([i + di[k],j + dj[k]])
  for i in range(len(octopi)):
    for j  in range(len(octopi[i])):
      if octopi[i][j] > 9:
        octopi[i][j] = 0
  return numberOfFlashes

# Part 1

octopi = list(map(lambda x: list(map(lambda y: int(y), x)),[list(line) for line in lines]))

result = 0
for i in range(100):
  result += step(octopi)

print("Part 1: ", result)

# Part 2

allFlashed = False
steps = 100

while not allFlashed:
  if step(octopi) == 100:
    allFlashed = True
  steps += 1

print("Part 2: ", steps)