import itertools
import random

class Enemy():
    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Enemy.id()

class Slime(Enemy):

    def __init__(self, attack, block):
        self.name = 'Slime Noob'
        self.hp = 40
        self.max_hp = 40
        self.attack = attack
        self.block = block

    def intent(self):
        next_move = random.choice(attack, block)
        print(next_move)

    def sayStats(self):
        print(f'\n{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}\n')

    def __repr__(self):
        print({self.name})

class Pigeon(Enemy):

    def __init__(self):
        self.name = 'Basic Pigeon Soldier'
        self.hp = 25
        self.max_hp = 25

    def intent(self):
        values = [3, 4, 5, 6, 7, 8, 10]
        intent = random.randint(1, 2)
        attack = random.choices(values, weights=[8, 8, 8, 2, 2, 1, 1])
        block = random.choices(values, weights=[1, 3, 3, 8, 8, 5, 3])
        if intent == 1:
            for i in attack:
                intent = i
            return f'{self.name} intends to Attack for {intent}.'
        else:
            for i in block:
                intent = i
            return f'{self.name} intends to Block for {intent}.'

    def sayName(self):
        return {self.name}

    def __repr__(self):
        print(f'A {self.name} appears...')

    