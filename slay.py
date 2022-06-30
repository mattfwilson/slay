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
    print('-' * 50 + f' Turn {TURN_COUNT} ' + '-' * 50)
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

class Enemy():
     id = itertools.count(0).__next__

     def __init__(self):
        self.id = Enemy.id()

class Slime():

    def __init__(self):
        moves = [3, 4, 5, 6, 7, 8, 10]
        attack = random.choices(moves, weights=[8, 8, 8, 2, 2, 1, 1])
        block = random.choices(moves, weights=[1, 3, 3, 8, 8, 5, 3])
        self.name = 'Slime Noob'
        self.hp = 40
        self.max_hp = 40
        self.attack = attack
        self.defend = block

    def sayName(self):
        print(self.name)

    def sayStats(self):
        print(f'\n{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}\n')

    def __repr__(self):
        print(f'\n{self.name} casually slides in...')

class Pigeon():

    def __init__(self):
        moves = [4, 5, 6, 7, 8, 10]
        attack = random.choices(moves, weights=[1, 2, 4, 6, 8, 4])
        block = random.choices(moves, weights=[8, 8, 6, 3, 1, 1])
        self.name = 'Basic Pigeon Soldier'
        self.hp = 25
        self.max_hp = 25
        self.attack = attack
        self.defend = block

    def sayName(self):
        print(self.name)

    def sayStats(self):
        print(f'\n{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}\n')

    def __repr__(self):
        print(f'\n{self.name} careens down...')

enemies = (Slime, Pigeon)
enemies_fought = []

for i in range(5):
    instance = random.choice(enemies)
    enemies_fought.append(instance)
instance().__repr__()