# Part 1

inputNumber = 36000000

def part1():
    arraySize = inputNumber//2
    result = [1]*(arraySize)

    for i in range(2, inputNumber):
        for j in range(1,inputNumber//i):
            if i*j < arraySize:
                result[i*j] += i
                if j == 1:
                    if result[i]*10 >= inputNumber:
                        return i
        # Just to see that algorithm is working
        if i % 10000 == 0:
            print(i, result[i]*10)

print(part1())

# Part 2

def part2():
    arraySize = inputNumber//2
    result = [1]*(arraySize)

    for i in range(2, inputNumber):
        for j in range(1,51):
            if i*j < arraySize:
                result[i*j] += i
                if j == 1:
                    if result[i]*11 >= inputNumber:
                        return i
        # Just to see that algorithm is working
        if i % 10000 == 0:
            print(i, result[i]*11)

print(part2())