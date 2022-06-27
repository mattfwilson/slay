import random
import itertools

hand = []

class Card:
    id = itertools.count(1).__next__

    def __init__(self):
        self.id = Card.id()

    def __repr__(self):
        return f'Card: {self.id}'

class Attack(Card):
    def __init__(self, id):
        self.damage = 6

class Defend(Card):
    def __init__(self, id):
        self.block = 6

hand.append(Card())
hand.append(Card())
hand.append(Card())

print(hand)

