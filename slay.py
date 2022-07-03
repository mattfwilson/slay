from enemy import *
from cards import *
import random
import time

USER_LVL = 1
CURRENT_HP = 70
MAX_HP = 70
CURRENT_ENERGY = 1
MAX_ENERGY = 3
USER_GOLD = 0
COMBAT_COUNT = 1
TURN_COUNT = 1
DRAW_COUNT = 5
DRAW_PILE = []
CURRENT_HAND = []
DISCARD_PILE = []
ENEMY = []

def buildDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def startTurn():
    playerSummary()
    enemySummary()

def startCombat():
    ENEMY.append(createEnemy())
    print(f'{ENEMY[-1]().__repr__()}')
    draw()
    startTurn()

def createEnemy():
    enemy_pool = (Slime, Pigeon)
    
    for i in range(1):
        CURRENT_ENEMY = random.choice(enemy_pool)
        ENEMY.append(CURRENT_ENEMY)
    return enemy_pool[-1]

def playerSummary():
    print('-' * 50 + f' Turn {TURN_COUNT} ' + '-' * 50)
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}')

def enemySummary():
    time.sleep(1)
    print('\n')
    ENEMY[-1]().sayHP()
    print(f'{ENEMY[-1]().intent()}')

def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1


# main game execution
buildDeck()
startCombat()