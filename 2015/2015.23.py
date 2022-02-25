import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

def program(a, b, lines):
    lineIndex = 0
    isStillRunning = True

    while isStillRunning:
        parts = lines[lineIndex].split(' ')
        command = parts[0]
        if command == 'hlf':
            if parts[1] == 'a':
                a = a // 2
            elif parts[1] == 'b':
                b = b // 2
            else :
                print('Whaaat? HLF')
            lineIndex += 1
        elif command == 'tpl':
            if parts[1] == 'a':
                a = a * 3
            elif parts[1] == 'b':
                b = b * 3
            else :
                print('Whaaat? TPL')
            lineIndex += 1
        elif command == 'inc':
            if parts[1] == 'a':
                a = a + 1
            elif parts[1] == 'b':
                b = b + 1
            else :
                print('Whaaat? INC')
            lineIndex += 1
        elif command == 'jmp':
            lineIndex += int(parts[1])
        elif command == 'jie':
            register = a if parts[1][0] == 'a' else b
            if register % 2 == 0:
                lineIndex += int(parts[2])
            else :
                lineIndex += 1
        elif command == 'jio':
            register = a if parts[1][0] == 'a' else b
            if register == 1:
                lineIndex += int(parts[2])
            else :
                lineIndex += 1
        else:
            isStillRunning = False
        if lineIndex >= len(lines):
            isStillRunning = False
    
    return b

# Part 1

print('Part1', program(0, 0, lines))

# Part 2

print('Part2', program(1, 0, lines))