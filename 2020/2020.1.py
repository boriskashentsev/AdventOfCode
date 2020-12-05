filename = "2020/1.input"

f = open(filename, "r")

inpt = f.read().split("\n")

numbers = []

for line in inpt:
    numbers.append(int(line))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if(numbers[i] + numbers[j] + numbers[k] == 2020) and (i!=j):
                print(numbers[i], ' ', numbers[j], ' ', numbers[k])
                print(numbers[i]*numbers[j]*numbers[k])