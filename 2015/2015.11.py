alphabet = "abcdefghijklmnopqrstuvwxyz"

def nextPassword(currentPassword):
    numbers = [alphabet.index(char) for char in currentPassword]
    index = len(numbers)-1
    increment = 1
    while increment > 0 and index >= 0:
        newIncrement = (numbers[index] + increment) // len(alphabet)
        numbers[index] = (numbers[index] + increment) % len(alphabet)
        increment = newIncrement
        index -= 1
    return ''.join([alphabet[number] for number in numbers])

def checkForThreeLetters(password):
    index = 0
    while index < len(password)-3:
        if alphabet.index(password[index]) + 1 == alphabet.index(password[index + 1]) and alphabet.index(password[index + 1]) + 1 == alphabet.index(password[index + 2]):
            return True
    return False

def checkNoOIL(password):
    exclude = "oil"
    checkValues = [False for char in exclude if char in password]
    return len(checkValues) == 0

def checkPairs(password):
    index = 0
    numberOfPairs = 0
    while index < len(password)-1:
        if (password[index] == password[index + 1]):
            numberOfPairs += 1
            index += 1
        index += 1
    return numberOfPairs > 1


def checkPassword(password):
    return checkForThreeLetters(password) and checkNoOIL(password) and checkPairs(password)

def nextPossiblePassword(password):
    newPassword = nextPassword(password)
    while not checkPassword(newPassword):
        newPassword = nextPassword(newPassword)
    return newPassword

#inputs = ["abcdefgh", "ghijklmn"]
inputs = ['vzbxkghb']

for input in inputs:
    nextPasswordString = nextPossiblePassword(input)
    print(input, '->', nextPasswordString)