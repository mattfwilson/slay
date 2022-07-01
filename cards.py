import itertools

CARD_TYPES = ['Base', 'Attack', 'Block', 'Skill']

class Card:

    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Card.id()
        self.type = CARD_TYPES[0]

class Attack(Card):
    
    def __init__(self):
        super().__init__()
        self.energy = 1
        self.type = CARD_TYPES[1]
        self.attack = 6

    def __repr__(self):
        return f'({self.energy}) {self.type} {self.attack}'

class Defend(Card):

    def __init__(self):
        super().__init__()
        self.energy = 1
        self.type = CARD_TYPES[2]
        self.block = 6

    def __repr__(self):
        return f'({self.energy}) {self.type} {self.block}'