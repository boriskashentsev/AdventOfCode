import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def isLineSafe(line):
  differents = []
  for i in range(len(line)-1):
    differents.append(int(line[i])-int(line[i+1]))
  if len(list(filter(lambda x: x > 0, differents))) == len(differents) or \
    len(list(filter(lambda x: x < 0, differents))) == len(differents) :
    if len(list(filter(lambda x: x in [1,2,3] or x in [-1, -2, -3], differents))) == len(differents):
      return True
  return False

lines = list(map(lambda x: x.split(' '), input.split('\n')))
result = 0
for line in lines:
  if isLineSafe(line):
    result += 1

print('Part 1: ', result)

# Part 2

result = 0
for line in lines:
  if isLineSafe(line):
    result += 1
  else:
    for i in range(len(line)):
      newLine = line[0:i] + line[i+1:len(line)]
      if isLineSafe(newLine):
        result += 1
        break
print('Part 2: ', result)

    