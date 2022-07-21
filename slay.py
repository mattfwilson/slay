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

def getEnemyIntent():
    intent = state.ENCOUNTER[-1].intent()
    return intent


def startCombat():
    createEnemy()
    print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
    draw()
    playerTurn()

def enemySummary(intent):
    state.ENCOUNTER[-1].summary()
    if intent[0] == 1:
        print(f'⚔  Enemy intends to Attack for {intent[1]}\n')
    else:
        print(f'🛡  Enemy intends to Block for {intent[1]}\n')

def playerSummary():
    print(f'🙂 {state.NAME}')
    print(f'🩸 HP: {state.HP}/{state.MAX_HP}')
    print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}')
    if state.BLOCK > 0:
        print(f'🛡  Block: {state.BLOCK}')
    print(f'\nCURRENT HAND:')
    for (index, card) in enumerate(state.HAND, start=0):
        print(index, card.getSummary())

def createEnemy():
    enemy_pool = [Pigeon(), CatOfThondor()]
    enemy = random.choices(enemy_pool, weights=[1, 1])
    state.ENCOUNTER.append(enemy[0])
    enemy = state.ENCOUNTER[-1]
    enemy.intro()
    return enemy

def draw():
    for card in state.DECK:
        state.DRAW_PILE.append(card)
    for count in range(state.DRAW_COUNT):
        state.HAND.append(random.choice(state.DRAW_PILE))

def enemyTurn():
    print(f'start of enemyTurn function')
    exit()

def playerTurn():
    intent = getEnemyIntent()
    while state.HP > 0 or state.ENCOUNTER[-1].getHP() > 0:
        while state.ENERGY > 0:
            enemySummary(intent)
            playerSummary()
            action = input('\nType the card index you want to play: ')
            try:
                index = int(action)
                cardPlayed = state.HAND[index]
                enemy = state.ENCOUNTER[-1]
                if (state.ENERGY - cardPlayed.getEnergy()) >= 0:
                    if cardPlayed.getType() == state.ACTIONS[2]:
                        state.ENERGY -= cardPlayed.getEnergy()
                        # enemy.setHP() -= cardPlayed.getAttack()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        state.HAND.remove(cardPlayed)
                        state.DISCARD_PILE.append(cardPlayed)
                if (state.ENERGY - cardPlayed.getEnergy()) >= 0:
                    if cardPlayed.getType() == state.ACTIONS[3]:
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
                    print(f'\nCURRENT HAND:')
                    for card in state.HAND:
                        print(f'{card.getSummary()}')
                elif action == 'draw':
                    print(f'\nDRAW PILE:')
                    for card in state.DRAW_PILE:
                        print(f'{card.getSummary()}')
                elif action == 'discard':
                    print(f'\nDISCARD PILE:')
                    for card in state.DISCARD_PILE:
                        print(f'{card.getSummary()}')
                elif action == 'end':
                    enemyTurn()
                    break
                else:
                    break
        if action == 'end':
            for card in state.HAND:
                state.HAND.remove(card)
                state.DISCARD_PILE.append(card)
            enemyTurn()
        else:
            action = input('ELSE if not int or not actions: Type "end" to conclude your turn: ')
    if state.ENCOUNTER[-1].getHP() <= 0:
        print(f'You win! You beat the {state.ENCOUNTER[-1].getName()}')
    else:
        print(f'You died. End of player/enemy HP loop')

buildDeck()
startCombat()
