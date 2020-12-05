filename = "2020/2.input"

f = open(filename, "r")

inpt = f.read().split("\n")

# First part

# answer = 0
# for line in inpt:
#     sides = line.split(": ")
#     left = sides[0].split(" ")
#     numbers = left[0].split("-")
#     limits = [int(numbers[0]), int(numbers[1])]
#     letter = left[1]
#     password = sides[1]
#     occurrence  = len(password.split(letter))-1
#     if (occurrence >= limits[0] and occurrence <= limits[1]):
#         answer = answer + 1

#print(answer)

#Second part
answer = 0
for line in inpt:
    sides = line.split(": ")
    left = sides[0].split(" ")
    numbers = left[0].split("-")
    positions = [int(numbers[0])-1, int(numbers[1])-1]
    letter = left[1]
    password = sides[1]
    occurance = [1 if password[positions[0]]==letter else 0, 1 if password[positions[1]]==letter else 0]
    endSum = occurance[0]+occurance[1]
    if (endSum == 1):
        answer = answer + 1

print(answer)