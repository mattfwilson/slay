import itertools
import random

class Enemy():
    
     id = itertools.count(0).__next__

     def __init__(self):
        self.id = Enemy.id()

class Slime(Enemy):

    def __init__(self):
        moves = [3, 4, 5, 6, 7, 8, 10]
        attack = random.choices(moves, weights=[8, 8, 8, 2, 2, 1, 1])
        block = random.choices(moves, weights=[1, 3, 3, 8, 8, 5, 3])
        self.name = 'Slime Noob'
        self.hp = 40
        self.max_hp = 40
        self.attack = attack
        self.defend = block

    def intent(self, attack, block):
        move = random.choidce(attack, block)

    def sayStats(self):
        print(f'\n{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}\n')

    def __repr__(self):
        print(f'\n{self.name} casually slides in...')

class Pigeon(Enemy):

    def __init__(self):
        moves = [4, 5, 6, 7, 8, 10]
        attack = random.choices(moves, weights=[1, 2, 4, 6, 8, 4])
        block = random.choices(moves, weights=[8, 8, 6, 3, 1, 1])
        self.name = 'Basic Pigeon Soldier'
        self.hp = 25
        self.max_hp = 25
        self.attack = attack
        self.defend = block

    def sayName(self):
        print(self.name)

    def sayStats(self):
        print(f'\n{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.attack}, Block: {self.defend}\n')

    def __repr__(self):
        print(f'\n{self.name} careens down...')