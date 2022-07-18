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
    return ENEMY[-1]

def draw():
    for i in range(DRAW_COUNT):
        card = DRAW_PILE.pop(-1)
        HAND.append(card)

def startCombat(hp, max_hp, energy, max_energy, hand, discard):
    draw()
    startPlayerTurn(hp, max_hp, energy, max_energy, hand, discard, createEnemy())

def startPlayerTurn(hp, max_hp, energy, max_energy, hand, discard, enemy):
    while energy > 0:
        enemySummary(enemy)
        playerSummary(hp, max_hp, energy, max_energy, hand)
        action = input('\nWhich card do you want to play? ')
        try:
            index = int(action)
            handChoice = hand[index]
            if handChoice.getType() == ACTIONS[1]:
                print(f'You used {handChoice.getEnergy()}💧 and attacked for {handChoice.getAttack()} {handChoice.getType()}!')
                energy -= 1
                hand.remove(handChoice)
                discard.append(handChoice)
                print(f'💧 Energy: {energy}/{max_energy}\n')
            elif handChoice.getType() == ACTIONS[2]:
                print(f'You used {handChoice.getEnergy()}💧 and blocked for {handChoice.getBlock()} {handChoice.getType()}!')
                energy -= 1
                hand.remove(handChoice)
                discard.append(handChoice)
                print(f'💧 Energy: {energy}/{max_energy}\n')
        except IndexError:
            pass
        except ValueError:
            if action == 'hand':
                print('Current Hand: {hand}')
            elif action == 'discard':
                print(f'Discard Pile: {discard}')
            elif action == 'end':
                print(f'Global energy: {ENERGY}')
                print(f'Function energy: {energy}')
                return energy
    action = input('You\'re out of energy! Type "end" to conclude your turn. ')
    if action == 'end':
        return hp, max_hp, energy, max_energy, hand, discard
    else:
        action = input('You\'re out of energy! Type "end" to conclude your turn. ')
    hp, max_hp, energy, max_energy, hand, discard
def endPlayerTurn():
    print(f'Hit endPlayerTurn function')
    pass
    # for card in HAND:
    #     print(card)
    #     HAND.remove(card)
    #     DISCARD_PILE.append(card)
    #     print(f'Discard Pile: {DISCARD_PILE}')

def enemySummary(enemy):
    print('-' * 70 + f' [Turn {TURN_COUNT}]')
    enemy.saySummary()
    print(f'{enemy.intent()}\n')

def playerSummary(hp, max_hp, energy, max_energy, hand):
    print(f'🙂 {NAME}')
    print(f'🩸 HP: {hp}/{max_hp}')
    print(f'💧 Energy: {energy}/{max_energy}\n')
    for (index, card) in enumerate(hand, start=0):
        print(index, card)

buildDeck()
startCombat(HP, MAX_HP, ENERGY, MAX_ENERGY, HAND, DISCARD_PILE)

print(f'Global energy (outside): {ENERGY}')
# Max ???s

# what order would you do for checking the main battle loop?
# best way to create iterators?
# is there an easier way to call class methods? 

# pull out parts of main battle loop into individual functions to make it easier to debug
# uses loops within summaries to continue actions
# try making a "game state" class to instantiate all needed global variables