def followsRules(num):
    notNum = str(num)
    check = False
    for i in range(len(notNum) - 1):
        if notNum[i] > notNum[i+1]:
            return False
        elif notNum[i] == notNum[i+1]:
            check = True
    return check

def followsDifferentRules(num):
    notNum = str(num)
    check = False
    i=0
    while i < len(notNum)-1:
        if notNum[i] > notNum[i+1]:
            return False
        elif notNum[i] == notNum[i+1]:
            repeat = 0
            while i < len(notNum)-1 and notNum[i] == notNum[i+1]:
                repeat += 1
                i += 1
            if repeat == 1:
                check = True
            i -= 1
        i += 1
    return check

# num = 123789
# print followsRules(num)

# result = 0
# for i in range(382345, 843167):
#     if (followsRules(i)):
#         result += 1
# print "***Result***"
# print result


# num = 111122
# print followsDifferentRules(num)

result = 0
for i in range(382345, 843167):
    if (followsDifferentRules(i)):
        result += 1
print "***Result***"
print result