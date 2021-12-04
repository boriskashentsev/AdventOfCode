def checkCard(card):
    for i in range(len(card)):
        vertical = True
        horizontal = True
        for j in range(len(card[i])):
            if card[i][j] > 0:
                horizontal = False
            if card[j][i] > 0:
                vertical = False
        if vertical or horizontal:
            return True
    return False

def checkAllCards(cards):
    for card in cards:
        if not checkCard(card):
            return False
    return True


def markCard(card, number):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == number:
                card[i][j] = -1
    return card

def calculateScore(card, number):
    sum = 0
    for line in card:
        for cell in line:
            if cell > 0:
                sum += cell
    return sum*number

filename = "2021/04.input"

f = open(filename, "r")

input = f.read().split("\n")

numbers = list(map(lambda x: int(x), input[0].split(",")))

cards = []

index = 2
while len(input) > index:
    card = []
    for i in range(5):
        line = []
        lineStr = input[index+i].split(" ")
        for element in lineStr:
            if element != "":
                line += [int(element)]
        card.insert(len(card), line)
    index += 6
    cards.insert(len(cards), card)

foundWinner = False
foundLastWinner = False
index = 0

while not (foundWinner and foundLastWinner) and  index < len(numbers):
    for i in range(len(cards)):
        card = markCard(cards[i], numbers[index])
        cards[i] = card
        if not foundWinner and checkCard(cards[i]):
            # Part 1
            print("First Winner: ", calculateScore(cards[i], numbers[index]))
            foundWinner = True
        if not foundLastWinner and checkAllCards(cards):
            # Part 2
            print("Last Winner: ",calculateScore(cards[i], numbers[index]))
            foundLastWinner = True
    index += 1

