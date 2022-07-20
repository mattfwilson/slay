# need to figure out why the main gamp loop can't call enemy from GameState class

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
    enemy = random.choices(enemy_pool, weights=[1, 1]) # add more weights after testing
    state.ENCOUNTER.append(enemy[0])
    enemy = state.ENCOUNTER[-1]
    enemy.intro()
    return enemy

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
                cardPlayed = state.HAND[index]
                enemy = state.ENCOUNTER[-1]
                if (state.ENERGY - cardPlayed.getEnergy()) >= 0:
                    if cardPlayed.getType() == state.ACTIONS[2]:
                        state.ENERGY -= cardPlayed.getEnergy()
                        # print(cardPlayed.getAttack()[0])
                        # print(enemy.setHP())
                        # enemy.setHP() -= cardPlayed.getAttack()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        state.HAND.remove(cardPlayed)
                        state.DISCARD_PILE.append(cardPlayed)
                    elif cardPlayed.getType() == state.ACTIONS[3]:
                        state.ENERGY -= cardPlayed.getEnergy()
                        state.BLOCK += cardPlayed.getBlock()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                        state.HAND.remove(cardPlayed)
                        state.DISCARD_PILE.append(cardPlayed)
                else:
                    print('You don\'t have enough energy!\n')
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
