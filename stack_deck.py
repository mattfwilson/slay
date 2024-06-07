import random

card_type = ['Attack', 'Skill', 'Power']

class StrikeCard:
    def __init__(self, next_card=None):
        self.type = card_type[0]
        self.energy = 1
        self.value = 6
        self.next_card = next_card
    
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
    def __init__(self, value=int(), next_card=None):
        self.type = card_type[1]
        self.energy = 1
        self.value = 5
        self.next_card = next_card
    
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

class Stack:
    def __init__(self, value=None, limit=5):
        self.top_card = StrikeCard()
        self.size = 0
        self.limit = 5

    def peek(self) -> object:
        return self.top_card

    def add_card(self):
        if self.has_space():
            new_card = random.choice([StrikeCard(), DefendCard()])
            new_card.set_next_card(self.top_card)
            self.top_card = new_card
        else:
            print(f'Cannot add card!')

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

    def stringify(self) -> str:
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
print(stack.stringify())
