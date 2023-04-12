import itertools

class Card:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(Card.id)

class BallLightning(Card):
    def __init__(self):
        super().__init__()
        self._name = "Ball Lightning"
        self.type = 'common'
        self._upgrade = False
        self._energy = 1
        self._damage = 7
        self._block = None
        self._channel_type = 'Lightning'
        self._channel_amount = 1
        self._desc = f'Deal {self._damage} damage. Channel {self._channel_amount} {self._channel_type}.'
    
    def displayCard(self):
        print(f'{self._name} ({self._energy})')
        print(f'{self._desc}')

card1 = BallLightning()
card1.displayCard()