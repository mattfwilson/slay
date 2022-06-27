import itertools
import time
import operator

hand = []
card_types = ['Attack', 'Defend', 'Skill', 'Power', 'Curse']

class Card:

    id = itertools.count(1).__next__

    def __init__(self):
        self.id = Card.id()

    def __repr__(self):
        return f'Card {self.id}'

class Attack(Card):
    def __init__(self):
        super().__init__()
        self. type = card_types[0]
        self.damage = 6
    
    def __repr__(self):
        return f'{self.type} Card {self.id}'

class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = card_types[1]
        self.block = 6
    
    def __repr__(self):
        return f'{self.type} Card {self.id}'

hand.append(Card())
hand.append(Attack())
hand.append(Defend())

print(hand)