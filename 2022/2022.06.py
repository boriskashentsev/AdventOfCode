import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def areAllElementsUnique(line):
  for i in range(len(line)-1):
    for j in range(i+1, len(line)):
      if line[i] == line[j]:
        return False
  return True

for i in range(len(input)-3):
  if areAllElementsUnique(input[i:i+4]):
    print("Part 1: ", i+4)
    break

# Part 2

for i in range(len(input)-13):
  if areAllElementsUnique(input[i:i+14]):
    print("Part 1: ", i+14)
    break