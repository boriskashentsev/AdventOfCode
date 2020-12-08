filename = "2020/8.input"

f = open(filename, "r")

inpt = f.read().split("\n")

instructions = []

for line in inpt:
    parts = line.split(" ")
    instructions.append([parts[0], int(parts[1])])

#first part

lines = []
accumulator = 0
line = 0
while line not in lines:
    lines.append(line)
    if instructions[line][0] == "nop":
        line = line + 1
    elif instructions[line][0] == "acc":
        accumulator = accumulator + instructions[line][1]
        line = line + 1
    elif instructions[line][0] == "jmp":
        line = line + instructions[line][1]

print(accumulator)

#second part

eoi = False # end of instructions
il = False # infinite loop
ltc = 0 # line to change
while not eoi:
    lines = []
    accumulator = 0
    line = 0
    il = False

    # instruction change
    while instructions[ltc][0] not in ["nop", "jmp"]:
        ltc = ltc + 1
    
    if instructions[ltc][0] == "nop":
        instructions[ltc][0] = "jmp"
    else:
        instructions[ltc][0] = "nop"
    
    # check for infinite loop
    while not il and not eoi:
        lines.append(line)
        if instructions[line][0] == "nop":
            line = line + 1
        elif instructions[line][0] == "acc":
            accumulator = accumulator + instructions[line][1]
            line = line + 1
        elif instructions[line][0] == "jmp":
            line = line + instructions[line][1]
        
        if line in lines:
            il = True
        if line >= len(instructions):
            eoi = True
    
    # restore instruction
    if instructions[ltc][0] == "nop":
        instructions[ltc][0] = "jmp"
    else:
        instructions[ltc][0] = "nop"
    ltc = ltc + 1

print(accumulator)