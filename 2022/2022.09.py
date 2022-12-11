import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

def findNewTailLocation(head, tail):
  if pow(head[0]-tail[0],2) + pow(head[1]-tail[1], 2) > 2:
    if pow(head[0]-tail[0],2) + pow(head[1]-tail[1], 2) == 8:
      tail[0] += (head[0]-tail[0]) // 2
      tail [1] += (head[1] -tail[1]) // 2
    elif pow(head[0]-tail[0],2) == 4:
      tail[0] += (head[0]-tail[0]) // 2
      tail[1] = head[1]
    elif pow(head[1]-tail[1], 2) == 4:
      tail [1] += (head[1] -tail[1]) // 2
      tail[0] = head[0]
    else:
      print(head, tail)
      print(">>> What?!")
      return
  return tail

head = [0,0]
tail = [0,0]

allTailLocations:list = [[0,0]]

for line in lines:
  parts = line.split(' ')
  axis = 0
  sign = 1
  if parts[0] in 'RL':
    axis = 1
  if parts[0] in 'LD':
    sign = -1
  steps = int(parts[1])
  for i in range(steps):
    head[axis] += sign
    tail = findNewTailLocation(head, tail)
    if tail not in allTailLocations:
      allTailLocations.append(list(tail))
  
print("Part 1: ", len(allTailLocations))

# Part 2

ropeLength = 10
rope=[]
for i in range(ropeLength):
  rope.append([0,0])

allTailLocations:list = [[0,0]]

for line in lines:
  parts = line.split(' ')
  axis = 0
  sign = 1
  if parts[0] in 'RL':
    axis = 1
  if parts[0] in 'LD':
    sign = -1
  steps = int(parts[1])
  for i in range(steps):
    rope[0][axis] += sign
    for j in range(1, len(rope)):
      rope[j] = findNewTailLocation(rope[j-1], rope[j])
      if rope[j] == None:
        print(line)
        print(rope)
        print(i)
    if rope[-1] not in allTailLocations:
      allTailLocations.append(list(rope[-1]))

print("Part 2: ", len(allTailLocations))