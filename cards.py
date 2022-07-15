from vars import *
import random
import itertools

class Card:

    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Card.id()

class Attack(Card):

    def __init__(self):
        super().__init__()
        amount = [4, 6, 8]
        attack = random.choices(amount, weights=[2, 4, 1])
        self._energy = 1
        self._type = ACTIONS[1]
        self._attack = attack

    def setEnergy(self):
        return self._energy
    
    def getEnergy(self):
        return self._energy

    def setType(self):
        return self._type

    def getType(self):
        return self._type

    def setAttack(self):
        return self._attack

    def getAttack(self):
        return self._attack

    def __repr__(self):
        return f'⚔  {self._type} {self._attack} for {self._energy}💧'

class Block(Card):

    def __init__(self):
        super().__init__()
        amount = [4, 6, 8, 10]
        block = random.choices(amount, weights=[1, 2, 6, 1])
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