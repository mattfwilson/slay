# need to figure out why the main gamp loop can't call enemy from GameState class
# remove block after enemy's turn ends

from vars import *
from enemy import *
from cards import *
import time
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

def enemyIntent(intent):
    if intent[0] == 1:
        state.ENEMY_ATTACK = intent[1]
    else:
        state.ENEMY_BLOCK = intent[1]

def createEnemy():
    enemy_pool = [Pigeon()]
    enemy = random.choices(enemy_pool, weights=[1])
    state.ENCOUNTER.append(enemy[0])
    enemy = state.ENCOUNTER[-1]
    enemy.intro()
    return enemy

def enemyTurn(hand, block, intent):
    if intent[0] == 1:
        if intent[1] >= block:
            state.HP -= intent[1] - block
            print(f'Enemy attacks for {intent[1]}!\n')
        else:
            block -= intent[1]
    else:
        print(f'Enemy blocks for {intent[1]}!\n')
        state.ENEMY_BLOCK = intent[1]
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
    state.FLOOR_COUNT += 1
    createEnemy()
    playerTurn(state.HP, state.ENCOUNTER[-1], state.HAND, state.DISCARD_PILE, state.ENERGY)

def discard():
    state.DISCARD_PILE += state.HAND
    state.HAND = []

def playerTurn(hp, enemy, hand, discard_pile, energy):
    state.TURN_COUNT += 1
    draw()
    intent = enemy.intent()
    while hp > 0 and enemy.getHP() > 0:
        print('-' * 50 + f' [Floor {state.FLOOR_COUNT} | [Turn {state.TURN_COUNT}]')
        enemySummary(enemy, intent)
        playerSummary(energy)
        action = input('\nWhich card do you want to play: ')
        if action.isdigit():
            index = int(action)
            try:
                cardPlayed = hand[index]
                if (energy - cardPlayed.getEnergy()) >= 0: #checks to see if you have enough energy to play the card
                    if cardPlayed.getType() == state.ACTIONS[2]: # checks if user input is attack action
                        energy -= cardPlayed.getEnergy()
                        print(f'You used {cardPlayed.getEnergy()}💧 and attacked for {cardPlayed.getAttack()[0]} {cardPlayed.getType()}!\n')
                        time.sleep(1)
                        if state.ENEMY_BLOCK > 0: # check to see if enemy has block
                            state.ENEMY_BLOCK -= cardPlayed.getAttack()[0]
                            if state.ENEMY_BLOCK < 0: # check if player damaged enemy more than block
                                unblocked = abs(state.ENEMY_BLOCK)
                                print(f'You broke the block and hit the enemy for {unblocked} damage!')
                                enemy.setHP(unblocked)
                                hand.pop(index)
                                discard_pile.append(cardPlayed)
                                time.sleep(1)
                            else:
                                print(f'You damaged {cardPlayed.getAttack()[0]} points of the enemy\'s block')
                                hand.pop(index)
                                discard_pile.append(cardPlayed)
                                time.sleep(1)
                        else:
                            print(f'You hit the enemy for {cardPlayed.getAttack()[0]} damage!')
                            enemy.setHP(cardPlayed.getAttack()[0])
                            hand.pop(index)
                            discard_pile.append(cardPlayed)
                            time.sleep(1)
                    elif cardPlayed.getType() == state.ACTIONS[3]: # checks if user input is block action
                        energy -= cardPlayed.getEnergy()
                        state.BLOCK += cardPlayed.getBlock()[0]
                        print(f'You used {cardPlayed.getEnergy()}💧 and blocked for {cardPlayed.getBlock()[0]} {cardPlayed.getType()}!\n')
                        hand.pop(index)
                        discard_pile.append(cardPlayed)
                        time.sleep(1)
                else:
                    print('You need more energy💧 to play that card!\n')
            except IndexError:
                pass
            except ValueError:
                if action == 'show':
                    showPiles()
                elif action == 'end':
                    discard()
                    state.ENEMY_BLOCK = 0
                    enemyTurn(hand, state.BLOCK, intent)
                else:
                    print(f'Invalid input.')
        if action == 'end':
            discard()
            state.ENEMY_BLOCK = 0
            enemyTurn(hand, state.BLOCK, intent)
        elif action == 'piles':
            showPiles()
        elif enemy.getHP() <= 0:
            print(f'🏆 You win! You beat the {enemy.getName()}')
            action = input('\nProceed to next floor?: ')
        else:
            continue
    
    if hp <= 0:
        print(f'💀 {state.NAME} was defeated. You lost.')
        quit()
    else:
        print(f'🏆 You defeated the {enemy.getName()}!')
        quit()

buildDeck()
startCombat()

# is there a better/more efficient way to check for if int or str in main loop?
# how would you retain enemy's intended block for an additional turn