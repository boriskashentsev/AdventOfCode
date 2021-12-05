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
    
    capacity = capacity if capacity > 0 else 0
    durability = durability if durability > 0 else 0
    flavor = flavor if flavor > 0 else 0
    texture = texture if texture > 0 else 0
    calories = calories if calories > 0 else 0
    
    if isPart1:
        return capacity*durability*flavor*texture
    if calories == 500:
        return capacity*durability*flavor*texture
    return -1

def cooking(ingredients, components, index, maxNumberOfComponents, maxValue, isPart1):
    if index >= len(components):
        if sum(components) == 100:
            return countCookieScore(ingredients, components, isPart1)
        else:
            return -1
    for i in range(maxNumberOfComponents + 1):
        components[index] = i
        if sum(components) <= maxNumberOfComponents:
            value = cooking(ingredients, components, index + 1, maxNumberOfComponents, maxValue, isPart1)
            if value > maxValue:
                maxValue = value
    components[index] = 0
    return maxValue

filename = "2015/15.input"
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
result = cooking(ingredients, components, 0, 100, -1, True)

print("Part 1", result)

components = [0]*len(input)

result = cooking(ingredients, components, 0, 100, -1, False)

print("Part 2", result)
