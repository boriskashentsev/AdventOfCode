filename = "2021/02.input"

f = open(filename, "r")

input = f.read().split("\n")



# Part 1

horizontal = 0
vertical = 0

for line in input:
    splits = line.split(" ")
    command = splits[0]
    value = int(splits[1])
    if command == "forward":
        horizontal += value
    elif command == "down":
        vertical += value
    elif command == "up":
        vertical -= value
        if (vertical < 0):
            print("Are we flying?")

print("result", horizontal*vertical)

# Part 2

horizontal = 0
aim = 0
vertical = 0

for line in input:
    splits = line.split(" ")
    command = splits[0]
    value = int(splits[1])
    if command == "forward":
        horizontal += value
        vertical += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value
        if (aim < 0):
            print("Are we flying?")

print("result", horizontal*vertical)