from vars import *
import itertools

class Card:

    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Card.id()

class Attack(Card):
    
    def __init__(self):
        super().__init__()
        self.energy = 1
        self.type = ACTIONS[1]
        self.attack = 6

    def sayEnergy(self):
        return self.energy

    def sayType(self):
        return self.type

    def sayAttack(self):
        return self.attack

    def __repr__(self):
        return f'[{self.type} {self.attack} for {self.energy} 💧]'

class Block(Card):

    def __init__(self):
        super().__init__()
        self.energy = 1
        self.type = ACTIONS[2]
        self.block = 6

    def sayEnergy(self):
        return self.energy

    def sayType(self):
        return self.type

    def sayBlock(self):
        return self.block

    def __repr__(self):
        return f'[{self.type} {self.block} for {self.energy} 💧]'