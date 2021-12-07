def validateLocation(location, keypad):
    shape = [len(keypad[0]), len(keypad)]
    for i in range(len(location)):
        if location[i] < 0 or location[i] >= shape[i]:
            return False
    if keypad[location[1]][location[0]] == ' ':
        return False
    return True

filename = "2016/02.input"
f = open(filename, "r")
input = f.read()

lines = input.split("\n")

directions = {'U':[0, -1], 'D':[0, 1], 'L':[-1, 0], 'R':[1, 0]}

# Part 1

keypad = ['123', '456', '789']

location = [1,1]
code=""

for line in lines:
    for instruction in line:
        for i in range(len(location)):
            location[i] += directions[instruction][i]
            if not validateLocation(location, keypad):
                location[i] -= directions[instruction][i]
    code += keypad[location[1]][location[0]]

print(code)

# Part 2

keypad = ['  1  ',' 234 ', '56789', ' ABC ', '  D  ']

location = [2,0]
code=""

for line in lines:
    for instruction in line:
        for i in range(len(location)):
            location[i] += directions[instruction][i]
            if not validateLocation(location, keypad):
                location[i] -= directions[instruction][i]
    code += keypad[location[1]][location[0]]

print(code)