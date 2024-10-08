from vars2 import *
from cultist import *
from cards import *
import time
import random

def buildDeck():
    for count in range(state.START_ATTACK):
        state.DECK.append(Attack())
    for count in range(state.START_BLOCK):
        state.DECK.append(Block())
    for count in range(state.START_DRAW):
        state.DECK.append(Draw())
    state.DRAW_PILE = state.DECK
    random.shuffle(state.DRAW_PILE)

def draw(draw_amount):
    if len(state.DRAW_PILE) < draw_amount:
        for card in state.DISCARD_PILE:
            returned = state.DISCARD_PILE.pop(-1)
            state.DRAW_PILE.append(returned)
        random.shuffle(state.DRAW_PILE)
        for count in range(draw_amount):
            drawn = state.DRAW_PILE.pop(-1)
            state.HAND.append(drawn)
    else:
        for count in range(draw_amount):
            drawn = state.DRAW_PILE.pop(-1)
            state.HAND.append(drawn)

def enemyIntent(intent):
    if intent[0] == 1:
        state.ENEMY_ATTACK = intent[1]
    else:
        state.ENEMY_BLOCK = intent[1]

def createEnemy():
    enemy_pool = [Cultist()]
    enemy = random.choices(enemy_pool, weights=[1])
    state.ENCOUNTER.append(enemy[0])
    enemy = state.ENCOUNTER[-1]
    return enemy

def enemyTurn(block, intent):
    if intent[0] == 1:
        if intent[1] >= block:
            state.HP -= intent[1] - block
            print(f'\n{state.ENCOUNTER[-1].getName()} attacks for {intent[1]}!\n')
            time.sleep(1)
        else:
            block -= intent[1]
    else:
        state.ENEMY_BLOCK = intent[1]
        print(f'\n{state.ENCOUNTER[-1].getName()} blocks for {intent[1]}!\n')
        time.sleep(1)
    state.BLOCK = 0
    playerTurn(state.HP, state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE, state.ENERGY)

def enemySummary(enemy, intent):
    enemy.summary()
    if state.ENEMY_BLOCK > 0:
        print(f'🛡  Enemy Block: {state.ENEMY_BLOCK}')
    if intent[0] == 1:
        print(f'⚔  Enemy intends to Attack for {intent[1]}\n')
    else:
        print(f'🛡  Enemy intends to Block for {intent[1]}\n')

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

def discardHand():
    state.DISCARD_PILE += state.HAND
    state.HAND = []

def playerTurn(hp, enemy, hand, discard_pile, energy):
    state.TURN_COUNT += 1
    draw(state.TURN_DRAW)
    intent = enemy.intent()
    while hp > 0 and enemy.getHP() > 0:
        print('-' * 30 + f' [Floor {state.FLOOR_COUNT} | [Turn {state.TURN_COUNT}]')
        enemySummary(enemy, intent)
        playerSummary(energy)
        action = input('\nWhich card do you want to play: ')
        if action.isdigit():
            index = int(action)
            try:
                cardPlayed = hand[index]
                if (energy - cardPlayed.getEnergy()) >= 0: # checks to see if you have enough energy to play the card
                    # Draw Card
                    if cardPlayed.getType() == state.ACTIONS[0]:
                        energy -= cardPlayed.getEnergy()
                        print(f'{state.NAME} used {cardPlayed.getEnergy()}💧 and played {cardPlayed.getType()} {cardPlayed.getDraw()}!\n')
                        draw(cardPlayed.getDraw())
                        print(f'You play {cardPlayed} draw 2 cards.')
                        hand.pop(index)
                        discard_pile.append(cardPlayed)
                        time.sleep(1)

                    # Attack Card
                    elif cardPlayed.getType() == state.ACTIONS[1]:
                        energy -= cardPlayed.getEnergy()
                        print(f'{state.NAME} used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        time.sleep(1)
                        if state.ENEMY_BLOCK > 0:
                            state.ENEMY_BLOCK -= cardPlayed.getAttack()[0]
                            if state.ENEMY_BLOCK < 0:
                                unblocked = abs(state.ENEMY_BLOCK)
                                print(f'{state.NAME} broke enemy\'s block and hit for {unblocked} damage!')
                                enemy.minusHP(unblocked)
                                hand.pop(index)
                                discard_pile.append(cardPlayed)
                                time.sleep(1)
                            else:
                                print(f'{state.NAME} damaged {cardPlayed.getAttack()[0]} points of the enemy\'s block')
                                hand.pop(index)
                                discard_pile.append(cardPlayed)
                                time.sleep(1)
                        else:
                            print(f'{state.NAME} hit the enemy for {cardPlayed.getAttack()[0]} damage!')
                            enemy.minusHP(cardPlayed.getAttack()[0])
                            hand.pop(index)
                            discard_pile.append(cardPlayed)
                            time.sleep(1)
                    # Block Card
                    elif cardPlayed.getType() == state.ACTIONS[2]:
                        energy -= cardPlayed.getEnergy()
                        print(f'{state.NAME} used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                        state.BLOCK += cardPlayed.getBlock()[0]
                        time.sleep(1)
                        print(f'{state.NAME} gained {cardPlayed.getBlock()[0]} Block.')
                        hand.pop(index)
                        discard_pile.append(cardPlayed)
                        time.sleep(1)
                    else:
                        print(f'Invalid input. Try again.\n')
                else:
                    print('You need more 💧 to play that card!\n')
            except IndexError:
                pass
            except ValueError:
                if action == 'show':
                    showPiles()
                elif action == 'end':
                    discardHand()
                    state.ENEMY_BLOCK = 0
                    enemyTurn(state.BLOCK, intent)
        if action == 'end':
            discardHand()
            state.ENEMY_BLOCK = 0
            enemyTurn(state.BLOCK, intent)
        elif action == 'piles':
            showPiles()
        elif enemy.getHP() <= 0:
            print(f'🏆 {state.NAME} wins! The {enemy.getName()} has been defeated.')
            action = input('\nProceed to next floor?: ')
        else:
            continue
    if hp <= 0:
        print(f'\n💀 {state.NAME} was defeated...')
        quit()
    else:
        print(f'\n🏆 {state.NAME} defeated the {enemy.getName()}!')
        quit()

def main():
    createEnemy()
    startCombat()
    discardHand()

buildDeck()
startCombat()

