def generateSequence(input, itterations):
    lineOriginal = input
    for i in range(itterations):
        constractedLine = ""
        j=0
        while j < len(lineOriginal):
            char = lineOriginal[j]
            repeat = 1
            j += 1
            while j < len(lineOriginal) and lineOriginal[j]==char:
                j += 1
                repeat += 1
            constractedLine += str(repeat)+char
        lineOriginal = constractedLine
    return(lineOriginal)

inputs = ["1", "11", "21", "1211", "111221","3113322113"]

# Part 1

itterations = 40

for input in inputs:
    result = generateSequence(input, itterations)
    print(len(result))


# Part 2

itterations = 50

for input in inputs:
    result = generateSequence(input, itterations)
    print(len(result))
