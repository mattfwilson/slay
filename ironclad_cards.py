from vars import *
import itertools

class Card:
    id = itertools.count(0)

    def __init__(self):
        self.id = next(Card.id)

class Strike:
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

class Defend:
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

class Bash:
    def __init__(self):
        super().__init__()
        self.dmg_amount = 8
        self.energy = 2
        self.type = 'Attack'
        self.debuffs = state.DEBUFFS[0]

    def getEnergy(self):
        return self.energy

    def setEnergy(new_energy):
        self.energy = new_energy

    def getType(self):
        return self.type

    def getDebuffs(self):
        return self.debuffs

bash = Bash()
print(bash.getDebuffs())
