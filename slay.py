import itertools
import random

USER_LVL = 1
CURRENT_HP = 70
MAX_HP = 70
CURRENT_ENERGY = 3
MAX_ENERGY = 3
USER_GOLD = 0
SPIRE_LVL = 1
DECK_START = 8
CURRENT_HAND = []
DRAW_PILE = []
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
    for i in range(4):
        CURRENT_HAND.append(Attack())
        CURRENT_HAND.append(Defend())
    random.shuffle(CURRENT_HAND)

def showSummary():
    print(f'HP: {CURRENT_HP}/{MAX_HP}')
    print(f'Energy: {CURRENT_ENERGY}/{MAX_ENERGY}')
    print(f'Hand: {CURRENT_HAND}')

createDeck()
showSummary()