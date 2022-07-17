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
    startPlayerTurn()

def checkInput(input):
    try:
        val = int(input)
        return True
        print('Input is an integer. Number = ', val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return False
            print('Input is a float. Number = ', val)
        except ValueError:
            print('Input is a string.')

def main():
    global TURN_COUNT
    global ENERGY
    while ENERGY > 0:
        enemySummary()
        playerSummary()
        action = input('\nWhich card do you want to play? ')
        try:
            index = int(action)
            handChoice = HAND[index]
            if handChoice.getType() == ACTIONS[1]:
                print(f'You used {handChoice.getEnergy()}💧 and attacked for {handChoice.getAttack()} {handChoice.getType()}!')
                ENERGY -= 1
                HAND.remove(handChoice)
                DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
            elif handChoice.getType() == ACTIONS[2]:
                print(f'You used {handChoice.getEnergy()}💧 and blocked for {handChoice.getBlock()} {handChoice.getType()}!')
                ENERGY -= 1
                HAND.remove(handChoice)
                DISCARD_PILE.append(handChoice)
                print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}\n')
        except ValueError:
            if action == 'hand':
                print(HAND)
            elif action == 'discard':
                print(DISCARD_PILE)
            else:
                print('Invalid input...')
    print('You\'re out of energy!')

def startPlayerTurn():
        draw()
        main()

def endTurn():
    for card in HAND:
        HAND.remove(card)
        DISCARD_PILE.append(card)

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