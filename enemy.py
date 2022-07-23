import itertools
import random

class Enemy:

    id = itertools.count(0)

    def __init__(self):
        self.id = next(Enemy.id)

class Pigeon(Enemy):

    def __init__(self):
        adj = ['Standard', 'Basic', 'Plebian', 'Undead', 'Armored', 'Elite', 'Untouchable']
        roll = random.choice(adj)
        name_adj = '🐦 ' + roll + ' Pigeon'

        super().__init__()
        self.name = name_adj
        self._hp = random.randint(35, 55)
        self.max_hp = self._hp

    def __repr__(self):
        return f'__repr__ for {self.name}, id: {self.id}'

    def intro(self):
        print('\nYou encountered an enemy!')
        print(f'A {self.name} swoops down...\n')

    def summary(self):
        print(f'\n{self.name}')
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
            return intent, attack
        else:
            return intent, block

class CatOfThondor(Enemy):

    def __init__(self):

        adj = ['Shrieking', 'Complacent', 'Regimented', 'Ghostly', 'Robotic', 'Frantic', 'Verbose']
        roll = random.choice(adj)
        name_adj = '😼 ' + roll + ' Cat Of Thondor'

        super().__init__()
        self.name = name_adj
        self._hp = random.randint(60, 75)
        self.max_hp = self._hp

    def __repr__(self):
        return f'__repr__ for {self.name}, id: {self.id}'

    def intro(self):
        print('\nYou encountered an enemy!')
        print(f'A {self.name} swoops down...\n')

    def summary(self):
        print(f'\n{self.name}')
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
        attackValues = [12, 14, 16, 18]
        blockValues = [6, 8, 10, 12]
        intent = random.randint(1, 2)
        attack = random.choices(attackValues, weights=[1, 2, 6, 1])
        block = random.choices(blockValues, weights=[1, 8, 3, 2])
        if intent == 1:
            return intent, attack
        else:
            return intent, block
