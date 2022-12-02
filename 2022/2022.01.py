import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

arrayOfCallories = []
calories = 0
for line in lines:
  if line == "":
    arrayOfCallories.append(calories)
    calories = 0
  else:
    calories += int(line)

arrayOfCallories.append(calories)

arrayOfCallories.sort(reverse=True)

print("Part 1: ", arrayOfCallories[0])

# Part 2

print("Part 2: ", sum(arrayOfCallories[:3]))