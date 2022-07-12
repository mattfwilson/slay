from vars import *
from enemy import *
from cards import *
import random

def buildDeck():
    for i in range(10):
        card = random.randint(1, 2)
        if card == 1:
            DRAW_PILE.append(Attack())
        else:
            DRAW_PILE.append(Block())
    random.shuffle(DRAW_PILE)

def createEnemy():
    enemy_pool = [Pigeon()]
    enemy = random.choices(enemy_pool, weights=[1]) # add more weights after testing
    ENEMY.append(enemy[0])
    ENEMY[-1].intro()

def draw():
    for i in range(DRAW_COUNT):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def testPool():
    for num in range(COUNTER):
        createEnemy()
    for enemy in ENEMY:
        print(f'{enemy.sayName()} {enemy.sayID()}, {enemy.sayHP()}/{enemy.sayMaxHP()} - {enemy.intent()}')

def startCombat():
    createEnemy()
    startTurn()

def startTurn():
    global TURN_COUNT
    global ENERGY
    # TURN_COUNT += 1
    # ENERGY = MAX_ENERGY
    draw()
    enemySummary()

    while ENERGY > 0:
        playerSummary()
        action = int(input('\nWhich card do you want to play? '))
        if HAND[action].sayType() == ACTIONS[1]:
            ENERGY -= 1
            print(f'You used {HAND[action].sayEnergy()}💧 and attacked for {HAND[action].sayAttack()}!')
        elif HAND[action].sayType() == ACTIONS[2]:
            ENERGY -= 1
            print(f'You used {HAND[action].sayEnergy()}💧 and blocked for {HAND[action].sayBlock()}!')
        else:
            print('Invalid input...')


def endTurn():
    for card in HAND:
        HAND.pop(card)

def enemySummary():
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    ENEMY[-1].saySummary()
    print(f'{ENEMY[-1].intent()}\n')

def playerSummary():
    print(f'🙂 {NAME}')
    print(f'🩸 HP: {HP}/{MAX_HP}')
    print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
    for (index, card) in enumerate(HAND, start=0):
        print(index, card)

# main game execution
buildDeck()
startCombat()