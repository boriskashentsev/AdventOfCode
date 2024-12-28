import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1


def comboOperand(value: int, register: dict) -> int:
    if value in [0, 1, 2, 3]:
        return value
    if value in [4, 5, 6]:
        registerOptions = "ABC"
        return register[registerOptions[value - 4]]
    if value == 7:
        print("Why the F***?")
        return -1


def runProgram(
    register: dict, program: list[int], checkSimilarity: bool = False
) -> str:
    index = 0
    isWorking = True
    outLine = []

    while isWorking:
        if index >= len(program):
            isWorking = False
        else:
            opcode = program[index]
            isJumped = False
            if opcode == 0:  # adv
                register["A"] = int(
                    register["A"] / pow(2, comboOperand(program[index + 1], register))
                )
            elif opcode == 1:  # bxl
                register["B"] ^= program[index + 1]
            elif opcode == 2:  # bst
                register["B"] = comboOperand(program[index + 1], register) % 8
            elif opcode == 3:  # jump
                if register["A"] != 0:
                    isJumped = True
                    index = program[index + 1]
            elif opcode == 4:  # bxc
                register["B"] ^= register["C"]
            elif opcode == 5:  # out
                outLine.append(comboOperand(program[index + 1], register) % 8)
                # print(outLine)
                if checkSimilarity:
                    outputIndex = len(outLine) - 1
                    if (
                        len(outLine) > len(program)
                        or outLine[outputIndex] != program[outputIndex]
                    ):
                        return "tryAgain!"
            elif opcode == 6:  # bdv
                register["B"] = int(
                    register["A"] / pow(2, comboOperand(program[index + 1], register))
                )
            elif opcode == 7:  # cdv
                register["C"] = int(
                    register["A"] / pow(2, comboOperand(program[index + 1], register))
                )
            if not isJumped:
                index += 2
    if checkSimilarity:
        if len(outLine) != len(program):
            return "tryAgain!"
    return ",".join(list(map(lambda x: str(x), outLine)))


[registerInput, programInput] = inputFile.split("\n\n")

register = {}

for line in registerInput.split("\n"):
    [_, name, value] = line.split(" ")
    register[name[0]] = int(value)

program = list(map(lambda x: int(x), programInput.split(" ")[1].split(",")))

print("Part 1: ", runProgram(register, program))


# Part 2 SLOW Stuff

# isRunning = True
# registerA = 8 * 8 * 5
# while isRunning:
#     for line in registerInput.split("\n"):
#         [_, name, value] = line.split(" ")
#         register[name[0]] = int(value)
#     register["A"] = registerA
#     result = runProgram(register, program)
#     if result != "tryAgain!":
#         isRunning = False
#     else:
#         registerA += 1

# print("Part 2: ", registerA)

# Part 2 Fast stuff


def goDeeper(registerInput: str, program: list[int], direction: int):
    programInput = ",".join(list(map(lambda x: str(x), program)))
    direction *= 8
    for line in registerInput.split("\n"):
        [_, name, value] = line.split(" ")
        register[name[0]] = int(value)
    for i in range(8):
        register["A"] = direction + i
        result = runProgram(register, program)
        # print(direction + i, ": ", result)
        if programInput == result:
            return direction + i
        elif programInput[-len(result) :] == result:
            recursionResult = goDeeper(registerInput, program, direction + i)
            if recursionResult > 0:
                return recursionResult
        elif len(result) > len(programInput):
            return -1
    return -1


result = goDeeper(registerInput, program, 0)

print("Part 2: ", result)
