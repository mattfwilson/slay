import itertools
import random

class DefectCard:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(DefectCard.id)
        self._class = 'Defect'

class BallLightning(DefectCard):
    def __init__(self, upgraded):
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
    def __init__(self, upgraded):
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

drawCount = 5
upgraded = False
upgradeCard = (True, False)
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]

card1 = BallLightning(False)
card1.showCard()

hand = []

for count in range(drawCount):
    drawUpgrade = random.choice(upgradeCard)
    print(drawUpgrade)
    if drawUpgrade == True:
        upgraded = True
    if drawUpgrade == False:
        upgraded = False
    hand.append(random.choice(defectCards))

for card in hand:
    print(card)