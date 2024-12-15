import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

register = {}
playedSound = 0
recoveredSound = 0

codeLines = input.split("\n")
lineIndex = 0
isRunning = True

while isRunning:
    command = codeLines[lineIndex].split(" ")
    match command[0]:
        case "set":
            if (
                not command[2].lstrip("-").isnumeric()
                and command[2] not in register.keys()
            ):
                register[command[2]] = 0
            register[command[1]] = (
                int(command[2])
                if command[2].lstrip("-").isnumeric()
                else register[command[2]]
            )
        case "add":
            if command[1] not in register.keys():
                register[command[1]] = 0
            if (
                not command[2].lstrip("-").isnumeric()
                and command[2] not in register.keys()
            ):
                register[command[2]] = 0
            register[command[1]] += (
                int(command[2])
                if command[2].lstrip("-").isnumeric()
                else register[command[2]]
            )
        case "mul":
            if command[1] not in register.keys():
                register[command[1]] = 0
            if (
                not command[2].lstrip("-").isnumeric()
                and command[2] not in register.keys()
            ):
                register[command[2]] = 0
            register[command[1]] *= (
                int(command[2])
                if command[2].lstrip("-").isnumeric()
                else register[command[2]]
            )
        case "mod":
            if command[1] not in register.keys():
                register[command[1]] = 0
            if (
                not command[2].lstrip("-").isnumeric()
                and command[2] not in register.keys()
            ):
                register[command[2]] = 0
            register[command[1]] %= (
                int(command[2])
                if command[2].lstrip("-").isnumeric()
                else register[command[2]]
            )
        case "snd":
            playedSound = (
                int(command[1])
                if command[1].lstrip("-").isnumeric()
                else register[command[1]]
            )
        case "rcv":
            if (command[1].lstrip("-").isnumeric() and int(command[1]) > 0) or register[
                command[1]
            ] != 0:
                recoveredSound = playedSound
                isRunning = False
                break
        case "jgz":
            if (command[1].lstrip("-").isnumeric() and int(command[1]) > 0) or register[
                command[1]
            ] > 0:
                lineIndex -= 1
                lineIndex += (
                    int(command[2])
                    if command[2].lstrip("-").isnumeric()
                    else register[command[2]]
                )
        case _:
            print("Which command??? ", command[0])
    lineIndex += 1
    if lineIndex not in range(len(codeLines)):
        isRunning = False

print("Part 1: ", recoveredSound)


# Part 2
