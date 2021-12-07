import sys
import hashlib
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()
doorID = input

# Part 1

password = ''

index = 0
while len(password) < 8:
    line = doorID + str(index)
    md5hash = hashlib.md5(line.encode())
    #print(md5hash.hexdigest())
    if (md5hash.hexdigest().startswith('00000')):
        password += md5hash.hexdigest()[5]
        print(md5hash.hexdigest())
    index += 1

print(password)

# Part 2

def hasEmptyPositions(password):
    for char in password:
        if char == '_':
            return True
    return False

password = '________'

index = 0
while hasEmptyPositions(password):
    line = doorID + str(index)
    md5hash = hashlib.md5(line.encode())
    if (md5hash.hexdigest().startswith('00000')):
        location = md5hash.hexdigest()[5]
        if location in '01234567' and password[int(location)] == '_':
            char = md5hash.hexdigest()[6]
            password = password[:int(location)] + char + password[int(location) + 1 :]
            print(md5hash.hexdigest(), '->', password)
    index += 1

print(password)
