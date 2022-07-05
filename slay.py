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
    enemy_pool = [Pigeon]
    enemy = random.choices(enemy_pool, weights=[1]) # add more weights after testing
    ENEMIES.append(enemy[0])

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def showPool():
    for i in range(COUNTER):
        createEnemy()
    print(ENEMIES)
    for i in ENEMIES:
        i().sayID()
    print('\n')

def startCombat():
    # showPool()
    createEnemy()
    ENEMIES[-1]().intro()
    draw()
    startTurn()

def startTurn():
    global ENERGY
    global MOVE
    ENERGY = MAX_ENERGY
    print(f'Enemy Pool: {ENEMIES}')
    print(f'self.id: {ENEMIES[-1]().sayID()}')
    print(f'self.name: {ENEMIES[-1]().sayName()}')
    print(f'self.hp/self.max_hp: {ENEMIES[-1]().sayHP()}/{ENEMIES[-1]().sayMaxHP()}')
    print(ENEMIES[-1]().doDamage(3))
    print(ENEMIES[-1]().sayHP())
    # playerSummary()
    # enemySummary()
    # MOVE = input('What would you like to do? ')

    # if MOVE == ACTIONS[1]:
    #     for card in CURRENT_HAND:
    #         if card.sayType() == MOVE:
    #             print(f'You use {card.sayEnergy()} 💧 to play ⚔  {card.sayType()} for {card.sayAttack()}')
    #             ENERGY -= card.sayEnergy()
    # elif MOVE == ACTIONS[2]:
    #     for card in CURRENT_HAND:
    #         if card.sayType() == MOVE:
    #             print(f'You use {card.sayEnergy()} 💧 to play 🛡  {card.sayType()} for {card.sayBlock()}')
    #             ENERGY -= card.sayEnergy()
    # else:
    #     print('You hit the else')


def playerSummary():
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    print(f'🙂 {NAME}')
    print(f'🩸 HP: {HP}/{MAX_HP}')
    print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}')
    print(f'🖐  Cards: {CURRENT_HAND}\n')

def enemySummary():
    ENEMIES[-1]().saySummary()
    print(f'{ENEMIES[-1]().intent()}')

def endTurn():
    global TURN_COUNT
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1

# main game execution
buildDeck()
startCombat()