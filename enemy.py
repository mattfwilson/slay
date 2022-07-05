import itertools
import random

class Enemy():
    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Enemy.id()

class Seagull(Enemy):

    def __init__(self):
        super().__init__()
        self.name = 'Standard Seagull'
        self.hp = 25
        self.max_hp = 25

    def intent(self):
        values = [3, 4, 5, 6, 7, 8, 10]
        intent = random.randint(1, 2)
        attack = random.choices(values, weights=[1, 1, 1, 2, 6, 8, 6])
        block = random.choices(values, weights=[1, 3, 3, 8, 8, 5, 3])
        if intent == 1:
            for i in attack:
                intent = i
            return f'Enemy intends to Attack for {intent}.'
        else:
            for i in block:
                intent = i
            return f'Enemy intends to Block for {intent}.'

    def saySummary(self):
        print(f'{self.name} [{self.id}]')
        print(f'HP: {self.hp}/{self.max_hp}')

    def intro(self):
        print('You encountered an enemy!')
        print(f'A {self.name} waddles in...')

    def __repr__(self):
        print(self.name)

class Pigeon(Enemy):

    def __init__(self):
        super().__init__()
        self.name = 'Basic Pigeon Soldier'
        self.hp = 25
        self.max_hp = 25

    def intent(self):
        values = [3, 4, 5, 6, 7, 8, 10]
        intent = random.randint(1, 2)
        attack = random.choices(values, weights=[8, 8, 8, 2, 2, 1, 1])
        block = random.choices(values, weights=[1, 3, 3, 8, 8, 6, 4])
        if intent == 1:
            for i in attack:
                intent = i
            return f'Enemy intends to Attack for {intent}.'
        else:
            for i in block:
                intent = i
            return f'Enemy intends to Block for {intent}.'

    def saySummary(self):
        print(f'{self.name} [{self.id}]')
        print(f'HP: {self.hp}/{self.max_hp}')

    def intro(self):
        print('You encountered an enemy!')
        print(f'A {self.name} careens down...')

    def __repr__(self):
        print(self.name)

    