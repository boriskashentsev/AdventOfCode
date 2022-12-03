import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

prioritySum = 0

for line in lines:
  array = [0]*len(alphabet)
  first = line[:len(line)//2]
  second = line[len(line)//2:]
  for char in first:
    array[alphabet.find(char)] = 1
  repeatingChar=' '
  for char in second:
    if array[alphabet.find(char)] == 1:
      repeatingChar = char
      break
  prioritySum += alphabet.find(repeatingChar) + 1

print("Part 1: ", prioritySum)

# Part 2

prioritySum = 0

for i in range(len(lines)//3):
  array = [0]*len(alphabet)
  repeatingChar = ''
  for j in range(3):
    line = lines[i*3 + j]
    for char in line:
      if array[alphabet.find(char)] == j:
        array[alphabet.find(char)] = j + 1
        if array[alphabet.find(char)] == 3:
          repeatingChar = char
          break
    if repeatingChar != '':
      break
  prioritySum += alphabet.find(repeatingChar) + 1

print("Part 2: ", prioritySum)
