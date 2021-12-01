filename = "2015/15.test.input"

f = open(filename, "r")

input = f.read().split("\n")

ingredients = {}

for line in input:
    parts = line.split(' ')
    ingredient = parts[0][:-1]
    ingredients[ingredient] = { 'capacity': int(parts[2][:-1]),
                                'durability': int(parts[4][:-1]),
                                'flavor': int(parts[6][:-1]),
                                'texture': int(parts[8][:-1]),
                                'calories': int(parts[10])}

