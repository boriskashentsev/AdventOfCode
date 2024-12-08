import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

def calculateSumLeftToRight(numbers: list, signs: str) -> int:
  result = numbers[0]
  for i in range(len(signs)):
    if signs[i] == '*':
      result *= numbers[i+1]
    elif signs[i] == '+':
      result += numbers[i+1]
    elif signs[i] == '|':
      result = int(str(result)+str(numbers[i+1]))
    else:
      print('What? Where? How?')
  return(result)

def generateSum(sum: int, numbers: list, listOfSigns: str, signs: str) -> bool:
  if len(signs) == len(numbers) - 1:
    return sum == calculateSumLeftToRight(numbers, signs)
  else:
    for sign in listOfSigns:
      if generateSum(sum, numbers, listOfSigns, signs+sign):
        return True
  return False
      

def isPossibleSum(sum: int, numbers: list, listOfSigns) -> bool:
  return generateSum(sum, numbers, listOfSigns, '')

result = 0
for line in input.split('\n'):
  [sum, rest] = line.split(': ')
  sum = int(sum)
  numbers = list(map(lambda x: int(x), rest.split(' ')))
  if(isPossibleSum(sum, numbers, '*+')):
    result += sum

print("Part 1: ", result)

# Part 2

result = 0
for line in input.split('\n'):
  [sum, rest] = line.split(': ')
  sum = int(sum)
  numbers = list(map(lambda x: int(x), rest.split(' ')))
  if(isPossibleSum(sum, numbers, '*+|')):
    result += sum

print("Part 2: ", result)