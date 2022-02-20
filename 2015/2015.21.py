import sys
sys.path.append('./')
from utils.filename import calculateFileName

filename = calculateFileName(sys.argv)
f = open(filename, "r")
input = f.read()

lines = input.split('\n')

enemy = {}
for line in lines:
    if len(line.split('Hit Points: ')) > 1:
        enemy['health'] = int(line.split('Hit Points: ')[1])
    elif len(line.split('Damage: ')) > 1:
        enemy['damage'] = int(line.split('Damage: ')[1])
    elif len(line.split('Armor: ')) > 1:
        enemy['armor'] = int(line.split('Armor: ')[1])

hero = {}
hero['health'] = 100
hero['damage'] = 0
hero['armor'] = 0
hero['cost'] = 0

# Yeah, yeah, yeah, we can read weapons, armors and rings from a file...
# But this time we will be stubborn and more forward with this
weapons = []
weapons.append({'name':'Dagger',     'cost':8,  'damage':4, 'armor':0})
weapons.append({'name':'Shortsword', 'cost':10, 'damage':5, 'armor':0})
weapons.append({'name':'Warhammer',  'cost':25, 'damage':6, 'armor':0})
weapons.append({'name':'Longsword',  'cost':40, 'damage':7, 'armor':0})
weapons.append({'name':'Greataxe',   'cost':74, 'damage':8, 'armor':0})
armors = []
armors.append({'name':'Leather',    'cost':13,  'damage':0, 'armor':1})
armors.append({'name':'Chainmail',  'cost':31,  'damage':0, 'armor':2})
armors.append({'name':'Splintmail', 'cost':53,  'damage':0, 'armor':3})
armors.append({'name':'Bandedmail', 'cost':75,  'damage':0, 'armor':4})
armors.append({'name':'Platemail',  'cost':102, 'damage':0, 'armor':5})
armors.append({'name':'',           'cost':0,   'damage':0, 'armor':0})
rings = []
rings.append({'name':'Damage +1',  'cost':25,  'damage':1, 'armor':0})
rings.append({'name':'Damage +2',  'cost':50,  'damage':2, 'armor':0})
rings.append({'name':'Damage +3',  'cost':100, 'damage':3, 'armor':0})
rings.append({'name':'Defense +1', 'cost':20,  'damage':0, 'armor':1})
rings.append({'name':'Defense +2', 'cost':40,  'damage':0, 'armor':2})
rings.append({'name':'Defense +3', 'cost':80,  'damage':0, 'armor':3})
rings.append({'name':'',           'cost':0,   'damage':0, 'armor':0})

def fight(hero, enemy):
    # return True for hero win, returns False for hero lose
    heroHealth = hero['health']
    enemyHealth = enemy['health']
    while True:
        enemyHealth -= (hero['damage'] - enemy['armor']) if (hero['damage'] - enemy['armor']) > 1 else 1
        if enemyHealth <= 0:
            return True
        heroHealth -= (enemy['damage'] - hero['armor']) if (enemy['damage'] - hero['armor']) > 1 else 1
        if heroHealth <= 0:
            return False

def equipAPiece(hero, piece, onOrOff):
    # onOrOff: +1 on, -1 off
    for equipmentKey in piece.keys():
        if equipmentKey in hero.keys():
            hero[equipmentKey] += onOrOff*piece[equipmentKey]


def equipAndFight(hero, enemy):
    minCost = -1 # Part 1
    maxCost = -1 # Part 2
    for weapon in weapons:
        equipAPiece(hero, weapon, 1)
        for armor in armors:
            equipAPiece(hero, armor, 1)
            for ring1 in rings:
                for ring2 in rings:
                    if ring1['name'] != ring2['name'] or ring1['name'] == '':
                        equipAPiece(hero, ring1, 1)
                        equipAPiece(hero, ring2, 1)
                        if fight(hero, enemy):
                            minCost = hero['cost'] if minCost < 0 or minCost > hero['cost'] else minCost
                        else:
                            if maxCost < hero['cost']:
                                maxCost = hero['cost']
                        equipAPiece(hero, ring1, -1)
                        equipAPiece(hero, ring2, -1)
            equipAPiece(hero, armor, -1)
        equipAPiece(hero, weapon, -1)
    
    return minCost, maxCost

print(equipAndFight(hero, enemy))