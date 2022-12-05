import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

stacks = []
wasEmptyLine = False

for line in lines:
  if line == '':
    wasEmptyLine = True
  elif not wasEmptyLine:
    if len(stacks) == 0:
      for i in range((len(line)+1)//4):
        stacks.append([])
    for i in range((len(line)+1)//4):
      index = i*4+1
      if(line[index] != ' '):
        stacks[i].insert(0, line[index])
  else:
    words = line.split(' ')
    amount = int(words[1])
    indexFrom = int(words[3])-1
    indexTo = int(words[5])-1
    for i in range(amount):
      stacks[indexTo].append(stacks[indexFrom].pop())

result = ''.join(list(map(lambda x: x[len(x)-1],stacks)))
print("Part 1: ", result)

# Part 2

stacks = []
wasEmptyLine = False

for line in lines:
  if line == '':
    wasEmptyLine = True
  elif not wasEmptyLine:
    if len(stacks) == 0:
      for i in range((len(line)+1)//4):
        stacks.append([])
    for i in range((len(line)+1)//4):
      index = i*4+1
      if(line[index] != ' '):
        stacks[i].insert(0, line[index])
  else:
    words = line.split(' ')
    amount = int(words[1])
    indexFrom = int(words[3])-1
    indexTo = int(words[5])-1
    buffer = []
    for i in range(amount):
      buffer.append(stacks[indexFrom].pop())
    while len(buffer)>0:
      stacks[indexTo].append(buffer.pop())

result = ''.join(list(map(lambda x: x[len(x)-1],stacks)))
print("Part 2: ", result)