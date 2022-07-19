import itertools
import random

########################################################################

class Enemy:

    id = itertools.count(0)

    def __init__(self):
        self.id = next(Enemy.id)

########################################################################

class Boss:

    def __init__(self):
        self.bonusHP = .5
        self.bonusAttack = .5

########################################################################

class Pigeon(Enemy):

    def __init__(self):

        adjectives = ['Standard', 'Basic', 'Plebian', 'Undead', 'Armored', 'Elite', 'Untouchable']
        roll = random.choice(adjectives)
        name_adj = '🐦 ' + roll + ' Pigeon'

        super().__init__()
        self.name = name_adj
        self._hp = random.randint(35, 55)
        self.max_hp = self._hp

    def __repr__(self):
        return f'This is the  repr of {self.name}, id: {self.id}'

    def intro(self):
        print('\nYou encountered an enemy!')
        print(f'A {self.name} swoops down...\n')

    def summary(self):
        print(f'{self.name}')
        print(f'🩸 HP: {self._hp}/{self.max_hp}')

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getHP(self):
        return self._hp
    
    def setHP(self):
        return self._hp

    def getMaxHP(self):
        return self.max_hp

    def doDamage(self, damage):
        self.hp -= damage
        return self.hp

    def intent(self):
        attackValues = [6, 8, 10, 12]
        blockValues = [12, 14, 16, 18]
        intent = random.randint(1, 2)
        attack = random.choices(attackValues, weights=[1, 2, 6, 1])
        block = random.choices(blockValues, weights=[1, 8, 3, 2])
        if intent == 1:
            for i in attack: # prints intent without list brackets (better way to do this?)
                return f'💢 Enemy intends to ⚔  Attack for {i}.'
        else:
            for i in block:
                return f'💢 Enemy intends to 🛡  Block for {i}.'

class CatOfThondor(Enemy):

    def __init__(self):

        adjectives = ['Shrieking', 'Complacent', 'Regimented', 'Ghostly', 'Robotic', 'Frantic', 'Verbose']
        roll = random.choice(adjectives)
        name_adj = '😼 ' + roll + ' Cat Of Thondor'

        super().__init__()
        self.name = name_adj
        self._hp = random.randint(60, 75)
        self.max_hp = self._hp

    def __repr__(self):
        return f'This is the repr of {self.name}, id: {self.id}'

    def intro(self):
        print('\nYou encountered an enemy!')
        print(f'A {self.name} swoops down...\n')

    def summary(self):
        print(f'{self.name}')
        print(f'🩸 HP: {self._hp}/{self.max_hp}')

    def getID(self):
        return self.id

    def getHP(self):
        return self._hp
    
    def setHP(self):
        return self._hp

    def getMaxHP(self):
        return self.max_hp

    def doDamage(self, damage):
        self.hp -= damage
        return self.hp

    def intent(self):
        attackValues = [12, 14, 16, 18]
        blockValues = [6, 8, 10, 12]
        intent = random.randint(1, 2)
        attack = random.choices(attackValues, weights=[1, 2, 6, 1])
        block = random.choices(blockValues, weights=[1, 8, 3, 2])
        if intent == 1:
            for damage in attack: # prints intent without list brackets (better way to do this?)
                return f'💢 Enemy intends to ⚔  Attack for {damage}.'
        else:
            for blocked in block:
                return f'💢 Enemy intends to 🛡  Block for {blocked}.'