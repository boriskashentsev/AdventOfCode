import sys
sys.path.append('./')

from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

class FancyList:
  def __init__(self, inputList) -> None:
    self.list = list(inputList)
  
  def addZeros(self, index) -> None:
    if index >= len(self.list):
      extraZeros = index - len(self.list) + 1
      self.list += list([0]*extraZeros)  

  def getValue(self, index) -> int:
    return 0 if index >= len(self.list) else self.list[index]
  
  def setValue(self, index, value) -> None:
    self.addZeros(index)
    self.list[index] = value
  
  def getList(self, start:int = 0, end:int = 0) -> list:
    if end == 0:
      return self.list
    else:
      return self.list[start: end]

class Intcode:
  def __init__(self, program: list = [], input: list = []) -> None:
    self.program:FancyList = FancyList(program)
    self.loc = 0
    self.rBase = 0 # relative base
    self.output = []
    self.input = list(input)

  def argumentValue(self, mode, offset) -> int:
    if mode == 0:
      return self.program.getValue(self.program.getValue(self.loc + offset))
    elif mode == 1:
      return self.program.getValue(self.loc + offset)
    else:
      return self.program.getValue(self.program.getValue(self.loc + offset)+self.rBase)
  
  def argumentValueForSet(self, mode, offset) -> int:
    if mode == 2:
      return self.program.getValue(self.loc + offset)+self.rBase
    elif mode == 0:
      return self.program.getValue(self.loc + offset)
    else :
      print("!!!!! HOW ??????")
      return -1

  def run(self) -> bool:
    ended = self.program.getValue(self.loc) == 99
    operations = 0
    while not ended:
      operations += 1
      instr = self.program.getValue(self.loc)
      de = instr % 100
      c = (instr // 100) % 10
      b = (instr // 1000) % 10
      a = (instr // 10000) % 10
      if (de == 1):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        arg3 = self.argumentValueForSet(a,3)
        self.program.setValue(arg3, arg1 + arg2)
        self.loc += 4
      elif (de == 2):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        arg3 = self.argumentValueForSet(a,3)
        self.program.setValue(arg3, arg1 * arg2)
        self.loc += 4
      elif (de == 3):
        if len(self.input) == 0:
          print("INPUT IS EMPTY")
          break
        arg1 = self.argumentValueForSet(c, 1)
        self.program.setValue(arg1, self.input.pop(0))
        self.loc += 2
      elif (de == 4):
        self.output.append(self.argumentValue(c, 1))
        self.loc += 2
      elif (de == 5):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        if (arg1 != 0):
          self.loc = arg2
        else:
          self.loc += 3
      elif (de == 6):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        if (arg1 == 0):
          self.loc = arg2
        else:
          self.loc += 3
      elif (de == 7):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        arg3 = self.argumentValueForSet(a, 3)
        self.program.setValue(arg3, 1 if (arg1 < arg2) else 0)
        self.loc += 4
        
      elif (de == 8):
        arg1 = self.argumentValue(c, 1)
        arg2 = self.argumentValue(b, 2)
        arg3 = self.argumentValueForSet(a, 3)
        self.program.setValue(arg3, 1 if (arg1 == arg2) else 0)
        self.loc += 4
      elif (de == 9):
        arg1 = self.argumentValue(c, 1)
        self.rBase += arg1
        self.loc += 2
      ended = self.program.getValue(self.loc) == 99
    return ended

  def flushOutput(self) -> list:
    output = list(self.output)
    self.output = []
    return output

program = list(map(lambda x: int(x), input.split(',')))

machine = Intcode(program, [1])

machine.run()

print("Part 1: ", machine.flushOutput())

# Part 2

machine = Intcode(program, [2])

machine.run()

print("Part 2: ", machine.flushOutput())