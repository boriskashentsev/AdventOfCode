import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

def isCaught(depth, delay):
  return (delay % ((depth-1)*2)) == 0

severity = 0
for line in lines:
  numbers = [int(num) for num in line.split(': ')]
  if isCaught(numbers[1], numbers[0]):
    severity += numbers[0]*numbers[1]

print("Part 1: ", severity)

# Part 2

gotCaught = True
delay = -1

while gotCaught:
  gotCaught = False
  delay += 1
  for line in lines:
    numbers = [int(num) for num in line.split(': ')]
    if isCaught(numbers[1], numbers[0] + delay):
      gotCaught = True
      break

print("Part 2: ", delay)