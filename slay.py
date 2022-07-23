# need to figure out why the main gamp loop can't call enemy from GameState class
# I think the main try is causing cards to discard at some interval when the player ends their turn

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
        
def enemyTurn(intent):
    print(f'start of enemyTurn function')
    if intent[0] == 1:
        print(f'Enemy attacks lol for {intent}')
    else:
        print(f'Enemy blocks lol for {intent}')

def playerSummary():
    print(f'🙂 {state.NAME}')
    print(f'🩸 HP: {state.HP}/{state.MAX_HP}')
    print(f'💧 Energy: {state.ENERGY}/{state.MAX_ENERGY}')
    if state.BLOCK > 0:
        print(f'🛡  Block: {state.BLOCK}')
    print(f'\nCURRENT HAND:')
    for (index, card) in enumerate(state.HAND, start=0):
        print(index, card.getSummary())

def startCombat():
    createEnemy()
    print('-' * 70 + f' [Turn {state.TURN_COUNT}]')
    draw()
    playerTurn(state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE)

def draw():
    for card in state.DECK:
        state.DRAW_PILE.append(card)
    for count in range(state.DRAW_COUNT):
        state.HAND.append(random.choice(state.DRAW_PILE))

def discard(hand, discard_pile):
    for card in hand:
        hand.remove(card)
        discard_pile.append(card)

def showDraw():
    print(f'\nDRAW PILE:')
    for card in state.DRAW_PILE:
        print(card.getSummary())

def showHand():
    print(f'\nCURRENT HAND:')
    for card in state.HAND:
        print(card.getSummary())

def showDiscard():
    print(f'\nDISCARD PILE:')
    for card in state.DISCARD_PILE:
        print(card.getSummary())

def showPiles():
    showDraw()
    showHand()
    showDiscard()

def playerTurn(enemy, hand, discarded):
    intent = enemyIntent(enemy)
    while state.HP > 0 or enemy.getHP() > 0:
        while state.ENERGY > 0:
            enemySummary(intent, enemy)
            playerSummary()
            action = input('\nType the card index you want to play: ')
            try:
                index = int(action)
                cardPlayed = hand[index]
                if (state.ENERGY - cardPlayed.getEnergy()) >= 0: #checks to see if you have enough energy to play the card
                    if cardPlayed.getType() == state.ACTIONS[2]: # checks if attack
                        state.ENERGY -= cardPlayed.getEnergy()
                        # print(f'Enemy HP: {enemy.setHP()}')
                        # print(f'Attacking for {cardPlayed.getAttack()[0]} damage')
                        # enemy.setHP() -= cardPlayed.getAttack()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        hand.remove(cardPlayed)
                        discarded.append(cardPlayed)
                    elif cardPlayed.getType() == state.ACTIONS[3]: # checks if block
                        state.ENERGY -= cardPlayed.getEnergy()
                        state.BLOCK += cardPlayed.getBlock()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                        hand.remove(cardPlayed)
                        discarded.append(cardPlayed)
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
                    discard(hand, discarded)
                    showPiles()
                    # enemyTurn(state.HP, state.BLOCK, intent)
                    break
            if action == 'end':
                discard(hand, discarded)
                showPiles()
                enemyTurn(hand, state.BLOCK, intent)
                break
            # else:
            #     action = input('ELSE if not int or not actions: Type "end" to conclude your turn: ')
        if enemy.getHP() <= 0:
            print(f'You win! You beat the {enemy.getName()}')
        else:
            print(f'You died. End of player/enemy HP loop')

buildDeck()
startCombat()
