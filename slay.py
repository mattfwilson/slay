from vars import *
from enemy import *
from cards import *
import random

def buildDeck():
    for i in range(5):
        state.DECK.append(Attack())
    for j in range(5):
        state.DECK.append(Block())

def createEnemy():
    enemy_pool = [Pigeon(), CatOfThondor()]
    enemy = random.choices(enemy_pool, weights=[2, 1]) # add more weights after testing
    state.ENCOUNTER.append(enemy[0])
    state.ENCOUNTER[-1].intro()

def draw():
    print(state.DECK)
    for card in state.DECK:
        state.DRAW_PILE.append(card)
    for x in range(state.DRAW_COUNT):
        state.HAND.append(random.choice(state.DRAW_PILE))

def startCombat():
    createEnemy()
    draw()
    startPlayerTurn()

def startPlayerTurn():
    # print(f'***TESTING*** before while loop: {state.ENERGY} energy')
    while state.ENERGY > 0:
        enemySummary()
        playerSummary()
        action = input('\nWhich card do you want to play? ')
        try:
            index = int(action)
            handChoice = state.HAND[index]
            if handChoice.getType() == ACTIONS[1]:
                print(f'You used {handChoice.getEnergy()}💧 and attacked for {handChoice.getAttack()} {handChoice.getType()}!')
                state.ENERGY -= 1
                state.HAND.remove(handChoice)
                state.DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}\n')
            elif handChoice.getType() == ACTIONS[2]:
                print(f'You used {handChoice.getEnergy()}💧 and blocked for {handChoice.getBlock()} {handChoice.getType()}!')
                state.ENERGY -= 1
                state.HAND.remove(handChoice)
                state.DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}\n')
        except IndexError:
            pass
        except ValueError:
            if action == 'HAND':
                print('Current Hand: {state.HAND}')
            elif action == 'DISCARD_PILE':
                print(f'Discard Pile: {state.DISCARD}')
            elif action == 'end':
                # print(f'***TESTING*** after while loop: {state.ENERGY} energy')
                return state.ENERGY
    action = input('You\'re out of energy! Type "end" to conclude your turn. ')
    if action == 'end':
        # print(f'***TESTING*** after while loop: {state.ENERGY} energy')
        return f'Energy: {state.ENERGY}/{state.MAX_ENERGY}, end of turn {TURN_COUNT}'
    else:
        action = input('You\'re out of energy! Type "end" to conclude your turn. ')


def enemySummary():
    print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
    state.ENCOUNTER[-1].saySummary()
    print(f'{state.ENCOUNTER[-1].intent()}\n')

def playerSummary():
    print(f'🙂 {state.NAME}')
    print(f'🩸 HP: {state.HP}/{state.MAX_HP}')
    print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}\n')
    for (index, card) in enumerate(state.HAND, start=0):
        print(index, card)

def endPlayerTurn():
    print(f'Hit endPlayerTurn function')
    pass

buildDeck()
startCombat()

print(f'Global energy (outside): {state.ENERGY}')
# Max ???s

# what order would you do for checking the main battle loop?
# best way to create iterators?
# is there an easier way to call class methods? 

# pull out parts of main battle loop into individual functions to make it easier to debug
# uses loops within summaries to continue actions
# try making a "game state" class to instantiate all needed global variables
