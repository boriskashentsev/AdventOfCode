filename = "2020/14.input"

f = open(filename, "r")

inpt = f.read().split("\n")

# first part

def binStringToNum(binString):
    result = 0
    for char in binString:
        result = 2 * result + int(char)
    return result

def numToBinString(number):
    result = ''
    while number > 0:
        binValue = number % 2
        result = str(binValue) + result
        number = (number - binValue) / 2
    return result

def applyMask(number, mask):
    strNumber = numToBinString(number)
    strNumber = list('0'*(len(mask)-len(strNumber))+strNumber)
    for i in range(len(mask)):
        if mask[i] != 'X':
            strNumber[i] = mask[i]
    
    strNumber = "".join(strNumber)
    return (binStringToNum(strNumber))

mask = ''
memory = {}

for line in inpt:
    parts = line.split(' ')
    if parts[0] == 'mask':
        mask = parts[2]
    else:
        memory[parts[0]] = applyMask (int(parts[2]), mask)

result = 0
for key in memory.keys():
    result = result + memory[key]

print(result)

# second part

def applyMaskToAddress(number, mask):
    strNumber = numToBinString(number)
    strNumber = list('0'*(len(mask)-len(strNumber))+strNumber)
    for i in range(len(mask)):
        if mask[i] in '1X':
            strNumber[i] = mask[i]
    strNumber = "".join(strNumber)
    return strNumber

def applyValueToMemory(strAddress, value, memory):
    if 'X' in strAddress:
        index = strAddress.index('X')
        for switch in ['0','1']:
            strAddress[index] = switch
            applyValueToMemory(strAddress, value, memory)
        strAddress[index] = 'X'
    else:
        memory[''.join(strAddress)] = value

mask = ''
memory = {}

for line in inpt:
    parts = line.split(' ')
    if parts[0] == 'mask':
        mask = parts[2]
    else:
        address = int(parts[0][4:len(parts[0])-1])
        value = int(parts[2])
        strAddress = applyMaskToAddress(address, mask)
        applyValueToMemory(list(strAddress), value, memory)

result = 0
for key in memory.keys():
    result = result + memory[key]

print(result)