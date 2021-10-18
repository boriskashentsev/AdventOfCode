numbers = "0123456789-"
filename = "2015/12.input"

f = open(filename, "r")

input = f.read()

# Part 1

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

# Part 2

def parseNumber(line, index):
    number = 0
    sign = 1
    while line[index] in numbers:
        if line[index] == '-':
            sign = -1
        else:
            number = number * 10 + int(numbers.index(line[index]))
        index += 1
    index -= 1
    return sign * number, index

def parseString(line, index):
    index +=1
    string = ''
    while(line[index] != '"'):
        string += line[index]
        index += 1
    return string, index

def parseArray(line, index):
    array = []
    index += 1
    while line[index] != ']':
        if line[index] in numbers:
            number, index = parseNumber(line, index)
            array.append(number)
        elif line[index] == '"':
            string, index = parseString(line, index)
            array.append(string)
        elif line [index] == '[':
            newArray, index = parseArray(line, index)
            array.append(newArray)
        elif line [index] == '{':
            dictionary, index = parseObject(line, index)
            array.append(dictionary)
        index += 1
    return array, index

def parseObject(line, index):
    dictionary = {}
    index += 1
    while line[index] != '}':
        # Key - Always a string
        if line[index] == '"':
            key, index = parseString(line, index)
        else:
            print('Are you sure key can be something else than a string?')
        # Colon 
        index += 1
        if line [index] != ':':
            print('Object is constructed wrongly')
        # Value
        index += 1
        value = []
        if line[index] in numbers:
            number, index = parseNumber(line, index)
            value.append(number)
        elif line[index] == '"':
            string, index = parseString(line, index)
            value.append(string)
        elif line [index] == '[':
            newArray, index = parseArray(line, index)
            value.append(newArray)
        elif line [index] == '{':
            newDictionary, index = parseObject(line, index)
            value.append(newDictionary)
        index += 1
        # Possible comma
        if line[index] == ',':
            index += 1
        dictionary[key] = value[0]

    return dictionary, index

def parseLine(line):
    result = []
    if line[0] == '{':
        result.append(parseObject(line, 0)[0])
    elif line[0] == '[':
        result.append(parseArray(line, 0)[0])
    else:
        print('Are you sure the line is correct?')
    return result

def countSum(myObject, excludeValue):
    result = 0
    if isinstance(myObject, dict):
        if(excludeValue in myObject.values()):
            return 0
        else:
            for key in myObject.keys():
                result += countSum(myObject[key], excludeValue)
    elif isinstance(myObject,list):
        for element in myObject:
            result += countSum(element, excludeValue)
    elif isinstance(myObject, str):
        return 0
    elif isinstance(myObject, int):
        return myObject
    else:
        print ('And what are you?')
    return result

#input = '[1,{"c":"red","b":2},3]' # Input for testing
excludeValue = 'red'

parsedObject = parseLine(input)[0]

result = countSum(parsedObject, excludeValue)
print(result)