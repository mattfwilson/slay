from tkinter.tix import MAX
from enemy import *
from cards import *
import random
import time

COUNTER = 25
NAME = 'Karmae'
HP = 70
MAX_HP = 70
ENERGY = 1
MAX_ENERGY = 3
USER_GOLD = 0
COMBAT_COUNT = 1
TURN_COUNT = 1
DRAW_COUNT = 5
DRAW_PILE = []
CURRENT_HAND = []
DISCARD_PILE = []
ENEMIES = []
ACTIONS = ['Draw', 'Attack', 'Block', 'Draw Pile', 'Discard Pile']

def buildDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def createEnemy():
    enemy_pool = [Seagull, Pigeon, Hawk]
    enemy = random.choices(enemy_pool, weights=[10, 7, 2])
    ENEMIES.append(enemy[0])

def draw():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def startCombat():
    for i in range(COUNTER):
        createEnemy()
    print(ENEMIES)
    for i in ENEMIES:
        i().sayID()
    print('\n')
    createEnemy()
    ENEMIES[-1]().intro()
    draw()
    startTurn()

def startTurn():
    global ENERGY
    ENERGY = MAX_ENERGY
    playerSummary()
    enemySummary()

def playerSummary():
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    print(f'{NAME}')
    print(f'HP: {HP}/{MAX_HP}')
    print(f'Energy: {ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}\n')

def enemySummary():
    ENEMIES[-1]().saySummary()
    print(f'{ENEMIES[-1]().intent()}')

def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1

# main game execution
buildDeck()
startCombat()