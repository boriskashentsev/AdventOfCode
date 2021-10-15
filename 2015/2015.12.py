numbers = "0123456789-"
filename = "2015/12.input"

f = open(filename, "r")

input = f.read()

index = 0
result = 0
while index < len(input):
    if input[index] in numbers:
        number = 0
        sign = 1
        while input[index] in numbers:
            if input[index] == '-':
                sign = -1
            else:
                number = number * 10 + int(numbers.index(input[index]))
            index += 1
        result += sign * number
        index -= 1
    index += 1

print(result)