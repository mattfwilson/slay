from vars import *
import random
import itertools

class Card:
    id = itertools.count(0)

    def __init__(self):
        self.id = next(Card.id)

class Attack(Card):
    def __init__(self):
        super().__init__()
        amount = [6, 8, 10]
        attack = random.choices(amount, weights=[2, 4, 1])
        self._energy = 1
        self._type = state.ACTIONS[1]
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
        amount = [6, 8, 10]
        block = random.choices(amount, weights=[3, 6, 1])
        self._energy = 1
        self._type = state.ACTIONS[2]
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

class Draw(Card):
    def __init__(self):
        super().__init__()
        self._energy = 1
        self._draw = 2
        self._type = state.ACTIONS[0]

    def setEnergy(self):
        return self._energy

    def getEnergy(self):
        return self._energy

    def setType(self):
        return self._type

    def getType(self):
        return self._type
    
    def setDraw(self):
        return self._draw

    def getDraw(self):
        return self._draw

    def getSummary(self):
        return f'♻  {self._type} {self._draw} for {self._energy}💧'

    def __repr__(self):
        return f'{state.ACTIONS[0]} {self._draw}'

