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


