from vars import *
import itertools

class Card:
    id = itertools.count(0)

    def __init__(self):
        self.id = next(Card.id)

class Strike(Card):
    def __init__(self):
        super().__init__()
        self.dmg_amount = 6
        self.energy = 1
        self.type = 'Attack'

    def getEnergy(self):
        return self.energy

    def setEnergy(self, new_energy):
        self.energy = new_energy

    def getType(self):
        return self.type

class Defend(Card):
    def __init__(self):
        super().__init__()
        self.block_amount = 5
        self.energy = 1
        self.type = 'Defend'

    def getEnergy(self):
        return self.energy

    def setEnergy(self, new_energy):
        self.energy = new_energy

    def getType(self):
        return self.type

class Bash(Card):
    def __init__(self):
        super().__init__()
        self.type = 'Attack'
        self.energy = 2
        self.dmg_amount = 8
        self.debuffs = state.DEBUFFS[0]
        self.debuff_amount = 2

    def getType(self):
        return self.type
    
    def getEnergy(self):
        return self.energy

    def setEnergy(self, new_energy):
        self.energy = new_energy

    def getDamage(self):
        return self.dmg_amount

    def setDamage(self, new_dmg):
        self.dmg_amount = new_dmg

    def getDebuffs(self):
        return self.debuffs

    def setDebuffs(self, new_buff):
        self.debuffs = new_buff

    def getDebuffAmount(self):
        return self.debuff_amount

    def setDebuffAmount(self, new_amount):
        self.debuff_amount = new_amount

    def upgrade(self):
        self.dmg_amount = 10
        self.debuff_amount = 3

bash = Bash()
print(f'Deal {bash.getDamage()} damage.')
print(f'Apply {bash.getDebuffAmount()} {bash.getDebuffs()}.\n')

bash.upgrade()

print(f'Deal {bash.getDamage()} damage.')
print(f'Apply {bash.getDebuffAmount()} {bash.getDebuffs()}.\n')
