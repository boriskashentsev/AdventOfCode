row = 2947
column = 3029

steps = 0

for i in range(1, column + 1):
    steps += i

for i in range(row-1):
    steps += column + i

print(steps)

number = 20151125

for i in range(steps-1):
    number *= 252533
    number %= 33554393

print("Part 1", number)

