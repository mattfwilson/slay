import random

FLOOR = 1
DROP_RATE = 40
POTION_CURRENT = 0
POTION_MAX = 3
POTIONS = ['Flex Potion', 'Ghost in a Jar', 'Block Potion', 'Skill Potion', 'Fire Potion', 'Smoke Bomb', 'Fairy in a Bottle', 'Fruit Juice', 'Liquid Bronze', 'Cultist Potion']
INVENTORY = []
ACTION = ''

def roll_potion(potions, rate, floor, inventory):
    success = random.randint(1, 100)
    if success <= rate:
        drop = random.choice(potions)
        inventory.append(drop)
        print(f'You found a {drop}')
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
        FLOOR, DROP_RATE, INVENTORY = roll_potion(POTIONS, DROP_RATE, FLOOR, INVENTORY)
    elif ACTION == 'inv':
        print(INVENTORY)
    else:
        break
quit()