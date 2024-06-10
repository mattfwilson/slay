import random

card_type = ['Attack', 'Skill', 'Power']
card_debuffs  = ['Vulnerable', 'Weakeness', 'Frail']
card_abilities = ['Exhaust', 'Discard']


class StrikeCard:
    def __init__(self, next_card=None):
        self.name = 'Strike'
        self.type = card_type[0]
        self.energy = 1
        self.value = 6
        self.next_card = next_card
   
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_energy(self):
        return self.energy

    def get_value(self) -> int:
        return self.value

    def get_next_card(self):
        return self.next_card

    def set_next_card(self, next_card):
        self.next_card = next_card

class DefendCard:
    def __init__(self, next_card=None):
        self.name = 'Defend'
        self.type = card_type[1]
        self.energy = 1
        self.value = 5
        self.next_card = next_card
    
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_energy(self):
        return self.energy

    def get_value(self) -> int:
        return self.value

    def get_next_card(self):
        return self.next_card

    def set_next_card(self, next_card):
        self.next_card = next_card

class SurvivorCard:
    def __init__(self, next_card=None):
        self.name = 'Survivor'
        self.type = card_type[1]
        self.energy = 1
        self.value = 8
        self.abilities = card_abilities[1]
        self.next_card = next_card

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    def get_energy(self):
        return self.energy

    def get_value(self) -> int:
        return self.value

    def get_abilities(self):
        return self.abilities

    def get_next_card(self):
        return self.next_card

    def set_next_card(self, next_card):
        self.next_card = next_card

base_cards = [SurvivorCard(), StrikeCard(), DefendCard()]

class Stack:
    def __init__(self, value=None, limit=5):
        self.top_card = StrikeCard()
        self.size = 0
        self.limit = 5

    def peek(self) -> object:
        return self.top_card

    def add_card(self):
        if self.is_empty():
            new_card = random.choices(base_cards, weights=[5, 3, 1])
            print(new_card)
            self.top_card = new_card
        else:
            if self.has_space():
                new_card = random.choices(base_cards, weights=[5, 3, 1])
                new_card = random.choices(StrikeCard(), DefendCard(), SurvivorCard())
                new_card.set_next_card(self.top_card)
                self.top_card = new_card

    def remove_top_card(self):
        self.top_card = self.top_card.get_next_card()

    def has_space(self):
        if self.size < self.limit:
            return True
        else:
            print(f'Deck has no space!')

    def is_empty(self):
        if self.size == 0:
            return True

    def stringify(self):
        str_stack = ''
        top_card = self.peek()
        while top_card:
            if top_card.get_value() != None:
                str_stack += '(' + str(top_card.get_energy()) + ')' + str(top_card.get_type()) + ' ' + str(top_card.get_value()) + ', '
                top_card = top_card.get_next_card()
        return str_stack

stack = Stack(0)
for i in range(5):
    stack.add_card()
    print(stack.get_name())

print(stack.stringify())

