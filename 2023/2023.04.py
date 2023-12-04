import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

def lineToNumbers(str):
  return list(map(lambda n: int(n) if n != '' else -1, str.split(' ')))

result = 0

for line in lines:
  numbersOnCard = line.split(': ')[1].split(' | ')
  winningNumbers = lineToNumbers(numbersOnCard[0])
  elfNumbers = lineToNumbers(numbersOnCard[1])
  score = 0
  for number in elfNumbers:
    if number > 0 and number in winningNumbers:
      if score == 0:
        score = 1
      else:
        score *= 2
  result += score

print('Part 1:', result)

# Part 2

result = 0
cards = [1] * len(lines)

for i in range(len(lines)):
  line = lines[i]
  numbersOnCard = line.split(': ')[1].split(' | ')
  winningNumbers = lineToNumbers(numbersOnCard[0])
  elfNumbers = lineToNumbers(numbersOnCard[1])
  score = 0
  for number in elfNumbers:
    if number > 0 and number in winningNumbers:
      score += 1
  for j in range(1, score + 1):
    if i+j >= len(lines):
      break
    cards[i + j] +=  cards[i]

print('Part 2:', sum(cards))