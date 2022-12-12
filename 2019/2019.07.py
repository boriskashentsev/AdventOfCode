import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

class Amplifier:
    def __init__(self, program, input):
        self.program = list(program)
        self.loc = 0
        self.output = []
        self.input = list(input)

    def run(self):
        ended = self.program[self.loc] == 99
        while not ended:
            instr = self.program[self.loc]
            de = instr % 100
            c = (instr // 100) % 10
            b = (instr // 1000) % 10
            a = (instr // 10000) % 10
            if (de == 1):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                self.program[self.program[self.loc+3]] = arg1 + arg2
                self.loc += 4
            elif (de == 2):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                self.program[self.program[self.loc+3]] = arg1 * arg2
                self.loc += 4
            elif (de == 3):
                if len(self.input) == 0:
                    break
                self.program[self.program[self.loc + 1]] = self.input.pop(0)
                self.loc += 2
            elif (de == 4):
                self.output.append(self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]])
                self.loc += 2
            elif (de == 5):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                if (arg1 != 0):
                    self.loc = arg2
                else: 
                    self.loc += 3
            elif (de == 6):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                if (arg1 == 0):
                    self.loc = arg2
                else: 
                    self.loc += 3
            elif (de == 7):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                self.program[self.program[self.loc + 3]] = 1 if (arg1 < arg2) else 0
                self.loc += 4
            elif (de == 8):
                arg1 = self.program[self.loc + 1] if (c == 1) else self.program[self.program[self.loc + 1]]
                arg2 = self.program[self.loc + 2] if (b == 1) else self.program[self.program[self.loc + 2]]
                self.program[self.program[self.loc + 3]] = 1 if (arg1 == arg2) else 0
                self.loc += 4
            ended = self.program[self.loc] == 99
        return ended

    def resetProgram(self, program):
        self.program = list(program)
    
    def flushOutput(self):
        output = list(self.output)
        self.output = []
        return output
    
    def appendInput(self, input):
        self.input += input


def bruteForce(program, sequence):
    result = [0]
    finished = False
    amps = []
    for i in range(len(sequence)):
        amps.append(Amplifier(program, [sequence[i]]))
    while not finished:
        for i in range(len(sequence)):
            amps[i].appendInput(result)
            ended = amps[i].run()
            result = amps[i].flushOutput()
            if i == len(sequence) - 1:
                finished = ended

    return result[0]


inpt = list(map(lambda x: int(x), input.split(',')))
maxResult = 0

for i in range(5):
    array1 = [0,1,2,3,4]
    result = []
    result.append(array1.pop(i))
    for j in range(4):
        array2 = array1[:]
        result.append(array2.pop(j))
        for k in range(3):
            array3 = array2[:]
            result.append(array3.pop(k))
            for l in range(2):
                array4 = array3[:]
                result.append(array4.pop(l))
                result.append(array4.pop(0))
                turnResult = bruteForce(inpt, result)
                if (turnResult > maxResult):
                    maxResult = turnResult
                result.pop()
                result.pop()
            result.pop()
        result.pop()
    result.pop()

print("Part 1: ", maxResult)

inpt = list(map(lambda x: int(x), input.split(',')))
maxResult = 0

for i in range(5):
    array1 = [5,6,7,8,9]
    result = []
    result.append(array1.pop(i))
    for j in range(4):
        array2 = array1[:]
        result.append(array2.pop(j))
        for k in range(3):
            array3 = array2[:]
            result.append(array3.pop(k))
            for l in range(2):
                array4 = array3[:]
                result.append(array4.pop(l))
                result.append(array4.pop(0))
                turnResult = bruteForce(inpt, result)
                if (turnResult > maxResult):
                    maxResult = turnResult
                result.pop()
                result.pop()
            result.pop()
        result.pop()
    result.pop()

print("Part 2: ", maxResult)