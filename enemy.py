import itertools
import random

########################################################################

class Enemy():
    id = itertools.count(0).__next__

    def __init__(self):
        self.id = Enemy.id()

########################################################################

class Pigeon(Enemy):

    def __init__(self):
        super().__init__()
        self.name = '🐦 Standard Pigeon'
        self.hp = random.randint(25, 100)
        self.max_hp = self.hp

    def __repr__(self):
        return f'self.id: {self.id} self.name: {self.name}, self.hp/self.max_hp: {self.hp}/{self.max_hp}'

    def intro(self):
        print('You encountered an enemy!')
        print(f'A {self.name} swoops down...\n')

    def saySummary(self):
        print(f'{self.name}')
        print(f'🩸 HP: {self.hp}/{self.max_hp}')

    def sayID(self):
        return self.id

    def sayName(self):
        return self.name

    def sayHP(self):
        return self.hp

    def sayMaxHP(self):
        return self.max_hp

    def doDamage(self, damage):
        self.hp -= damage
        return self.hp

    def intent(self):
        values = [4, 5, 6, 7, 8, 10, 11]
        intent = random.randint(1, 2)
        attack = random.choices(values, weights=[1, 1, 1, 2, 6, 8, 6])
        block = random.choices(values, weights=[1, 3, 3, 8, 8, 3, 2])
        if intent == 1:
            for i in attack: # prints intent without list brackets (better way to do this?)
                return f'💢 Enemy intends to ⚔  Attack for {i}.'
        else:
            for i in block:
                return f'💢 Enemy intends to 🛡  Block for {i}.'

########################################################################

# class Duck(Enemy):

#     def __init__(self):
#         super().__init__()
#         self.name = '🦆 Anxious Duck'
#         self.hp = 25
#         self.max_hp = 25

#     def sayID(self):
#         print(f'{self.id} {self.name}')

#     def intent(self):
#         values = [3, 4, 5, 6, 7, 8, 10]
#         intent = random.randint(1, 2)
#         attack = random.choices(values, weights=[8, 8, 8, 2, 2, 1, 1])
#         block = random.choices(values, weights=[1, 3, 3, 8, 8, 6, 4])
#         if intent == 1:
#             for i in attack:
#                 intent = i
#             return f'⚔  Enemy intends to ⚔  Attack for {intent}.\n'
#         else:
#             for i in block:
#                 intent = i
#             return f'Enemy intends to 🛡  Block for {intent}.\n'

#     def saySummary(self):
#         print(f'{self.name}')
#         print(f'🩸 HP: {self.hp}/{self.max_hp}')

#     def intro(self):
#         print('You encountered an enemy!')
#         print(f'A {self.name} waddles in...\n')

#     def __repr__(self):
#         print(self.name)

# ########################################################################

# class SpaceCat(Enemy):

#     def __init__(self):
#         super().__init__()
#         self.name = '😾 Space Cat'
#         self.hp = 25
#         self.max_hp = 25

#     def sayID(self):
#         print(f'{self.id} {self.name}')

#     def intent(self):
#         values = [3, 4, 5, 6, 7, 8, 10]
#         intent = random.randint(1, 2)
#         attack = random.choices(values, weights=[8, 8, 8, 2, 2, 1, 1])
#         block = random.choices(values, weights=[1, 3, 3, 8, 8, 6, 4])
#         if intent == 1:
#             for i in attack:
#                 intent = i
#             return f'⚔  Enemy intends to ⚔  Attack for {intent}.\n'
#         else:
#             for i in block:
#                 intent = i
#             return f'Enemy intends to 🛡  Block for {intent}.\n'

#     def saySummary(self):
#         print(f'{self.name}')
#         print(f'🩸 HP: {self.hp}/{self.max_hp}')

#     def intro(self):
#         print('You encountered an enemy!')
#         print(f'A {self.name} readies his stance...\n')

#     def __repr__(self):
#         print(self.name)