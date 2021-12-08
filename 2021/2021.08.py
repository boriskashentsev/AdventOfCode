import sys
sys.path.append('./')
from utils.filename import calculateFileName
from functools import cmp_to_key

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
lines = input.split('\n')

# Part 1

result = 0

for line in lines:
    parts = line.split()
    neededDigits = parts[-4:]
    result += sum(list(map(lambda x: 1 if len(x) in [2,3,4,7] else 0, neededDigits)))

print(result)

# Part 2

def compare(item1, item2):
    if len(item1[0]) > len(item2[0]):
        return 1
    return -1

def contains(item1, item2):
    for element in item2:
        if element not in item1:
            return False
    return True

def minus(item1, items):
    result =''
    itemsTogether = ''.join(items)
    for element in item1:
        if element not in itemsTogether:
            result += element
    return result

result = 0

for line in lines:
    parts = line.split()
    code = list(map(lambda x: [x, -1],parts[:10]))
    code.sort(key = cmp_to_key(compare))
    # Simple numbers
    code[0][1] = 1
    code[2][1] = 4
    code[1][1] = 7 
    code[9][1] = 8
    # Looking for 9
    for i in range(6,9):
        if contains(code[i][0], code[2][0]):
            code[i][1] = 9
            break
    # Looking for 0
    for i in range(6,9):
        if code[i][1] == -1 and contains(code[i][0], code[0][0]):
            code[i][1] = 0
            break
    # Looking for 6
    for i in range(6,9):
        if code[i][1] == -1:
            code[i][1] = 6
    # Looking for 3
    for i in range(3, 6):
        if contains(code[i][0], code[0][0]):
            code[i][1] = 3
            break
    # Looking for 2:
    for i in range(3,6):
        if code[i][1] == -1 and contains(code[i][0], minus(code[9][0],[code[1][0], code[2][0]])):
            code[i][1] = 2
    # Looking for 5
    for i in range(3,6):
        if code[i][1] == -1:
            code[i][1] = 5

    neededDigits = parts[-4:]

    convertedDigit = 0
    for digit in neededDigits:
        for i in range(10):
            if minus(digit,[code[i][0]]) == '':
                convertedDigit = convertedDigit * 10 + code[i][1]
                break
    result += convertedDigit

print(result)