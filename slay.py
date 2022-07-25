# need to figure out why the main gamp loop can't call enemy from GameState class

from vars import *
from enemy import *
from cards import *
import copy
import random
        
def buildDeck():
    for count in range(5):
        state.DECK.append(Attack())
    for count in range(5):
        state.DECK.append(Block())
    state.DRAW_PILE = state.DECK
    random.shuffle(state.DRAW_PILE)

def draw():
    if len(state.DRAW_PILE) < state.DRAW_COUNT:
        print(f'Length of draw: {len(state.DRAW_PILE)}')
        state.DRAW_PILE += state.DISCARD_PILE
        state.DISCARD_PILE = []
        random.shuffle(state.DRAW_PILE)
        for card in range(state.DRAW_COUNT):
            drawn = state.DRAW_PILE.pop(-1)
            state.HAND.append(drawn)
    else:
        for card in range(state.DRAW_COUNT):
            drawn = state.DRAW_PILE.pop(-1)
            state.HAND.append(drawn)

def createEnemy():
    enemy_pool = [Pigeon(), CatOfThondor()]
    enemy = random.choices(enemy_pool, weights=[1, 1])
    state.ENCOUNTER.append(enemy[0])
    enemy = state.ENCOUNTER[-1]
    enemy.intro()
    return enemy

def enemyIntent(enemy):
    intent = enemy.intent()
    return intent

def enemySummary(intent, enemy):
    enemy.summary()
    if intent[0] == 1:
        print(f'⚔  Enemy intends to Attack for {intent[1][0]}\n')
    else:
        print(f'🛡  Enemy intends to Block for {intent[1][0]}\n')
        
def enemyTurn(hand, block, intent):
    print(f'start of enemyTurn function')
    for i in intent[1]:
        dmgAmount = i
    if intent[0] == 1:
        if dmgAmount >= block:
            state.HP -= dmgAmount - block
            print(f'Enemy attacks for {intent[1]}!')
            print(state.HP)
        else:
            block -= dmgAmount
            print(f'Remaining Block: {block}')
    else:
        print(f'Enemy blocks for {intent[1]}')
    playerTurn(state.HP, state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE, state.ENERGY)

def playerSummary(current_energy):
    print(f'🙂 {state.NAME}')
    print(f'🩸 HP: {state.HP}/{state.MAX_HP}')
    print(f'💧 Energy: {current_energy}/{state.MAX_ENERGY}')
    if state.BLOCK > 0:
        print(f'🛡  Block: {state.BLOCK}')
    print(f'\nCURRENT HAND:')
    for (index, card) in enumerate(state.HAND, start=0):
        print(index, card.getSummary())

def startCombat():
    createEnemy()
    playerTurn(state.HP, state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE, state.ENERGY)

def discard():
    state.DISCARD_PILE += state.HAND
    state.HAND = []

def showDraw():
    print(f'DRAW PILE:')
    print(state.DRAW_PILE)

def showHand():
    print(f'\nCURRENT HAND:')
    print(state.HAND)

def showDiscard():
    print(f'\nDISCARD PILE:')
    print(state.DISCARD_PILE)

def showPiles():
    print('-' * 70 + f' [PILES]')
    showDraw()
    showHand()
    showDiscard()

def playerTurn(hp, enemy, hand, discard_pile, energy):
    draw()
    intent = enemyIntent(enemy)
    while state.HP > 0 or state.ENCOUNTER[-1].getHP() > 0:
        print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
        enemySummary(intent, enemy)
        playerSummary(energy)
        action = input('\nType the card index you want to play: ')
        if action.isdigit():
            index = int(action)
            try:
                print(f'TRY - Index played: {index}')
                cardPlayed = hand[index]
                if (energy - cardPlayed.getEnergy()) >= 0: #checks to see if you have enough energy to play the card
                    if cardPlayed.getType() == state.ACTIONS[2]: # checks if user input is attack action
                        energy -= cardPlayed.getEnergy()
                        # print(f'Enemy HP: {enemy.setHP()}')
                        # print(f'Attacking for {cardPlayed.getAttack()[0]} damage')
                        # enemy.setHP() -= cardPlayed.getAttack()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        discard_pile += state.HAND[cardPlayed]
                    elif cardPlayed.getType() == state.ACTIONS[3]: # checks if user input is block action
                        energy -= cardPlayed.getEnergy()
                        state.BLOCK += cardPlayed.getBlock()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                        hand.pop(index)
                        discard_pile.append(cardPlayed)
                else:
                    print('You need more energy to play that card!\n')
            except IndexError:
                print(f'EXCEPT - IndexError')
                pass
            except ValueError:
                print(f'EXCEPT - ValueError')
                if action == 'show':
                    showPiles()
                elif action == 'end':
                    discard()
                    # enemyTurn(hand, state.BLOCK, intent)
                else:
                    print(f'Invalid input.')
        if action == 'end':
            discard()
            enemyTurn(hand, state.BLOCK, intent)
        elif action == 'piles':
            showPiles()
        elif enemy.getHP() <= 0:
            print(f'You win! You beat the {enemy.getName()}')
        else:
            continue

buildDeck()
startCombat()