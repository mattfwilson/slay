import itertools

class DefectCard:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(DefectCard.id)
        self._class = 'Defect'

class BallLightning(DefectCard):
    def __init__(self, upgraded=False):
        super().__init__()
        self._name = ('Ball Lightning', 'Ball Lightning +1')
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
            self._damage += 3
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount[0]} {self._channel_type}.'

    def showCard(self):
        print(f'{self._name[0]} ({self._energy}💧) - ID: {self._id}')
        print(f'{self._desc}')


    damage = property()

card1 = BallLightning(False)
card1.showCard()

card2 = BallLightning(True)
card2.showCard()