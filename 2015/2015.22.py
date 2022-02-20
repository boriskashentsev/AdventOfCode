import sys
sys.path.append('./')
from utils.filename import calculateFileName
from copy import deepcopy

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

hero = {}
hero['health'] = 50
hero['armor'] = 0
hero['mana'] = 500
hero['effects'] = []

spells = []
spells.append({'name':'Magic Missile', 'cost':53,  'damage':4, 'health':0, 'armor':0, 'mana':0,   'turns':0})
spells.append({'name':'Drain',         'cost':73,  'damage':2, 'health':2, 'armor':0, 'mana':0,   'turns':0})
spells.append({'name':'Shield',        'cost':113, 'damage':0, 'health':0, 'armor':7, 'mana':0,   'turns':6})
spells.append({'name':'Poison',        'cost':173, 'damage':3, 'health':0, 'armor':0, 'mana':0,   'turns':6})
spells.append({'name':'Recharge',      'cost':229, 'damage':0, 'health':0, 'armor':0, 'mana':101, 'turns':5})

for spell in spells:
    if spell['turns'] > 0:
        spellCopy = deepcopy(spell)
        spellCopy['turns'] = 0
        hero['effects'].append(spellCopy)

def printCharacterInfo(hero, enemy, heroOrEnemy):
    print('')
    if heroOrEnemy == 1:
        print('-- Player turn --')
    else:
        print('-- Boss turn --')
    print('- Player has', hero['health'], 'hit points,', hero['armor'], 'armor,', hero['mana'], 'mana')
    print('- Boss has', enemy['health'], 'hit points')

def fight(part, hero, enemy, heroOrEnemy, manaUsed, minMana):
    #printCharacterInfo(hero, enemy, heroOrEnemy)

    # Part 2 check
    if part == 2 and heroOrEnemy == 1:
        hero['health'] -= 1
        #print('The players takes 1 damage from environment.')
        if hero['health'] <= 0:
            #print('This kills the player, and the environment wins.')
            #print('------------------------------------------------')
            return minMana
    # start of the turn - spells take their effect
    for effect in hero['effects']:
        if effect['turns'] > 0:
            effect['turns'] -= 1
            if effect['name'] == 'Shield':
                #print('Shield\'s timer is now', effect['turns'], '.')
                if effect['turns'] == 0:
                    #print('Shield wears off, decreasing armor by', effect['armor'], '.')
                    hero['armor'] = 0
                else:
                    hero['armor'] = effect['armor']
            elif effect['name'] == 'Recharge':
                #print('Recharge provides', effect['mana'], 'mana; its timer is now', effect['turns'],'.')
                hero['mana'] += effect['mana']
                #if effect['turns'] == 0:
                    #print('Recharge wears off.')
            elif effect['name'] == 'Poison':
                enemy['health'] -= effect['damage']
                if enemy['health'] <= 0:
                    #print('Poison deals', effect['damage'], 'damage. This kills the boss, and the player wins.')
                    minMana = manaUsed if minMana < 0 or minMana > manaUsed else minMana
                    #if minMana < 0 or minMana > manaUsed:
                        #minMana  = manaUsed
                        #print(minMana)
                    return minMana
                #else:
                    #print('Poison deals',effect['damage'],'damage; its timer is now', effect['turns'],'.')
    
    # characters turn
    if heroOrEnemy == 1:
        heroHadTurn = False
        for spell in spells:
            heroCopy = deepcopy(hero)
            enemyCopy = deepcopy(enemy)
            if hero['mana'] >= spell['cost']:
                if spell['name'] == 'Magic Missile' or spell['name'] == 'Drain':
                    #print('Player casts', spell['name'], ', dealing', spell['damage'], ' damage.')
                    #if spell['health'] > 0:
                        #print('And health the player by', spell['health'],'.')
                    heroHadTurn = True
                    heroCopy['health'] += spell['health']
                    enemyCopy['health'] -= spell['damage']
                    if enemy['health'] <= 0:
                        #print(spell['name'], 'deals', effect['damage'], 'damage. This kills the boss, and the player wins.')
                        minMana = (manaUsed + spell['cost']) if minMana < 0 or minMana > (manaUsed + spell['cost']) else minMana
                        #if minMana < 0 or minMana > (manaUsed + spell['cost']):
                            #minMana = manaUsed + spell['cost']
                            #print(minMana)
                        return minMana
                else: 
                    for effect in heroCopy['effects']:
                        if effect['name'] == spell['name']:
                            if effect['turns'] <= 0:
                                #print('Player casts', spell['name'], '.')
                                effect['turns'] = spell['turns']
                                heroHadTurn = True
                if heroHadTurn:
                    heroCopy['mana'] -= spell['cost']
                    if minMana > 0 and minMana >= manaUsed + spell['cost'] or minMana < 0:
                        minMana = fight(part, heroCopy, enemyCopy, -1, manaUsed + spell['cost'], minMana)
        if not heroHadTurn:
            #print('Not enough mana to cast any spell. The Playes loses.')
            return minMana
    else:
        damage = (enemy['damage'] - hero['armor']) if (enemy['damage'] - hero['armor']) > 1 else 1
        hero['health'] -= damage
        #if hero['armor'] > 0:
            #print('Boss attacks for', enemy['damage'], '-', hero['armor'], '=', damage, 'damage!')
        #else:
            #print('Boss attacks for', enemy['damage'], 'damage!')
        if hero['health'] <= 0:
            #print('This kills the player, and the boss wins.')
            #print('-----------------------------------------')
            return minMana
        else:
            minMana = fight(part, hero, enemy, 1, manaUsed, minMana)
    return minMana


minMana = fight(1, hero, enemy, 1, 0, -1)
print(minMana)

minMana = fight(2, hero, enemy, 1, 0, -1)
print(minMana)