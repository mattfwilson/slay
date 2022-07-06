from venv import create
from vars import *
from enemy import *
from cards import *
import random

def buildDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Block())
    random.shuffle(DRAW_PILE)

def createEnemy():
    enemy_pool = [Pigeon()]
    enemy = random.choices(enemy_pool, weights=[1]) # add more weights after testing
    ENEMY.append(enemy[0])

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def testPool():
    for num in range(COUNTER):
        createEnemy()
    for enemy in ENEMY:
        print(f'{enemy.sayName()} {enemy.sayID()}, {enemy.sayHP()}/{enemy.sayMaxHP()} - {enemy.intent()}')
    print('\n')

def startCombat():
    createEnemy()
    ENEMY[-1].intro()
    draw()
    startTurn()

def startTurn():
    global ENERGY
    global MOVE
    ENERGY = MAX_ENERGY
    # testPool()
    playerSummary()
    enemySummary()
    MOVE = input('What would you like to do? ')

    if MOVE == ACTIONS[1]:
        for card in HAND:
            if card.sayType() == MOVE:
                print(f'You use {card.sayEnergy()} 💧 to play ⚔  {card.sayType()} for {card.sayAttack()}')
                ENERGY -= card.sayEnergy()
    elif MOVE == ACTIONS[2]:
        for card in HAND:
            if card.sayType() == MOVE:
                print(f'You use {card.sayEnergy()} 💧 to play 🛡  {card.sayType()} for {card.sayBlock()}')
                ENERGY -= card.sayEnergy()
    else:
        print('You hit the else')

def playerSummary():
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    print(f'🙂 {NAME}')
    print(f'🩸 HP: {HP}/{MAX_HP}')
    print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}')
    print(f'🖐  Cards: {HAND}\n')

def enemySummary():
    ENEMY[-1].saySummary()
    print(f'{ENEMY[-1].intent()}')

def endTurn():
    global TURN_COUNT
    HAND.pop(len(range(HAND)))
    TURN_COUNT += 1

# main game execution
buildDeck()
startCombat()