import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

# Part 1

antennas = {}

for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] != '.':
      if lines[i][j] not in antennas.keys():
        antennas[lines[i][j]] = []
      antennas[lines[i][j]].append([i,j])

antinodes = []

for key in antennas.keys():
  for i in range(len(antennas[key])-1):
    for j in range(i+1,len(antennas[key])):
      first = antennas[key][i]
      second = antennas[key][j]
      zero = [ 2*first[0]-second[0], 2*first[1]-second[1]]
      if zero[0] in range(len(lines)) and zero[1] in range(len(lines[zero[0]])):
        if zero not in antinodes:
          antinodes.append(zero)
      zero = [ 2*second[0]-first[0], 2*second[1]-first[1]]
      if zero[0] in range(len(lines)) and zero[1] in range(len(lines[zero[0]])):
        if zero not in antinodes:
          antinodes.append(zero)

print("Part 1: ", len(antinodes))

# Part 2

antinodes = []

for key in antennas.keys():
  if len(antennas[key]) > 1:
    for i in range(len(antennas[key])):
      if antennas[key][i] not in antinodes:
          antinodes.append(antennas[key][i])

for key in antennas.keys():
  for i in range(len(antennas[key])-1):
    first = antennas[key][i]
    for j in range(i+1,len(antennas[key])):
      second = antennas[key][j]
      isMovingForward = True
      multiplier = 1
      while isMovingForward:
        zero = [ first[0] + multiplier*(first[0]-second[0]), first[1] + multiplier*(first[1]-second[1])]
        if zero[0] in range(len(lines)) and zero[1] in range(len(lines[zero[0]])):
          if zero not in antinodes:
            antinodes.append(zero)
        else:
          isMovingForward = False
        multiplier += 1

      isMovingForward = True
      multiplier = 1
      while isMovingForward:
        zero = [ second[0] + multiplier*(second[0]-first[0]), second[1] + multiplier*(second[1]-first[1])]
        if zero[0] in range(len(lines)) and zero[1] in range(len(lines[zero[0]])):
          if zero not in antinodes:
            antinodes.append(zero)
        else:
          isMovingForward = False
        multiplier += 1

print("Part 2: ", len(antinodes))