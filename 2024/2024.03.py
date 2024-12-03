import sys
from re import findall

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def calculateMul(input):
  allInstances = findall("mul[(]\\d{1,3},\\d{1,3}[)]", input)
  result = 0
  for instance in allInstances:
    numbers = findall("\\d{1,3}", instance)
    result += int(numbers[0])*int(numbers[1])
  return result

print("Part 1: ", calculateMul(input))

# Part 2

DOs = input.split('do()')

result = 0
for do in DOs:
  calculatables = do.split("don't()")[0]
  result += calculateMul(calculatables)

print("Part 2: ", result)
