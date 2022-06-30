from enemy import *
from cards import *
import itertools
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

def createDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def showSummary():
    print('-' * 50 + f' Turn {TURN_COUNT} ' + '-' * 50)
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}')

def startCombat():
    pass

def drawCards():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def startTurn():
    global CURRENT_ENERGY
    global TURN_COUNT
    CURRENT_ENERGY = MAX_ENERGY
    drawCards()
    showSummary()

def enemyTurn():
    pass

def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1
    enemyTurn()
    
createDeck()
startTurn()

enemies = (Slime, Pigeon)
enemies_fought = []

for i in range(5):
    instance = random.choice(enemies)
    enemies_fought.append(instance)
instance().__repr__()