import itertools
import random

USER_LVL = 1
CURRENT_HP = 70
MAX_HP = 70
CURRENT_ENERGY = 1
MAX_ENERGY = 3
USER_GOLD = 0
COMBAT_COUNT = 1
TURN_COUNT = 1
DRAW_COUNT = 5
DRAW_PILE = []
CURRENT_HAND = []
DISCARD_PILE = []
CARD_TYPES = ['Base', 'Attack', 'Defend', 'Skill']

class Card:
    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Card.id()
        self.type = CARD_TYPES[0]

class Attack(Card):
    def __init__(self):
        super().__init__()
        self.type = CARD_TYPES[1]
        self.attack = 6

    def __repr__(self):
        return f'({self.id}) {self.type} {self.attack}'

class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = CARD_TYPES[2]
        self.block = 6

    def __repr__(self):
        return f'({self.id}) {self.type} {self.block}'

def createDeck():
    for i in range(DRAW_COUNT):
        DRAW_PILE.append(Attack())
        DRAW_PILE.append(Defend())
    random.shuffle(DRAW_PILE)

def showSummary():
    print('-' * 100)
    print(f'Turn: {TURN_COUNT}')
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Cards: {CURRENT_HAND}')

def startCombat():
    pass

def drawCards():
    for i in range(5):
        card = DRAW_PILE.pop(-1)
        CURRENT_HAND.append(card)

def startTurn():
    global CURRENT_ENERGY
    global TURN_COUNT
    CURRENT_ENERGY = MAX_ENERGY
    drawCards()
    showSummary()

def enemyTurn():
    pass

def endTurn():
    CURRENT_HAND.pop(len(range(CURRENT_HAND)))
    TURN_COUNT += 1
    enemyTurn()
    
createDeck()
startTurn()

class Slime():

    def __init__(self):
        attack = random.randint(3, 10)
        block = random.randint(4, 9)
        self.name = 'Noob Slime'
        self.hp = 37
        self.max_hp = 37
        self.attack = attack
        self.defend = block

    def sayName(self):
        print(self.name)

    def sayStats(self):
        print('-' * 100)
        print(self.name)
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}')


    def __repr__(self):
        print(f'Attack: {self.attack}, Block: {self.defend}')

Slime().sayStats()

