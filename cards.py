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
        self._type = state.ACTIONS[2]
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

    def getSummary(self):
        return f'⚔  {self._type} {self._attack[0]} for {self._energy}💧'

    def __repr__(self):
        for attack in self._attack:
            return f'Attack {attack}'

class Block(Card):

    def __init__(self):
        super().__init__()
        amount = [4, 6, 8, 10]
        block = random.choices(amount, weights=[1, 2, 6, 1])
        self._energy = 1
        self._type = state.ACTIONS[3]
        self._block = block

    def setEnergy(self):
        return self._energy

    def getEnergy(self):
        return self._energy

    def setType(self):
        return self._type

    def getType(self):
        return self._type

    def setBlock(self):
        return self._block

    def getBlock(self):
        return self._block

    def getSummary(self):
        return f'🛡  {self._type} {self._block[0]} for {self._energy}💧'

    def __repr__(self):
        for block in self._block:
            return f'Block {block}'