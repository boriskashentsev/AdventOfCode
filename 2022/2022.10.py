import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

importantCycles = [20, 60, 100, 140, 180, 220]
signalStrength = 0
registerValue = 1
cycle = 0

def increaseCycleAndCalculateSignal(cycle, value, signal):
  cycle += 1
  if cycle in importantCycles:
    signal += cycle * value
  return [cycle, signal]

for line in lines:
  parts = line.split(' ')
  if cycle > importantCycles[-1]:
    break
  if parts[0] == 'noop':
    [cycle, signalStrength] = increaseCycleAndCalculateSignal(cycle, registerValue, signalStrength)
  elif parts[0] == 'addx':
    [cycle, signalStrength] = increaseCycleAndCalculateSignal(cycle, registerValue, signalStrength)
    [cycle, signalStrength] = increaseCycleAndCalculateSignal(cycle, registerValue, signalStrength)
    registerValue += int(parts[1])

print("Part 1: ", signalStrength)

# Part 2

def increaseCycle(cycle, value, crtLine):
  if len(crtLine) in range(value-1, value+2):
    crtLine.append('#')
  else:
    crtLine.append('.')
  cycle += 1
  return [cycle, crtLine]

registerValue = 1
cycle = 0
result:list = []
crtLine:list = []

for line in lines:
  parts = line.split(' ')
  if cycle > 240:
    break
  if parts[0] == 'noop':
    [cycle, crtLine] = increaseCycle(cycle, registerValue, crtLine)
    if len(crtLine)==40:
      result.append(''.join(crtLine))
      crtLine = []
  elif parts[0] == 'addx':
    [cycle, crtLine] = increaseCycle(cycle, registerValue, crtLine)
    if len(crtLine)==40:
      result.append(''.join(crtLine))
      crtLine = []
    [cycle, crtLine] = increaseCycle(cycle, registerValue, crtLine)
    if len(crtLine)==40:
      result.append(''.join(crtLine))
      crtLine = []
    registerValue += int(parts[1])

print("Part 2:")
for i in range(len(result)):
  print(result[i])