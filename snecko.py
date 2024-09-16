import random

class Loop:
    def __init__(self, energy=1):
        self.name = 'Loop'
        self.type = 'Power'
        self.energy = energy

    def __repr__(self):
        return f'({self.energy}) {self.name} - {self.type}'
    
class Reprogram:
    def __init__(self, energy=2):
        self.name = 'Reprogram'
        self.type = 'Skill'
        self.energy = energy

    def __repr__(self):
        return f'({self.energy}) {self.name} - {self.type}'

class MeteorStrike:
    def __init__(self, energy=5):
        self.name = 'Meteor Strike'
        self.type = 'Attack'
        self.energy = energy

    def __repr__(self):
        return f'({self.energy}) {self.name} - {self.type}'

def rand_energy():
    return random.randint(0, 3)

snecko = True

match snecko:
    case True:
        card1 = Loop(rand_energy())
        card2 = Reprogram(rand_energy())
        card3 = MeteorStrike(rand_energy())
    case False:
        card1 = Loop()
        card2 = Reprogram()
        card3 = MeteorStrike()

print(card1)
print(card2)
print(card3)


