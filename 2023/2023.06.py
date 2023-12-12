import sys
sys.path.append('./')
from utils.filename import calculateFileName

from re import findall

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

def solver(times, distances): 
  result = 1

  for i in range(len(times)):
    count = 0
    for j in range(1, times[i]):
      if(j * (times[i] - j) > distances[i]):
        count += 1
    result *= count
  return result

time = list(map(lambda x: int(x), findall('\d+', lines[0].split(':')[1])))
distance = list(map(lambda x: int(x), findall('\d+', lines[1].split(':')[1])))

print("Part 1: ", solver(time, distance))

# Part 2

time = [int(''.join(lines[0].split(':')[1].split(' ')))]
distance = [int(''.join(lines[1].split(':')[1].split(' ')))]

print("Part 2: ", solver(time, distance))