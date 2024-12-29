import sys

sys.path.append("./")
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
inputFile = f.read()

# Part 1


def rebuildDictionary(dictionary: list[str]) -> dict:
    result = {}
    for word in dictionary:
        letterDictionary = result
        for letter in word:
            if letter in letterDictionary.keys():
                letterDictionary = letterDictionary[letter]
            else:
                tempDictionary = {}
                letterDictionary[letter] = tempDictionary
                letterDictionary = tempDictionary
    return result


def checkWordsValidity(word: str, dictionary: dict, impossibleWords: list[str]) -> bool:
    if word == "":
        return True

    index = 0
    letterDictionary = dictionary
    while True:
        if "," in letterDictionary.keys():
            if word[index:] not in impossibleWords:
                if checkWordsValidity(word[index:], dictionary, impossibleWords):
                    return True
                else:
                    impossibleWords.append(word[index:])
        if index >= len(word):
            return False
        letter = word[index]
        if letter in letterDictionary.keys():
            letterDictionary = letterDictionary[letter]
            index += 1
        else:
            return False


def countWordsPermutation(
    word: str, dictionary: dict, impossibleWords: list[str], countedWords: dict
) -> int:
    if word == "":
        return 1
    if word in impossibleWords:
        return 0
    index = 0
    letterDictionary = dictionary
    result = 0
    isRunning = True
    while isRunning:
        if "," in letterDictionary.keys():
            if word[index:] not in impossibleWords:
                if word[index:] in countedWords.keys():
                    result += countedWords[word[index:]]
                else:
                    value = countWordsPermutation(
                        word[index:], dictionary, impossibleWords, countedWords
                    )
                    result += value
                    countedWords[word[index:]] = value
        if index >= len(word):
            isRunning = False
        else:
            letter = word[index]
            if letter in letterDictionary.keys():
                letterDictionary = letterDictionary[letter]
                index += 1
            else:
                isRunning = False
    return result


[dictionary, words] = inputFile.split("\n\n")

dictionary = dictionary.split(" ")
dictionary[-1] += ","
words = words.split("\n")

fancyDictionary = rebuildDictionary(dictionary)
result1 = 0
result2 = 0
impossibleWords = []
countedWords = {}
for i in range(len(words)):
    word = words[i]
    isValid = checkWordsValidity(word, fancyDictionary, impossibleWords)
    result1 += 1 if isValid else 0
    if isValid:
        # Part 2 is here
        permituations = countWordsPermutation(
            word, fancyDictionary, impossibleWords, countedWords
        )
        countedWords[word] = permituations
        result2 += permituations

print("Part 1: ", result1)
print("Part 2: ", result2)
