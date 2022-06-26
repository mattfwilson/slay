class Card:
    def __init__(self, id):
        self.id = id

class Attack(Card):
    def __init__(self, id):
        super().init(id)
        self.damage = 6

class Defend(Card):
    def __init__(self, id):
        super().init(id)
        self.block = 6

# Test 2