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
ENEMIES_FOUGHT = []
CURRENT_ENEMY = ''


def buildDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def createEnemy():
    enemy_pool = (Slime, Pigeon)
    
    for i in range(1):
        CURRENT_ENEMY = random.choice(enemy_pool)
        ENEMIES_FOUGHT.append(CURRENT_ENEMY)

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def startCombat():
    startTurn()

def startTurn():
    global CURRENT_ENERGY
    global TURN_COUNT
    CURRENT_ENERGY = MAX_ENERGY
    createEnemy()
    draw()
    showSummary()

def showSummary():
    print('-' * 50 + f' Turn {TURN_COUNT} ' + '-' * 50)
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}')
    # playerMove = input("Type the move you'd like to do? ")

def executeIntent():
    pass

def decideIntent():
    pass

def enemyTurn():
    pass
def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1
    enemyTurn()
    
buildDeck()
startCombat()
print(ENEMIES_FOUGHT)