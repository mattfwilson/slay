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

def draw():
    for i in range(DRAW_COUNT):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def test():
    for num in range(COUNTER):
        createEnemy()
    for enemy in ENEMY:
        print(f'{enemy.sayName()} {enemy.sayID()}, {enemy.sayHP()}/{enemy.sayMaxHP()} - {enemy.intent()}')

def startCombat():
    createEnemy()
    startTurn()

# def main():
#     global ENERGY
#     while ENERGY > 0:
#         action = int(input('\nWhich card do you want to play? '))
#         handIndex = HAND[action]
#         if handIndex.sayType() == ACTIONS[1]:
#             HAND.remove(handIndex)
#             DISCARD_PILE.append(handIndex)
#             print(f'You used {handIndex.sayEnergy()}💧 and attacked for {HAND[action].sayAttack()}!')
#             ENERGY -= 1
#             print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
#         elif handIndex.sayType() == ACTIONS[2]:
#             print(f'You used {handIndex.sayEnergy()}💧 and blocked for {HAND[action].sayBlock()}!')
#             ENERGY -= 1
#             print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
#         elif action == 'hand':
#             print(HAND)
#         elif action == 'discard':
#             print(DISCARD_PILE)
#         else:
#             print('Invalid input...')

def startTurn():
    global TURN_COUNT
    global ENERGY
    # TURN_COUNT += 1
    # ENERGY = MAX_ENERGY
    draw()
    enemySummary()
    playerSummary()
    # main()

def endTurn():
    for card in HAND:
        HAND.pop(card)

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

# Max ???s

# what order would you do for checking the main battle loop?
# best way to create iterators?
# is there an easier way to call class methods? 

# pull out parts of main battle loop into individual functions to make it easier to debug
# uses loops within summaries to continue actions
# try making a "game state" class to instantiate all needed global variables