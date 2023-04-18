import itertools
import random

class DefectCard:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(DefectCard.id)
        self._class = 'Defect'

class BallLightning(DefectCard):
    def __init__(self, upgraded=False):
        super().__init__()
        self._name = 'Ball Lightning'
        self.type = 'Common'
        self._upgrade = upgraded
        self._energy = 1
        self._damage = 7
        self._block = 0
        self._channel_type = 'Lightning'
        self._channel_amount = (1, 1)
        self._exhaust = False
        self._power = False
        if self._upgrade == True:
            self._name = 'Ball Lightning +1'
            self._damage += 3
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount[0]} {self._channel_type}.\n'

    def showCard(self):
        print(f'{self._name} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')
    
    def __repr__(self):
        return f'({self._energy}💧) {self._name}'

class ColdSnap(DefectCard):
    def __init__(self, upgraded=False):
        super().__init__()
        self._name = 'Cold Snap'
        self.type = 'Common'
        self._upgrade = upgraded
        self._energy = 1
        self._damage = 6
        self._block = 0
        self._channel_type = 'Frost'
        self._channel_amount = (1, 1)
        self._exhaust = False
        self._power = False
        if self._upgrade == True:
            self._name = 'Cold Snap +1'
            self._damage += 3
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount[0]} {self._channel_type}.\n'

    def showCard(self):
        print(f'{self._name} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')
    
    def __repr__(self):
        return f'({self._energy}💧) {self._name}'

defectCards = [BallLightning(), ColdSnap()]

card1 = BallLightning(False)
card1.showCard()

# card2 = BallLightning(True)
# card2.showCard()

# card3 = ColdSnap(True)
# card3.showCard()

draw = random.choices(defectCards, k=5)
print(draw)