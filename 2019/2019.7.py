def solver (instructions, user_input):
    loc = 0
    result = []
    while (instructions[loc] != 99):
        instr = instructions[loc]
        de = instr % 100
        c = (instr // 100) % 10
        b = (instr // 1000) % 10
        a = (instr // 10000) % 10
        if (de == 1):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            instructions[instructions[loc+3]] = arg1 + arg2
            loc += 4
        elif (de == 2):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            instructions[instructions[loc+3]] = arg1 * arg2
            loc += 4
        elif (de == 3):
            instructions[instructions[loc + 1]] = user_input.pop(0)
            loc += 2
        elif (de == 4):
            result.append(instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]])
            loc += 2
        elif (de == 5):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            if (arg1 != 0):
                loc = arg2
            else: 
                loc += 3
        elif (de == 6):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            if (arg1 == 0):
                loc = arg2
            else: 
                loc += 3
        elif (de == 7):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            instructions[instructions[loc + 3]] = 1 if (arg1 < arg2) else 0
            loc += 4
        elif (de == 8):
            arg1 = instructions[loc + 1] if (c == 1) else instructions[instructions[loc + 1]]
            arg2 = instructions[loc + 2] if (b == 1) else instructions[instructions[loc + 2]]
            instructions[instructions[loc + 3]] = 1 if (arg1 == arg2) else 0
            loc += 4
        #print instructions
    return result

def bruteForce(program, sequence):
    result = 0
    for i in sequence:
        instr = program[:]
        result = solver(instr, [i, result])[0]
    return result


# inpt = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# inpt = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# inpt = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
inpt = [3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]
num = 0

maxResult = 0

for i in range(5):
    array1 = [0, 1,2,3,4]
    result = []
    result.append(array1.pop(i))
    for j in range(4):
        array2 = array1[:]
        result.append(array2.pop(j))
        for k in range(3):
            array3 = array2[:]
            result.append(array3.pop(k))
            for l in range(2):
                array4 = array3[:]
                result.append(array4.pop(l))
                result.append(array4.pop(0))
                num += 1
                print "Step", num
                turnResult = bruteForce(inpt, result)
                if (turnResult > maxResult):
                    maxResult = turnResult
                result.pop()
                result.pop()
            result.pop()
        result.pop()
    result.pop()

print maxResult