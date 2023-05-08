import itertools

class DefectCard:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(DefectCard.id)
        self._character = 'Defect'

class BallLightning(DefectCard):
    def __init__(self, upgraded):
        super().__init__()
        self._name = 'Ball Lightning'
        self._rarity = 'Common'
        self._upgrade = upgraded
        self._energy = 1
        self._damage = 7
        self._block = 0
        self._channel_type = 'Lightning'
        self._channel_amount = (1, 1)
        self._exhaust = False
        self._power = False
        if self._upgrade == True:
            self._name += ' +1'
            self._damage += 3
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount[0]} {self._channel_type}.\n'

    def showCard(self):
        print(f'{self._name} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')
    
    def __repr__(self):
        return f'({self._energy}💧) {self._name}'

class ColdSnap(DefectCard):
    def __init__(self, upgraded):
        super().__init__()
        self._name = 'Cold Snap'
        self._rarity = 'Common'
        self._upgrade = upgraded
        self._energy = 1
        self._damage = 6
        self._block = 0
        self._channel_type = 'Frost'
        self._channel_amount = (1, 1)
        self._exhaust = False
        self._power = False
        if self._upgrade == True:
            self._name += ' +1'
            self._damage += 3
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount[0]} {self._channel_type}.\n'

    def showCard(self):
        print(f'{self._name} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')
    
    def __repr__(self):
        return f'({self._energy}💧) {self._name}'

class Barrage(DefectCard):
    def __init__(self, upgraded):
        super().__init__()
        self._name = 'Barrage'
        self._rarity = 'Common'
        self._upgrade = upgraded
        self._energy = 1
        self._damage = 4
        self._block = 0
        self._channel_type = 'Frost'
        self._channel_amount = (0, 0)
        self._exhaust = False
        self._power = False
        if self._upgrade == True:
            self._name += ' +1'
            self._damage += 3
        self._desc = f'Deal {self._damage} damage for each channeled {self._channel_type} Orb.\n'

    def showCard(self):
        print(f'{self._name} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')
    
    def __repr__(self):
        return f'({self._energy}💧) {self._name}'