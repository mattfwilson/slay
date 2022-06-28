import itertools
import random

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

    def __repr__(self):
        return f'({self.id}) {self.type} Card'

class Attack(Card):
    def __init__(self):
        super().__init__()
        self.type = CARD_TYPES[1]

class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = CARD_TYPES[2]

def createDeck():
    for i in range(4):
        CURRENT_HAND.append(Attack())
        CURRENT_HAND.append(Defend())
    print(CURRENT_HAND)

createDeck()