from vars import *
import random
import itertools

class Card:

    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Card.id()

class Attack(Card):

    def __init__(self):
        amount = [4, 6, 8]
        attack = random.choices(amount, weights=[2, 4, 1])
        super().__init__()
        self.energy = 1
        self.type = ACTIONS[1]
        self.attack = attack

    def sayEnergy(self):
        return self.energy

    def sayType(self):
        return self.type

    def sayAttack(self):
        return self.attack

    def __repr__(self):
        return f'⚔  {self.type} {self.attack} for {self.energy}💧'

class Block(Card):

    def __init__(self):
        amount = [4, 6, 8, 10]
        block = random.choices(amount, weights=[1, 2, 6, 1])
        super().__init__()
        self.energy = 1
        self.type = ACTIONS[2]
        self.block = block

    def sayEnergy(self):
        return self.energy

    def sayType(self):
        return self.type

    def sayBlock(self):
        return self.block

    def __repr__(self):
        return f'🛡  {self.type} {self.block} for {self.energy}💧'