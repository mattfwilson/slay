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
    enemy_pool = [Pigeon()]
    enemy = random.choices(enemy_pool, weights=[1]) # add more weights after testing
    ENEMY.append(enemy[0])
    ENEMY[-1].intro()

def draw():
    for i in range(DRAW_COUNT):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def testPool():
    for num in range(COUNTER):
        createEnemy()
    for enemy in ENEMY:
        print(f'{enemy.sayName()} {enemy.sayID()}, {enemy.sayHP()}/{enemy.sayMaxHP()} - {enemy.intent()}')

def startCombat():
    createEnemy()
    startTurn()

def startTurn():
    global TURN_COUNT
    global ENERGY
    TURN_COUNT += 1
    ENERGY = MAX_ENERGY
    draw()
    playerSummary()
    enemySummary()

# start WHILE:
# PLAYER_HP > 0 or ENEMY_HP > 0: "I'm not dead. Enemy is not dead"
# PLAYCARD is in HAND: "Card I played is in my current hand"
# PLAYCARD == Block or Attack: "Check to what card type I played"
# PLAYCARD ENERGY >= ENERGY: I can afford the energy cost of card I played

    while HP > 0:
        PLAYCARD = input('\nWhat do you want to do? ')
        count = 0
        for card in HAND:
            if PLAYCARD in HAND:
                count += 1
                HAND.pop(PLAYCARD)
                DISCARD_PILE.append(PLAYCARD)
                print(HAND)
                print(DISCARD_PILE)
            elif PLAYCARD == 'hand':
                print(HAND)
                break
            elif PLAYCARD == 'discard':
                print(DISCARD_PILE)
                break
            else:
                print(f'{PLAYCARD} not in hand...')
                PLAYCARD = input('What do you want to do? ')
        if count == 0:
            print('You have no move. Type "end" to conclude your turn.')

def endTurn():
    HAND.pop(len(range(HAND)))

def playerSummary():
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    print(f'🙂 {NAME}')
    print(f'🩸 HP: {HP}/{MAX_HP}')
    print(f'💧 Energy: {ENERGY}/{MAX_ENERGY}')
    for card in HAND:
        print(card, end=' ')

def enemySummary():
    ENEMY[-1].saySummary()
    print(f'{ENEMY[-1].intent()}')

# main game execution
buildDeck()
startCombat()