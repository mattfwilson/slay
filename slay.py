from ctypes.wintypes import HANDLE
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
    enemy_pool = [Pigeon(), CatOfThondor()]
    enemy = random.choices(enemy_pool, weights=[1, 1]) # add more weights after testing
    ENEMY.append(enemy[0])
    ENEMY[-1].intro()
    return ENEMY[-1]

def draw():
    for i in range(DRAW_COUNT):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def startCombat():
    createEnemy()
    draw()
    startPlayerTurn()

def startPlayerTurn():
    global ENERGY
    global HAND
    
    print(f'ENERGY before while: {state.ENERGY}')
    while ENERGY > 0:
        enemySummary()
        playerSummary()
        action = input('\nWhich card do you want to play? ')
        try:
            index = int(action)
            handChoice = HAND[index]
            if handChoice.getType() == ACTIONS[1]:
                print(f'You used {handChoice.getEnergy()}💧 and attacked for {handChoice.getAttack()} {handChoice.getType()}!')
                ENERGY -= 1
                HAND.remove(handChoice)
                DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
            elif handChoice.getType() == ACTIONS[2]:
                print(f'You used {handChoice.getEnergy()}💧 and blocked for {handChoice.getBlock()} {handChoice.getType()}!')
                ENERGY -= 1
                HAND.remove(handChoice)
                DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
        except IndexError:
            pass
        except ValueError:
            if action == 'HAND':
                print('Current Hand: {HAND}')
            elif action == 'DISCARD_PILE':
                print(f'Discard Pile: {DISCARD_PILE}')
            elif action == 'end':
                print(f'Global energy: {ENERGY}')
                print(f'Function energy: {ENERGY}')
                return ENERGY
    action = input('You\'re out of energy! Type "end" to conclude your turn. ')
    if action == 'end':
        return f'Energy: {ENERGY}/{MAX_ENERGY}, end of turn {TURN_COUNT}'
    else:
        action = input('You\'re out of energy! Type "end" to conclude your turn. ')

def endPlayerTurn():
    print(f'Hit endPlayerTurn function')
    pass
    # for card in HAND:
    #     print(card)
    #     HAND.remove(card)
    #     DISCARD_PILE.append(card)
    #     print(f'Discard Pile: {DISCARD_PILE}')

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

buildDeck()
startCombat()

print(f'Global energy (outside): {ENERGY}')
# Max ???s

# what order would you do for checking the main battle loop?
# best way to create iterators?
# is there an easier way to call class methods? 

# pull out parts of main battle loop into individual functions to make it easier to debug
# uses loops within summaries to continue actions
# try making a "game state" class to instantiate all needed global variables
