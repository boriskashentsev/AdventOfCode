import sys

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1

lines = list(map(lambda x: x.split('   '), input.split('\n')))

left = list(map(lambda x: int(x[0]), lines))
right = list(map(lambda x: int(x[1]), lines))

left.sort()
right.sort()

result = 0
for i in range(len(left)):
  result += abs(left[i]-right[i])

print("Part 1:", result)

# Part 2

rightHistogram = {}
for i in range(len(right)):
  if right[i] in rightHistogram.keys():
    rightHistogram[right[i]] += 1
  else:
    rightHistogram[right[i]] = 1

result = 0
for i in range(len(left)):
  if left[i] in rightHistogram.keys():
    result += left[i] * rightHistogram[left[i]]

print("Part 2:", result)