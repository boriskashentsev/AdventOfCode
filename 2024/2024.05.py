import sys
from re import findall

sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

# Part 1 & 2

[orders, manuals] = input.split('\n\n')

donts = {}
for order in orders.split('\n'):
  [left, right] = order.split('|')
  if right in donts.keys():
    donts[right] += [left]
  else:
    donts[right] = [left]

def correctPages(pages, donts):
  i = 0
  newPages = [*pages]
  while i < len(newPages)-1:
    printingPage = newPages[i]
    isCorrect = True
    for j in range(i+1, len(newPages)):
      if printingPage in donts.keys() and newPages[j] in donts[printingPage]:
        isCorrect = False
        break
    if not isCorrect:
      for j in reversed(range(i+1, len(newPages))):
        if printingPage in donts.keys() and newPages[j] in donts[printingPage]:
          newPages= newPages[:j+1] + [printingPage] + newPages[j+1:]
          break
      newPages = newPages[:i] + newPages[i+1:]
    else: 
      i += 1
  return(int(newPages[int(len(newPages)/2)]))

result1 = 0
result2 = 0
for manual in manuals.split('\n'):
  pages = manual.split(',')
  isCorrectOrder = True
  for i in range(len(pages)-1):
    printingPage = pages[i]
    for j in range(i+1, len(pages)):
      if printingPage in donts.keys() and pages[j] in donts[printingPage]:
        isCorrectOrder = False
        break
    if not isCorrectOrder:
      break
  if isCorrectOrder:
    result1 += int(pages[int(len(pages)/2)])
  else:
    result2 += correctPages(pages, donts)

print('Part 1: ', result1)
print('Part 2: ', result2)
