# need to figure out why the main gamp loop can't call enemy from GameState class
# I think the main try is causing cards to discard at some interval when the player ends their turn

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
    for count in range(state.DRAW_COUNT):
        if len(state.DRAW_PILE) < state.DRAW_COUNT:
            for card in state.DISCARD_PILE:
                state.DISCARD_PILE.pop(card)
                state.DRAW_PILE.append(card)
            random.shuffle(state.DRAW_PILE)
        else:
            state.HAND.append(random.choice(state.DRAW_PILE))


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
        print(f'⚔  Enemy intends to Attack for {intent[1]}\n')
    else:
        print(f'🛡  Enemy intends to Block for {intent[1]}\n')
        
def enemyTurn(hand, block, intent):
    print(f'start of enemyTurn function')
    for i in intent[1]:
        action = i
    if intent[0] == 1:
        state.HP -= action
        print(f'Enemy attacks for {intent[1]}')
        print(state.HP)
    else:
        print(f'Enemy blocks lol for {intent[1]}')
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
    print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
    playerTurn(state.HP, state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE, state.ENERGY)

def discard(hand, discard_pile):
    for card in hand:
        hand.remove(card)
        discard_pile.append(card)

def playerTurn(hp, enemy, hand, discard_pile, energy):
    draw()
    intent = enemyIntent(enemy)
    while state.HP > 0 or enemy.getHP() > 0:
        enemySummary(intent, enemy)
        playerSummary(energy)
        action = input('\nType the card index you want to play: ')
        try:
            index = int(action)
            cardPlayed = hand[index]
            if (energy - cardPlayed.getEnergy()) >= 0: #checks to see if you have enough energy to play the card
                if cardPlayed.getType() == state.ACTIONS[2]: # checks if user input is attack action
                    energy -= cardPlayed.getEnergy()
                    # print(f'Enemy HP: {enemy.setHP()}')
                    # print(f'Attacking for {cardPlayed.getAttack()[0]} damage')
                    # enemy.setHP() -= cardPlayed.getAttack()[0]
                    print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                    hand.remove(cardPlayed)
                    discard_pile.append(cardPlayed)
                elif cardPlayed.getType() == state.ACTIONS[3]: # checks if user input is block action
                    energy -= cardPlayed.getEnergy()
                    print(energy)
                    print(cardPlayed.getEnergy())
                    state.BLOCK += cardPlayed.getBlock()[0]
                    print(f'You used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                    hand.remove(cardPlayed)
                    discard_pile.append(cardPlayed)
            else:
                print('You don\'t have enough energy!\n')
        except IndexError:
            pass
        except ValueError:
            if action == 'hand':
                showHand()
            elif action == 'draw':
                showDraw()
            elif action == 'discard':
                showDiscard()
            elif action == 'end':
                discard(hand, discard_pile)
                enemyTurn(hand, state.BLOCK, intent)
        if action == 'end':
            discard(hand, discard_pile)
            showPiles()
            enemyTurn(hand, state.BLOCK, intent)
    if enemy.getHP() <= 0:
        print(f'You win! You beat the {enemy.getName()}')
    else:
        action = input('\nType the card index you want to play: ')

buildDeck()
startCombat()
