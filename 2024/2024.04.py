import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines= input.split('\n')

# Part 1

dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]
line = 'XMAS'

result = 0
for i in range(len(lines)):
  for j in range(len(lines[i])):
    for k in range(len(dx)):
      x = j
      y = i
      pickedLine = lines[y][x]
      for l in range(len(line)-1):
        x += dx[k]
        y += dy[k]
        if y in range(len(lines)) and x in range(len(lines[y])):
          pickedLine += lines[y][x]
        else:
          break
      if len(pickedLine) == len(line):
        if pickedLine == line or pickedLine == line[::-1]:
          result += 1

print("Part 1: ", result)

# Part 2

line = 'MAS'
result = 0

for i in range(1, len(lines)-1):
  for j in range(1, len(lines[i])-1):
    if lines[i][j] == 'A':
      pickedLine = lines[i-1][j-1] + 'A' + lines[i+1][j+1]
      if pickedLine == line or pickedLine == line[::-1]:
        pickedLine = lines[i+1][j-1] + 'A' + lines[i-1][j+1]
        if pickedLine == line or pickedLine == line[::-1]:
          result += 1

print('Part 2: ', result)