filename = "2020/9.input"

f = open(filename, "r")

inpt = f.read().split("\n")

sequence = []
for line in inpt:
    sequence.append(int(line))

preamble = 0
if ("test" in filename):
    preamble = 5
else:
    preamble = 25

# first part

found = False
result = 0

for i in range(preamble, len(sequence)):
    number = sequence[i]
    shortSeq = sequence[i-preamble:i]
    found = False
    loops = 0
    while not found and loops < preamble:
        first = shortSeq.pop(0)
        for element in shortSeq:
            if (first + element) == number:
                found = True
                break
        shortSeq.append(first)
        loops = loops + 1
    
    if not found:
        result = number
        break

if not found:
    print(result)

# second part

i = 0
j = 1
secondResult = 0

while not found:
    # increasing J
    while sum(sequence[i:j]) < result:
        j = j + 1
    # increasing I
    while sum(sequence[i:j]) > result:
        i = i + 1
    if sum(sequence[i:j]) == result:
        secondResult = min(sequence[i:j]) + max(sequence[i:j])
        found = True

print(secondResult)

