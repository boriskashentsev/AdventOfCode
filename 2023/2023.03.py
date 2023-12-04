import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

numbers = '0123456789'

result = 0

for i in range(len(lines)):
  line = lines[i]
  j = 0
  while j < len(line):
    if line[j] in numbers:
      number = 0
      surrounding = ''
      if j > 0:
        if i > 0:
          surrounding += lines[i-1][j-1]
        surrounding += lines[i][j-1]
        if i < len(lines)-1:
          surrounding += lines[i+1][j-1]
      while line[j] in numbers:
        number = number*10 + int(line[j])
        if i > 0:
          surrounding += lines[i-1][j]
        if i < len(lines)-1:
          surrounding += lines[i+1][j]
        j += 1
        if j >= len(line):
          break
      if j < len(line):
        if i > 0:
          surrounding += lines[i-1][j]
        surrounding += lines[i][j]
        if i < len(lines)-1:
          surrounding += lines[i+1][j]
      if surrounding.count('.') != len(surrounding):
        result += number
    j += 1

print('Part 1:', result)

# Part 2

dx = [0, 1, -1, 1,  0,  1, -1, -1]
dy = [1, 1,  1, 0, -1, -1, -1,  0]

result = 0

for i in range(len(lines)):
  line = lines[i]
  for j in range(len(line)):
    if line[j] == '*':
      di = 0
      numbersForMultiplication = []
      while di < len(dx):
        y = i + dy[di]
        x = j + dx[di]
        isNumber = False
        if y in range(len(lines)) and x in range(len(lines[y])):
          if lines[y][x] in numbers:
            isNumber = True
            # find start of the number
            newJ = x
            while newJ >= 0 and lines[y][newJ] in numbers:
              newJ -= 1
            newJ += 1
            number = 0
            while newJ < len(lines[y]) and lines[y][newJ] in numbers:
              number = number * 10 + int(lines[y][newJ])
              newJ += 1
            numbersForMultiplication.append(number)
        if isNumber and di % 4 == 0:
          di += 2
        di += 1
      if len(numbersForMultiplication) == 2:
        result += numbersForMultiplication[0] * numbersForMultiplication[1]

print("Part 2:", result)

