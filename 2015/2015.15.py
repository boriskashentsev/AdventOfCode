def countCookieScore(ingredients, components, isPart1):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    ingredients_keys = list(ingredients.keys())
    for i in range(len(ingredients_keys)):
        capacity += components[i]*ingredients[ingredients_keys[i]]['capacity']
        durability += components[i]*ingredients[ingredients_keys[i]]['durability']
        flavor += components[i]*ingredients[ingredients_keys[i]]['flavor']
        texture += components[i]*ingredients[ingredients_keys[i]]['texture']
        calories += components[i]*ingredients[ingredients_keys[i]]['calories']
    
    if isPart1:
        return capacity*durability*flavor*texture
    return -1

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

components = [0]*len(input)
components[0] = 100

print(countCookieScore(ingredients, components, True))