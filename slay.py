import itertools

hand = []
card_types = ['Base', 'Attack', 'Defend', 'Skill', 'Power', 'Curse']

class Card:

    id = itertools.count(1).__next__

    def __init__(self):
        self.id = Card.id()
        self.type = card_types[0]

    def __repr__(self):
        return f'({self.id}) {self.type} Card'

class Attack(Card):
    def __init__(self):
        super().__init__()
        self.type = card_types[1]

class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = card_types[2]

hand.append(Card())
hand.append(Attack())
hand.append(Defend())

print(hand)