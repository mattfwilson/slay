import random

FLOOR = 1
DROP_RATE = 40
POTION_CURRENT = 0
POTION_MAX = 3
INVENTORY = []
ACTION = ''
POTIONS = {
    'Power Potion': 1,
    'Speed Potion': 1,
    'Flex Potion': 1,
    'Strength Potion': 1,
    'Focus Potion': 1,
    'Energy Potion': 1,
    'Attack Potion': 1,
    'Weak Potion': 1,
    'Swift Potion': 1,
    'Block Potion': 1,
    'Dexerity Potion': 1,
    'Skill Potion': 1,
    'Fire Potion': 1,
    'Colorless Potion': 1,
    'Blessing of the Forge': 1,
    'Ancient Potion': 2,
    'Gambler\'s Brew': 2,
    'Duplication Potion': 2,
    'Distilled Chaos': 2,
    'Essence of Steel': 2,
    'Explosive Potion': 2,
    'Regen Potion': 2,
    'Fear Potion': 2,
    'Heart of Iron': 2,
    'Liquid Memories': 2,
    'Liquid Bronze': 2,
    'Fruit Juice': 2,
    'Cultist Potion': 3,
    'Smoke Bomb': 3,
    'Snecko Oil': 3,
    'Entropic Brew': 3,
    'Fairy in a Bottle': 3,
    'Ghost in a Jar': 3

    }

def roll(potions):
    weightedRoll = random.choices(potions, weights=(potions.values()), k=1)
    print(weightedRoll)
    return weightedRoll

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

test = roll(POTIONS)
print(test)

while True:
    ACTION = input(f'You are on floor {FLOOR}. Proceed to the next floor? ')
    if ACTION == 'yes':
        FLOOR, DROP_RATE, INVENTORY = roll_potion(POTIONS, DROP_RATE, FLOOR, INVENTORY)
    elif ACTION == 'inv':
        print(INVENTORY)
    else:
        break
quit()