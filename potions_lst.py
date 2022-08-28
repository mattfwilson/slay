import random
import numpy as np

FLOOR = 1
DROP_RATE = 40
POTION_CURRENT = 0
POTION_MAX = 3
INVENTORY = []
ACTION = ''
POTIONS = [
    'Power Potion',
    'Speed Potion',
    'Flex Potion',
    'Strength Potion',
    'Focus Potion',
    'Energy Potion',
    'Attack Potion',
    'Weak Potion',
    'Swift Potion',
    'Block Potion',
    'Dexerity Potion',
    'Skill Potion',
    'Fire Potion',
    'Colorless Potion',
    'Blessing of the Forge',
    'Ancient Potion',
    'Gambler\'s Brew',
    'Duplication Potion',
    'Distilled Chaos',
    'Essence of Steel',
    'Explosive Potion',
    'Regen Potion',
    'Fear Potion',
    'Heart of Iron',
    'Liquid Memories',
    'Liquid Bronze',
    'Fruit Juice',
    'Cultist Potion', 
    'Smoke Bomb',
    'Snecko Oil',
    'Entropic Brew',
    'Fairy in a Bottle',  
    'Ghost in a Jar'
    ]

def roll(potions, inventory, rate, floor):
    success = random.randint(1, 100)
    if success <= rate:
        potion = np.random.choice(potions, 32, p=[.05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .02, .02, .02, .02, .02, .02, .02, .02, .02, .02, .02, .02, .015, .015, .015, .015, .015, .015, .01, .01])
        inventory.append(potion)
        print(f'You found a {potion}')
        rate = 40
        floor += 1
        print(f'Drop rate: {rate}&')
        return floor, inventory, rate
    else:
        rate += 10
        floor += 1
        print(f'Drop rate: {rate}%')
        print('You didn\'t find anything..')


def roll_potion(potions, rate, floor, inventory):
    success = random.randint(1, 100)
    if success <= rate:
        potion = random.choice(list(potions.keys()))
        inventory.append(potion)
        print(f'You found a {potion}')
        rate = 40
        floor += 1
        print(f'Drop rate: {rate}&')
        return floor, rate, inventory
    else:
        rate += 10
        floor += 1
        print(f'Drop rate: {rate}%')
        print('You didn\'t find anything..')
        return floor, rate, inventory

while True:
    ACTION = input(f'You are on floor {FLOOR}. Proceed to the next floor? ')
    if ACTION == 'yes':
        roll(POTIONS, INVENTORY, DROP_RATE, FLOOR)
    elif ACTION == 'inv':
        print(INVENTORY)
    else:
        break
quit()