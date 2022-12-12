import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

class Monkey:
  def __init__(self, items:list = [], operation:str = '', test: int = 1, true: int = 0, false: int = 0):
    self.items = list(items)
    self.operation = operation
    self.test = test
    self.true = true
    self.false = false
    self.inspectionNumber = 0
    self.delimiter = 1
  
  def __repr__(self):
    return str(self.items) + '  "' + self.operation + '" ' + str(self.test) + ' : ' + str(self.true) +' ? '+ str(self.false)
  
  def calculateOperation(self, withDivision: bool = True):
    self.inspectionNumber += 1
    value = self.items.pop(0)
    parts = self.operation.split(' ')
    operand = 0
    if parts[1] == 'old':
      operand = value
    else:
      operand = int(parts[1])
    if parts[0] == '+':
      return (value + operand) // 3 if withDivision else (value + operand)
    return (value * operand) // 3 if withDivision else (value * operand)

  def doTheTest(self, value, isPart2: bool = False):
    newValue = value % self.delimiter
    if value % self.test == 0:
      return [self.true, value if not isPart2 else newValue]
    return [self.false, value if not isPart2 else newValue]
  
  def addItem(self, value):
    self.items.append(value)
  
  def itemsLen(self):
    return len(self.items)

  def getInspectionNumber(self):
    return self.inspectionNumber

  def resetItems(self, items):
    self.items = list(items)
    self.inspectionNumber = 0

  def setDelimiter(self, value):
    self.delimiter = value
  
  def getTest(self):
    return self.test

# Part 1

monkeys: list = []

index = 0
while index < len(lines):
  index += 1
  parts = lines[index].split(': ')
  items = list(map(lambda x: int(x), parts[1].split(', ')))
  index += 1
  operator = lines[index].split('= old ')[1]
  index += 1
  test = int(lines[index].split(' by ')[1])
  index += 1
  true = int(lines[index].split(' monkey ')[1])
  index += 1
  false = int(lines[index].split(' monkey ')[1])
  index += 2
  monkeys.append(Monkey(items, operator, test, true, false))


for step in range(20):
  for monkey in monkeys:
    while monkey.itemsLen() > 0:
      item = monkey.calculateOperation()
      [index,item] = monkey.doTheTest(item)
      monkeys[index].addItem(item)

numbers = []
for monkey in monkeys:
  numbers.append(monkey.getInspectionNumber())
  numbers = sorted(numbers)[-2:]

print("Part 1: ", numbers[0]*numbers[1])

# Part 2

index = 0
delimiter = 1

for monkey in monkeys:
  index += 1
  parts = lines[index].split(': ')
  items = list(map(lambda x: int(x), parts[1].split(', ')))
  index += 6
  monkey.resetItems(items)
  delimiter *= monkey.getTest()

for monkey in monkeys:
  monkey.setDelimiter(delimiter)

for step in range(10000):
  if step % 1000 == 0:
    print(step)
  for monkey in monkeys:
    while monkey.itemsLen() > 0:
      item = monkey.calculateOperation(False)
      [index,item] = monkey.doTheTest(item, True)
      monkeys[index].addItem(item)

numbers = []
for monkey in monkeys:
  numbers.append(monkey.getInspectionNumber())
  numbers = sorted(numbers)[-2:]

print("Part 2: ", numbers[0]*numbers[1])