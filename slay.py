from vars import *
from enemy import *
from cards import *
import random

def buildDeck():
    for count in range(5):
        state.DECK.append(Attack())
    for count in range(5):
        state.DECK.append(Block())

def createEnemy():
    enemy_pool = [Pigeon(), CatOfThondor()]
    enemy = random.choices(enemy_pool, weights=[2, 1]) # add more weights after testing
    state.ENCOUNTER.append(enemy[0])
    state.ENCOUNTER[-1].intro()

def draw():
    for card in state.DECK:
        state.DRAW_PILE.append(card)
    for count in range(state.DRAW_COUNT):
        state.HAND.append(random.choice(state.DRAW_PILE))

def startCombat():
    createEnemy()
    startPlayerTurn()

def startPlayerTurn():
    print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
    draw()
    while state.HP > 0 or state.ENCOUNTER[-1].getHP() > 0:
        while state.ENERGY > 0:
            enemySummary()
            playerSummary()
            action = input('\nType the card index you want to play: ')
            try:
                index = int(action)
                handChoice = state.HAND[index]
                if handChoice.getType() == state.ACTIONS[2]:
                    state.ENERGY -= 1
                    print(f'You used {handChoice.getEnergy()}💧 and attacked for {handChoice.getAttack()[0]} {handChoice.getType()}!\n')
                    state.HAND.remove(handChoice)
                    state.DISCARD_PILE.append(handChoice)
                elif handChoice.getType() == state.ACTIONS[3]:
                    state.ENERGY -= 1
                    state.BLOCK += handChoice.getBlock()[0]
                    print(f'You used {handChoice.getEnergy()}💧 and blocked for {handChoice.getBlock()[0]} {handChoice.getType()}!\n')
                    state.HAND.remove(handChoice)
                    state.DISCARD_PILE.append(handChoice)
            except IndexError:
                pass
            except ValueError:
                if action == 'hand':
                    print(f'Current Hand: {state.HAND}')
                elif action == 'discard':
                    print(f'Discard pile: {state.DISCARD_PILE}')
                elif action == 'end':
                    print(f'Discard pile: {state.DISCARD_PILE}')
                    break
                else:
                    break
        action = input('You\'re out of energy! Type "end" to conclude your turn: ')
        if action == 'end':
            print('Turn end')
            break
        else:
            action = input('You\'re out of energy! Type "end" to conclude your turn: ')
    if state.ENCOUNTER[-1].getHP() <= 0:
        print(f'You win! You beat the {state.ENCOUNTER[-1].getName()}')
    else:
        print(f'You died.')

def enemySummary():
    state.ENCOUNTER[-1].summary()
    print(f'{state.ENCOUNTER[-1].intent()}\n')

def playerSummary():
    print(f'🙂 {state.NAME}')
    print(f'🩸 HP: {state.HP}/{state.MAX_HP}')
    print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}')
    if state.BLOCK > 0:
        print(f'🛡  Block: {state.BLOCK}\n')
    for (index, card) in enumerate(state.HAND, start=0):
        print(index, card)

def endPlayerTurn():
    print(f'Hit endPlayerTurn function')
    pass

buildDeck()
startCombat()

# pull out parts of main battle loop into individual functions to make it easier to debug
# uses loops within summaries to continue actions
