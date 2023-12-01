import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

summ = 0
numbers = '0123456789'

for line in lines:
  first = -1
  last = -1
  for element in line:
    if element in numbers:
      last = numbers.index(element)
      if first < 0:
        first = numbers.index(element)
  summ += first*10 + last

print('Part 1: ', summ)

# Part 2

summ = 0
numbers = '0123456789'
spelledNumbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
  first = -1
  last = -1
  
  # first number
  i = 0
  while i < len(line):
    flag = False
    for num in spelledNumbers:
      if line[i: i+len(num)] == num:
        first = spelledNumbers.index(num)
        flag = True
        break
    if flag:
      break
    if not flag:
      if line[i] in numbers:
        first = numbers.index(line[i])
        break
    i += 1

  # last number
  i = len(line)
  while i > 0:
    flag = False
    for num in spelledNumbers:
      if line[i-len(num): i] == num:
        last = spelledNumbers.index(num)
        flag = True
        break
    if flag:
      break
    if not flag:
      if line[i-1] in numbers:
        last = numbers.index(line[i-1])
        break
    i -= 1
  summ += first*10 + last

print('Part 2: ', summ)