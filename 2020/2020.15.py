filename = "2020/15.input"
f = open(filename, "r")
inpt = f.read()

sequence = map(int, inpt.split(','))

# first part

'''while len(sequence) < 2020:
    number = sequence[-1]
    age = 0
    if number in sequence[:-1]:
        age = 1
        while sequence[len(sequence) - 1 - age] != number:
            age = age + 1
    sequence.append(age)

print(sequence[-1])'''

# second part (Seems to be very slow)

ages = {}
step = 0
number = -1

sequence = map(int, inpt.split(','))

while step < len(sequence) - 1:
    number = sequence[step]
    if step >= 0:
        ages[number] = step
    step = step + 1


number = sequence[step]
while step < 1000000-1:
    number1 = number
    if (number in ages.keys()):
        number = step - ages[number]
    else:
        number = 0
    ages[number1] = step
    step = step + 1
    if step % 10000 == 0:
        print(step)
        print(len(ages.keys()))

print(step+1, number)
