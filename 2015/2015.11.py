alphabet = "abcdefghijklmnopqrstuvwxyz"
crippledAlphabet = "abcdefghjkmnpqrstuvwxyz"

def preparePassword(password):
    '''Prepare password at the start to exclude letters O, I and L'''
    numbers = [alphabet.index(char) for char in password]
    exclude = 'oil'
    excludeNumbers = [alphabet.index(char) for char in exclude]
    index =0
    while index < len(numbers):
        if numbers[index] in excludeNumbers:
            numbers[index] += 1
            index += 1
            while index < len(numbers):
                numbers[index] = 0
                index += 1
        else:
            index += 1
    return ''.join([alphabet[number] for number in numbers])

def nextPassword(currentPassword, alphabet):
    '''Generate next password by increasing characters by one (using special alphabet)'''
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
    '''Check that there is ne increasing straight of at least three letters '''
    index = 0
    while index < len(password)-3:
        if alphabet.index(password[index]) + 1 == alphabet.index(password[index + 1]) and alphabet.index(password[index + 1]) + 1 == alphabet.index(password[index + 2]):
            return True
        index += 1
    return False

def checkPairs(password):
    '''Check that there are at least two different, non-overlapping pairs of letters'''
    index = 0
    numberOfPairs = 0
    while index < len(password)-1:
        if (password[index] == password[index + 1]):
            numberOfPairs += 1
            index += 1
        index += 1
    return numberOfPairs > 1


def checkPassword(password):
    '''Wrapper-checker'''
    return checkForThreeLetters(password) and checkPairs(password)

def nextPossiblePassword(password):
    '''Generate next possible password accodring to checks'''
    newPassword = preparePassword(password)
    newPassword = nextPassword(newPassword, crippledAlphabet)
    while not checkPassword(newPassword):
        newPassword = nextPassword(newPassword, crippledAlphabet)
    return newPassword

# Test

#inputs = ["abcdefgh", "ghijklmn"]

# Part 1

#inputs = ['vzbxkghb']

#Part 2

inputs = ['vzbxxyzz']

for input in inputs:
    nextPasswordString = nextPossiblePassword(input)
    #nextPasswordString = preparePassword(input)
    print(input, '->', nextPasswordString)