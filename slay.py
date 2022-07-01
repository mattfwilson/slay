from enemy import *
from cards import *
import random

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
ENEMIES = []

def buildDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def createEnemy():
    enemy_pool = (Slime, Pigeon)
    
    for i in range(1):
        CURRENT_ENEMY = random.choice(enemy_pool)
        ENEMIES.append(CURRENT_ENEMY)
    return enemy_pool[-1]

def executeIntent():
    pass

def decideIntent():
    pass

def startCombat():
    startTurn()
    # enemyTurn()
    
def startTurn():
    global CURRENT_ENERGY
    CURRENT_ENERGY = MAX_ENERGY
    ENEMIES.append(createEnemy())
    draw()
    showSummary()
    ENEMIES[-1]().__repr__()
    ENEMIES[-1]().sayStats()

def showSummary():
    print('-' * 50 + f' Turn {TURN_COUNT} ' + '-' * 50)
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}')
    # playerMove = input("Type the move you'd like to do? ")

def enemyTurn():
    pass

def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1
    enemyTurn()
    
buildDeck()
startCombat()